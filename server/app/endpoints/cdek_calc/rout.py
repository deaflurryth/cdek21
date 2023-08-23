import httpx
from fastapi import APIRouter

from app.endpoints.cdek_calc.utils import client, dict_city_code
from pydantic import BaseModel
from pydantic.class_validators import Optional

# http.client.HTTPConnection.debuglevel = 1
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
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
    goods = [
        {
            'weight': 10,
            'length': 20,
            'width': 30,
            'height': 40,
        }
    ]

    response = client.get_delivery_cost(sender_city_code, receiver_city_code, goods)
    print(response)

    return response


@calculator_cdek.get('/fsdaf')
async def get_cdek_cities():
    url = "https://api.edu.cdek.ru/v2/location/cities"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            cities_data = response.json()
            return cities_data
        else:
            return None
