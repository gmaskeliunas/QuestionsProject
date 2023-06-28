import json

class FileWriter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def write_file(data):
        filename = "data.json"
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)