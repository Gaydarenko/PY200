from abc import ABC, abstractmethod
from typing import Dict
import json
import pickle


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def write(self, value: Dict):
        raise NotImplementedError


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> Dict:
        with open(self.filename) as file:
            return json.load(file)

    def write(self, value: Dict):
        with open(self.filename, "w") as file:
            json.dump(value, file)


class PICKLEFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> Dict:
        with open(self.filename, "rb") as file:
            return pickle.load(file)

    def write(self, value: Dict):
        with open(self.filename, "wb") as file:
            pickle.dump(value, file)


class JSONStringdriver(IStructureDriver):
    def __init__(self, s: str = "{}"):
        self.string = s

    def __str__(self):
        return self.string

    def read(self) -> Dict:
        return json.loads(self.string)

    def write(self, value: Dict):
        return json.dumps(value)

obj = {
    "a": [
        {
            "a": 1,
            "b": True,
            "c": "some string"
        },
        {
            "afff": None,
            "caaa": "some string 2"
        }
    ],
    "value": (1, 2, 3)
}

fd = JSONFileDriver("some_file.json")
fd.write(obj)
obj2 = fd.read()
print(obj2)
obj2["value"] = tuple(obj2["value"])
assert obj == obj2
# print(obj == obj2)
