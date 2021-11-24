import json
from model.mongodb import Model


class Patients(Model):
    def upsert_patient(self, document: dict):
        self.col.update_one(
            {'S_DT': document['S_DT']},
            {'$set': self.schemize(document)},
            upsert=True
        )
    
    def get_patient(self, date: str):
        return self.col.find_one(
            {'S_DT': date},
            {'_id': 0}
        )
