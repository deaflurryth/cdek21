import httpx
from fastapi import APIRouter

from app.endpoints.cdek_calc.utils import dict_city_code, CDEK2Client
from pydantic import BaseModel
from pydantic.class_validators import Optional
from app.config import CLIENT_ID, CLIENT_SECRET

calculator_cdek = APIRouter()


class Dimensions(BaseModel):
    weight: int
    length: Optional[int] = 10
    width: Optional[int] = 10
    height: Optional[int] = 10


class FormCalc(BaseModel):
    sender_city_code: str
    receiver_city_code: str
    goods: Dimensions


@calculator_cdek.post("/cdek_calc")
def calc_cost_delivery(data: FormCalc):
    sender_city_code = dict_city_code[data.sender_city_code.title()]
    receiver_city_code = dict_city_code[data.receiver_city_code.title()]
    client = CDEK2Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    goods = [
        {
            'weight': data.goods.weight,
            'length': data.goods.length,
            'width': data.goods.width,
            'height': data.goods.height,
        }
    ]

    response = client.get_delivery_cost(sender_city_code, receiver_city_code, goods)
    return response


