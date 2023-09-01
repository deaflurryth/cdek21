import httpx
from fastapi import APIRouter

from app.endpoints.cdek_calc.utils import client, dict_city_code, CDEK2Client
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
    client = CDEK2Client(client_id="R7R9cfqq0ua0pKxlDb3bSVUvtEIzer9J", client_secret="P85B26JBZE7YmifsrKlU4DSKn2RVHpU4")
    goods = [
        {
            'weight': 10,
            'length': 20,
            'width': 30,
            'height': 40,
        }
    ]

    response = client.get_delivery_cost(sender_city_code, receiver_city_code, goods)
    return response


