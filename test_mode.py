import random
from datetime import datetime
from question_statistics import Statistics

class TestMode:
    def __init__(self) -> None:
        pass

    @staticmethod
    def test_mode(reader, writer):
        # Test mode is similar to the practice mode but I do not change the weights here..
        # If the user hasn't already entered the file_path the program prompts for the file path.
        print("\nYou entered the test mode.")
        username = reader.username
        data = reader.read_file()[0]
        question_type = input(
            f'Please enter which test you want to take: \n1. Quiz questions\n2. Free-form questions\n{username}: '
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
        # I assing quiz questions to the active ones only, then I prompt the user with how many questions would he like to be tested with.
        enabled_data = Statistics.enabled_questions(data, username, questions)
        quiz_questions = enabled_data[username][questions]
        quiz_keys = list(quiz_questions.keys())
        if len(quiz_keys) < 5:
            print(f"Please add or enable more questions so you have at least 5.\nCurrently you have {len(quiz_keys)} questions for selected mode.")
            return
        if len(quiz_keys) == 0:
            print("Please select a mode which has added questions")
            TestMode.test_mode(reader, writer)
        num_q = input(f"Please select how many questions you want to take ({len(quiz_keys)} are available): ")
        # I check if the value that the user entered is correct and doesn't go higher than the amount of questions available
        while True:
            try:
                num_q = int(num_q)
                if num_q <= len(quiz_keys) or num_q > 0:
                    break
                else:
                    continue
            except ValueError:
                print(f'Please enter numerical value between 1 and {len(quiz_keys)}')
                continue
        # I create a variable score that will keep track of the amount of correctly answered questions
        # After that I iterate using for loop until the desired amount of test questions are shown
        score = 0
        for i in range(1, num_q+1):
            # Here I use choice for it to have equal chance to be chosen from all of the questions and after that I remove the selected key
            # from the available question list. By doing that I ensure that the question will not repeat again.
            random_key = random.choice(quiz_keys)
            quiz_keys.pop(quiz_keys.index(random_key))
            random_value = quiz_questions[random_key]
            # Similarly as in practice mode I print questions and answers
            print(f'\nQuestion ({i}/{num_q}):',random_key)
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
                    score+=1
                    data[username][questions][random_key]['correct'] += 1
            else:
                random_ans = input(f"Please enter your answer\n{username}: ")
                if random_ans.lower() == random_value['_answer'].lower():
                    score+=1
                    data[username][questions][random_key]['correct'] += 1

            if random_ans.lower() == "exit":
                break
            # I update the metrics, but don't change the weights.
            data[username][questions][random_key]['times_showed'] += 1
            data[username][questions][random_key]['accuracy'] = round(data[username][questions][random_key]['correct'] / data[username][questions][random_key]['times_showed'], 2)
            writer.write_file(data)
        # I print out the respective message to the user based on the score
        if score == num_q:
            print(f'Congratulations, you score is perfect, you answered {score} out of {num_q} questions!')
        elif score/num_q >= 0.8:
            print(f'Congratulations, you score is {int(round(score/num_q*100, 2))}%')
        elif score/num_q < 0.8:
            print(f'You scored: {int(round(score/num_q*100, 2))}%')
        # I then create a file that has the original file name, only it has an added _scores.txt name+extension
        file_name = "scores.txt"
        # I then write to it the score and the date when the test was finished. I also note the type of test the user took
        with open(file_name, "a+", encoding="UTF-8") as file:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
            if question_type == "1":
                file.write(f"{username} took a test quiz and scored {int(round(score/num_q*100, 2))}%. Date: {formatted_datetime}.\n")
            else:
                question_type = "free-form"
                file.write(f"{username} took a free-form test and scored {int(round(score/num_q*100, 2))}%. Date: {formatted_datetime}.\n")