import pytz

from fastapi import FastAPI, HTTPException, status
from schema import VipDueDate
from aiohttp import ClientSession

from datetime import datetime

app = FastAPI()
session = None

TIME_ZONE = pytz.timezone('Asia/Shanghai')

@app.on_event('startup')
async def on_start():
    global session
    session = ClientSession()


@app.on_event('shutdown')
async def on_shutdown():
    await session.close()

@app.get('/vip', response_model=VipDueDate)
async def get_vip_due_date(uid: str):
    api = f'https://api.bilibili.com/x/web-interface/card?mid={uid}'
    headers = {'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}

    try:
        async with session.get(api, headers=headers, timeout=10) as resp:
            ret = await resp.json()
    except Exception as e:
        print(e)

    code = ret['code']

    if code != 0:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=ret)

    card = ret['data']['card']

    vip = card['vip']
    # 1498924800000 => 多了 3 个 0，int 型
    timestamp = vip['due_date'] // 1000
    is_vip = vip['status'] == 1

    result_dict = {
        'uid': card['mid'],
        'name': card['name'],
        'vip_due_date': datetime.strftime(datetime.fromtimestamp(timestamp, tz=TIME_ZONE), '%Y/%m/%d %H:%M:%S'),
        'is_vip': is_vip,
        'fans': card['fans'],
        'attention': card['attention'],
        'sign': card['sign'],
        'space': f'https://space.bilibili.com/{card["mid"]}'
    }

    return VipDueDate(**result_dict)
