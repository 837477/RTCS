import json
from model.mongodb import Model


class Vaccine(Model):
    def upsert_vaccine(self, document: dict):
        self.col.update_one(
            {'S_VC_DT': document['S_VC_DT']},
            {'$set': self.schemize(document)},
            upsert=True
        )
    
    def get_vaccine(self, date: str):
        return self.col.find_one(
            {'S_VC_DT': date},
            {'_id': 0}
        )
