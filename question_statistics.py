from file_reader import FileReader

class Statistics:
    def __init__(self, question_id):
        self.question_id = question_id
        self.active = True
        self.times_showed = 0
        self.correct = 0
        self.weight = 1.0
        self.accuracy = 0.0

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        if isinstance(question_id, str) is not True:
            raise ValueError("Question id variable is not an int type.")
        self._question_id = question_id

    @staticmethod
    def enabled_questions(data, username, q_type):
        tmp_data = {username : {q_type : {}}}
        for question, details in data[username][q_type].items():
            if data[username][q_type][question]['active'] == True:
                # print(tmp_data[username][q_type])
                tmp_data[username][q_type].update({question : details})
        return tmp_data

    @staticmethod
    def print_questions(quiz_data):
        # This method iterates through the questions data and prints out the most important metrics and parameters
        for question, details in quiz_data.items():
            question_id = details['_question_id']
            answer = details['_answer']
            active = details['active']
            num_times_shown = details['times_showed']
            accuracy = details['accuracy']
            print(f"\nID: {question_id}")
            print(f"Is active: {active}")
            print(f"Question: {question}")
            print(f"Accuracy: {round(accuracy*100, 0)}%")
            print(f"Number of times showed: {num_times_shown}")
            print(f"Correct answer: {answer}")

    @staticmethod
    def match_enabled_data(question_type, data, username):
        match question_type.upper():
            case '1':
                quiz_data = data[username]['Quiz']
                Statistics.print_questions(quiz_data)
            case '2':
                free_data = data[username]['FreeForm']
                Statistics.print_questions(free_data)
            case '3':
                quiz_data = data[username]['Quiz']
                Statistics.print_questions(quiz_data)
                free_data = data[username]['FreeForm']
                Statistics.print_questions(free_data)
            case _:
                ...
    @staticmethod
    def view_statistics(username):
        data = FileReader.read_file(username)[0]
        question_type = input(
            f'Please type what type of questions you want to view: \n1. Quiz questions\n2. Free-form questions\n3. All questions\n{username}: '
        )
        while True:
            if question_type.lower() not in ["1", "2", "3", "exit"]:
                question_type = input(f'Please input the correct mode!\n{username}: ')
            elif question_type.lower() == "exit":
                return
            else:
                break
        Statistics.match_enabled_data(question_type, data, username)
