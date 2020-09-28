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


class JSONStringDriver(IStructureDriver):
    def __init__(self, s: str = "{}"):
        self.string = s

    def __str__(self):
        return self.string

    def read(self) -> Dict:
        return json.loads(self.string)

    def write(self, value: Dict):
        return json.dumps(value)


class SDBuilder:
    def build(self):
        raise NotImplementedError


class JSONFileBuilder(SDBuilder):
    def build(self):
        file_name = input("Enter filename without extension")
        return JSONFileDriver(file_name + ".json")


class PICKLEFileBuilder(SDBuilder):
    def build(self):
        file_name = input("Enter filename without extension")
        return PICKLEFileDriver(file_name + ".pickle")


class JSONStringBuilder(SDBuilder):
    def build(self):
        string = input("Enter dictionary as string ('{keys: items}')")
        return JSONStringDriver(string)


class SDFabric:
    @staticmethod
    def get_sd_driver(driver_name: str, t=True):
        while t:
            if driver_name == "JSONFileDriver":
                return JSONFileBuilder()
            elif driver_name == "PICKLEFileDriver":
                return PICKLEFileBuilder()
            elif driver_name == "JSONStringDriver":
                return JSONStringBuilder()
            else:
                y_n = input("Wrong name driver. Are you want try again? (y/n")
                if y_n in ('y', 'yes', 'Y', 'Yes'):
                    driver_name = input("Please inter driver name")
                else:
                    t = None


if __name__ == "__main__":
    # obj = {
    #     "a": [
    #         {
    #             "a": 1,
    #             "b": True,
    #             "c": "some string"
    #         },
    #         {
    #             "afff": None,
    #             "caaa": "some string 2"
    #         }
    #     ],
    #     "value": (1, 2, 3)
    # }
    #
    # fd = JSONFileDriver("some_file.json")
    # fd.write(obj)
    # obj2 = fd.read()
    # print(obj2)
    # obj2["value"] = tuple(obj2["value"])
    # assert obj == obj2
    # # print(obj == obj2)
    driver_name = input("Please enter driver name > ")
    builder = SDFabric().get_sd_driver(driver_name)
    sd = builder.build()
