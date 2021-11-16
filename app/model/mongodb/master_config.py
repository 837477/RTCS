import json
import datetime
from model.mongodb import Model


class MasterConfig(Model):
    def upsert_config(self, document: dict):
        self.col.update_one(
            {'key': document['key']},
            {'$set': self.schemize(document)},
            upsert=True
        )

    def get_data(self, key: str):
        return self.col.find_one({'key': key})

    def init_location(self):
        data = open("model/mongodb/initial_data/location.json")
        data = json.load(data)
        document = {
            'key': 'location',
            'value': data
        }
        self.upsert_config(document)

