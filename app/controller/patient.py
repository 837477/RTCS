import requests
import datetime
from dependencies import Config
from model.mongodb.patients import Patients


def get_api_data_infected_persons(auth_key):
    url = "http://openAPI.seoul.go.kr:8088/{}/json/Corona19Status/1/30/".format(auth_key)
    return requests.get(url).json()


def get_api_data_patients(auth_key):
    url = "http://openAPI.seoul.go.kr:8088/{}/json/TbCorona19CountStatus/1/1/".format(auth_key)
    return requests.get(url).json()


def get_infected_persons():
    api_data = get_api_data_infected_persons(Config.API_SECRET_KEY)
    result = api_data['Corona19Status']['row']
    return result


def get_patients(db):
    today = datetime.date.today().strftime('%Y.%m.%d.00')
    result = Patients(db).get_patient(today)
    if not result:
        try:
            api_data = get_api_data_patients(Config.API_SECRET_KEY)
            result = api_data['TbCorona19CountStatus']['row'][0]
            Patients(db).upsert_patient(result)
        except:
            result = Patients(db).get_patient_recent()
    
    return result

