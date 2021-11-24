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
