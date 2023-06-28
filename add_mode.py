from file_reader import FileReader
from file_writer import FileWriter
from quiz_question import QuizQuestion
from free_form_question import FreeFormQuestion
from question_statistics import Statistics

class AddMode:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_questions(reader, writer):
        username = reader.username
        data, question_id = reader.read_file()
        enabled_data = Statistics.enabled_questions(data, username, "Quiz")
        q_len = len(enabled_data[username]["Quiz"])
        enabled_data = Statistics.enabled_questions(data, username, "FreeForm")
        ff_len = len(enabled_data[username]["FreeForm"])
        if q_len < 5:
            print(f'You have {q_len} active quiz questions, please add at least {5-q_len} more quiz questions.')
        if ff_len < 5:
            print(f'You have {ff_len} active free-from questions, please add at least {5-ff_len} more free-form questions.')
        try:
            adding_mode = input(f'What type of question you would like to add? (To exit, type "exit")\n1. Quiz question\n2. Free-form question\n{username}: ')
            while True:
                if adding_mode.lower() not in ["1", "2", "exit"]:
                    adding_mode = input(f"Enter either 1 or 2.\n{username}: ")
                elif adding_mode == "1":
                    user_question = input(f'Enter a quiz question (to return to menu type "exit")\n{username}: ')
                    while True:
                        try:
                            if user_question in [""]:
                                user_question = input(f"Please enter a valid question!\n{username}: ")
                            elif user_question.lower() == "exit":
                                return
                            else:
                                break
                        except Exception as e:
                            print(e)
                    while True:
                        try:
                            i = input(f'How many choices (to return to menu type "exit")?\n{username}: ')
                            if i.lower() == "exit":
                                return
                            elif not 1 < int(i) < 7:
                                print("You can enter from 2 to 6 choices!")
                                continue
                            else:
                                break
                        except ValueError:
                            print("Please input an integer! ")
                            continue
                    answer = input(f'Enter the correct answer (to return to menu type "exit").\n{username}: ')
                    while True:
                        try:
                            if answer in [""]:
                                answer = input(f"Please enter a valid answer!\n{username}: ")
                            elif answer.lower() == "exit":
                                return
                            else:
                                break
                        except Exception as e:
                            print(e)
                    temp_ans = [answer]
                    for _ in range(int(i)-1):
                        tmp = input(f"Add an answer choice\n{username}: ")
                        while True:
                            if tmp != answer:
                                temp_ans.append(tmp)
                                break
                            tmp = input(f"Please add an answer choice that does not match with the correct answer\n{username}: ")
                    quiz_question = QuizQuestion(user_question, answer, temp_ans)
                    json_quiz_q = dict(quiz_question.__dict__)
                    print(json_quiz_q)
                    json_quiz_q.pop("_question")
                    quiz_q_stats = Statistics(str(question_id))
                    json_q_stats = dict(quiz_q_stats.__dict__)
                    data[username]["Quiz"].update({quiz_question.question: json_quiz_q})
                    data[username]["Quiz"][quiz_question.question].update(json_q_stats)
                    enabled_quiz_q = Statistics.enabled_questions(data, username, "Quiz")
                    q_len = len(enabled_quiz_q[username]["Quiz"])
                    if q_len < 5:
                        print(f'Add {5-q_len} more question(s).')
                    writer.write_file(data)
                    question_id += 1
                elif adding_mode == "2":
                    user_question = input(f'Enter a free-form question (to return to menu type "exit").\n{username}: ')
                    while True:
                        try:
                            if user_question in [""]:
                                user_question = input(f"Please enter a valid question!\n{username}: ")
                            elif user_question.lower() == "exit":
                                return
                            else:
                                break
                        except Exception as e:
                            print(e)
                    answer = input(f'Enter the correct answer (to return to menu type "exit")\n{username}: ')
                    while True:
                        try:
                            if answer in [""]:
                                answer = input(f"Please enter a valid answer!\n{username}: ")
                            elif answer.lower() == "exit":
                                return
                            else:
                                break
                        except Exception as e:
                            print(e)
                    ff_question = FreeFormQuestion(user_question, answer)
                    ff_q_stats = Statistics(str(question_id))
                    json_q_stats = dict(ff_q_stats.__dict__)
                    json_quiz_q = dict(ff_question.__dict__)
                    json_quiz_q.pop('_question')
                    data[username]["FreeForm"].update({ff_question.question:json_quiz_q})
                    data[username]["FreeForm"][ff_question.question].update(json_q_stats)
                    enabled_data = Statistics.enabled_questions(data, username, "FreeForm")
                    ff_len = len(enabled_data[username]["FreeForm"])
                    if ff_len < 5:
                        print(f'Add {5-ff_len} more question(s).')
                    writer.write_file(data)
                    question_id += 1
                elif adding_mode.lower() == "exit":
                    return
        except Exception as e:
            print("An unexpected error occurred:", str(e))
