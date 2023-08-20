from fastapi import APIRouter

from app.endpoints.cdek_calc.utils import client

# http.client.HTTPConnection.debuglevel = 1
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
calculator_cdek = APIRouter(prefix="/cdek_calclulator")



@calculator_cdek.get("/cdek_calc")
def calc_cost_delivery(sender_city_code: int, receiver_city_code: int):

    goods = [
        {
            'weight': 1000,
            'length': 10,
            'width': 15,
            'height': 20,
        }
    ]

    # Вызываем метод для расчета стоимости доставки
    response = client.get_delivery_cost(sender_city_code, receiver_city_code, goods)
    return response
