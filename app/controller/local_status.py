import requests
import datetime
from dependencies import Config
from model.mongodb.local_status import LocalStatus

def get_api_data(auth_key):
    url = "http://openAPI.seoul.go.kr:8088/{}/json/TbCorona19CountStatusJCG/1/1/".format(auth_key)
    return requests.get(url).json()


def get_all_local_status(db):
    today = datetime.date.today().strftime('%Y.%m.%d.00')
    result = LocalStatus(db).get_local_status(today)
    if not result:
        api_data = get_api_data(Config.API_SECRET_KEY)
        result = api_data['TbCorona19CountStatusJCG']['row'][0]
        LocalStatus(db).upsert_local_status(result)

    return result
