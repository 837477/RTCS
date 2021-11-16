import requests
import datetime
from dependencies import Dependencies, Config
from model.mongodb.master_config import MasterConfig

def get_data(auth_key, _type):
    today = datetime.date.today().strftime('%Y.%m.%d.00')
    url = "http://openAPI.seoul.go.kr:8088/{}/{}/TbCorona19CountStatusJCG/1/5/{}".format(auth_key, _type, today)
    data = requests.get(url).json()

    result = None
    if data['TbCorona19CountStatusJCG']['RESULT']['CODE'] == "INFO-000":
        result = {
            'date': today,
            'infected': data['TbCorona19CountStatusJCG']['row'][0]
        }

    return result


def mapping_location(location_name: str):    
    location_dict = MasterConfig(Dependencies.db).get_data('location')
    location_dict = location_dict['value']

    return location_dict[location_name]
