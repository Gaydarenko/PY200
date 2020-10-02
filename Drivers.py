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
    def build(self, filename=None):
        if not filename:
            filename = input("Enter filename without extension > ") + ".json"
        return JSONFileDriver(filename)


class PICKLEFileBuilder(SDBuilder):
    def build(self, filename=None):
        if not filename:
            filename = input("Enter filename without extension > ") + ".pickle"
        return PICKLEFileDriver(filename)


class JSONStringBuilder(SDBuilder):
    def build(self):
        string = input("Enter dictionary as string ('{keys: items}') > ")
        return JSONStringDriver(string)


class SDFabric:
    @staticmethod
    def get_driver_base():
        return {"json": "JSONFileDriver", "pickle": "PICKLEFileDriver"}

    @staticmethod
    def get_sd_driver(driver_name: str):
        builders = {
            "JSONFileDriver": JSONFileBuilder,
            "PICKLEFileDriver": PICKLEFileBuilder,
            "JSONStringDriver": JSONStringBuilder
        }

        driver = builders.get(driver_name)
        if driver:
            return driver()
        else:
            y_n = input("Wrong name driver. Are you want try again? (y/n)")
            if y_n in ('y', 'yes', 'Y', 'Yes'):
                driver_name = input("Please inter driver name > ")
                SDFabric.get_sd_driver(driver_name)


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
    # l1 = LinkedList()
