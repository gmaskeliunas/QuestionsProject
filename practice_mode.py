import random
from weights_adjust import Weights
from question_statistics import Statistics

class PracticeMode:
    def __init__(self) -> None:
        pass

    @staticmethod
    def practice(reader, writer):
        username = reader.username
        data = reader.read_file()[0]
        # I ask what type of questions the user would like to practice
        question_type = input(
            f'Please type what type of questions you want to practice: \n1. Quiz questions\n2. Free-form questions\n{username}: '
            )
        while True:
            if question_type.lower() not in ["1", "2", "exit"]:
                question_type = input(f'Please input the correct mode!\n{username}: ')
            elif question_type.lower() == "exit":
                return
            else:
                break
        if question_type.upper() == "1":
            questions = "Quiz"
        else:
            questions = "FreeForm"
        enabled_data = Statistics.enabled_questions(data, username, questions)
        quiz_questions = enabled_data[username][questions]
        quiz_keys = list(quiz_questions.keys())
        if len(quiz_keys) < 5:
            print(f"Please add or enable more questions so you have at least 5.\nCurrently you have {len(quiz_keys)} questions for selected mode.")
            return
        # I begin the practice with a while loop so it loops until the user types exit
        while True:
            # Note, here I assign quiz_questions to the temporary questions and answers since they only contain active questions
            quiz_questions = enabled_data[username][questions]
            quiz_keys = list(quiz_questions.keys())
            # If the user selects type of questions that are not available the user is reprompted to select.
            if len(quiz_keys) == 0:
                print("Please select a mode which has added questions")
                PracticeMode.practice(reader, writer)
            # I put all the weights for questions into a list and then pass it to random.choices method
            weights = [question["weight"] for question in quiz_questions.values()]
            random_key = random.choices(quiz_keys, weights=weights)[0]
            random_value = quiz_questions[random_key]
            print('\nQuestion:',random_key)
            correct_nr = None
            if questions == "Quiz":
                print('The choices are:')
                random.shuffle(random_value['_choices'])
                for i, choice in enumerate(random_value['_choices']):
                    print(f"{i+1}. {choice}")
                    if choice == random_value['_answer']:
                        correct_nr = i+1
                data[username][questions][random_key]['times_showed'] += 1
                random_ans = input(f"Please enter your answer\n{username}: ")
                if random_ans.lower() == "exit":
                    return
                while True:
                    try:
                        ans = int(random_ans)
                        if ans in [1,2,3,4,5,6]:
                            break
                    except Exception as e:
                        print(e)
                        random_ans = input(f"Please enter a number\n{username}: ")
                        continue
                if ans == correct_nr:
                    print("Correct!")
                    data[username][questions][random_key]['correct'] += 1
                else:
                    print(f"False! The correct answer is {random_value['_answer']}")
            # I increment by one the times showed value after the question has been printed to the console
            else:
                random_ans = input(f"Please enter your answer.\n{username}: ")
                data[username][questions][random_key]['times_showed'] += 1
                if random_ans.lower() == "exit":
                    return
                # I print to the user if the answer was correct or not, and if not, I print the answer
                if random_ans.lower() == random_value['_answer'].lower():
                    print("Correct!")
                    data[username][questions][random_key]['correct'] += 1
                else:
                    print(f"False! The correct answer is {random_value['_answer']}")
            # Here I calculate the accuracy by dividing correct amount by the times showed amount and round it to 2 decimal places.
            data[username][questions][random_key]['accuracy'] = round(data[username][questions][random_key]['correct'] / data[username][questions][random_key]['times_showed'], 2)
            print(f"The accuracy for this question is: {data[username][questions][random_key]['accuracy']}")
            Weights.adjust_weights(data, username, random_key, questions)
            writer.write_file(data)