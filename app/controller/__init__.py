from model.mongodb.master_config import MasterConfig


def map_naming(db, document: dict, key: str):
    name_dict = MasterConfig(db).get_data(key)['value']
    result = {}
    for key, value in document.items():
        result[name_dict[key][0]] = {'value': value, 'en_name': name_dict[key][1]}
    return result
