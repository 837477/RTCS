import requests
import datetime
from dependencies import Config
from model.mongodb.vaccine import Vaccine

def get_api_data(auth_key):
    url = "http://openAPI.seoul.go.kr:8088/{}/json/tvCorona19VaccinestatNew/1/1/".format(auth_key)
    return requests.get(url).json()


def get_vaccine_status(db):
    today = datetime.date.today().strftime('%Y.%m.%d.00')
    result = Vaccine(db).get_vaccine(today)
    if not result:
        api_data = get_api_data(Config.API_SECRET_KEY)
        result = api_data['tvCorona19VaccinestatNew']['row'][0]
        Vaccine(db).upsert_vaccine(result)
    
    return result
