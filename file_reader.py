import json, os

class FileReader:
    @staticmethod
    def read_file(username) -> (dict, int):
        filename = "data.json"
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding="UTF-8") as file:
                data = {username: {"Quiz": {}, "FreeForm": {}}}
                json.dump(data, file)
        if os.path.getsize(filename) != 0:
            with open(filename, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                max_id = 0
                # Iterate through the nested dictionary
                try:
                    for section in data[username].values():
                        # print(section)
                        for question in section.values():
                            if '_question_id' in question:
                                current_id = int(question['_question_id'])
                                if max_id is None or current_id > max_id:
                                    max_id = current_id
                    question_id = max_id + 1
                    return data, question_id
                except Exception as e:
                    print(e)
