from pydantic import BaseModel

class VipDueDate(BaseModel):
    uid: str
    name: str
    space: str

    vip_due_date: str

    fans: int
    attention: int
    sign: str

    is_vip: bool