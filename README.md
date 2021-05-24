## B站用户会员过期时间查询API

在线地址：

https://5pdfwb.deta.dev/vip?uid=2

修改`uid=`后面的数字为你想查询的用户的uid。

如何获取uid？:

*[如何获取B站用户UID_百度搜索 (baidu.com)](https://www.baidu.com/s?ie=UTF-8&wd=如何获取B站用户UID)*

**使用提供免费托管FastAPI的[Deta](https://docs.deta.sh/docs/micros/getting_started)**

结果解释：

```json
{
    uid: "2",
    name: "碧诗",
    space: "https://space.bilibili.com/2",
    vip_due_date: "2093/06/22 00:00:00", // 会员过期时间
    fans: 960046, // 粉丝数
    attention: 234, // 关注数
    sign: "kami.im 直男过气网红 # av362830 “We Are Star Dust”", // 签名
    is_vip: true // 是否是大会员
}
```

### 本地运行

确保你安装了 docker 和 docker-compose，在项目根文件夹下输入`docker-compose up`构建并运行项目，然后访问: https://127.0.0.1:8000/vip?uid=2