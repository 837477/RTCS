import json
from model.mongodb import Model


class LocalStatus(Model):
    def upsert_local_status(self, document: dict):
        self.col.update_one(
            {'JCG_DT': document['JCG_DT']},
            {'$set': self.schemize(document)},
            upsert=True
        )
    
    def get_local_status(self, date: str):
        return self.col.find_one(
            {'JCG_DT': date},
            {
                '_id': 0,
                '_created': 0,
                '_updated': 0,
                '_version': 0
            }
        )
