from dataclasses import dataclass


@dataclass
class Stato:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)

    def __eq__(self, other):
        if other is None:
            return False
        return self.CCode == other.CCode

    def __lt__(self, other):
        return self.StateNme < other.StateNme
