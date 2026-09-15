from dataclasses import dataclass
@dataclass
class State:
    id:str
    airport_id: list #lista airports

    def __str__(self):
        return str(self.id)
    def __repr__(self):
        return str(self.id)
    def __hash__(self):
        return hash(self.id)

