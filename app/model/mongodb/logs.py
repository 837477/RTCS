import json
from model.mongodb import Model


class Logs(Model):
    def insert_log(self, document: dict):
        self.col.insert_one(
            self.schemize(document)
        )
