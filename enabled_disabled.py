class EnabledDisabled:
    def __init__(self) -> None:
        pass

    @staticmethod
    def change_answer(username, data, question_id, writer):
        # This method accepts the question id an changes active parameter from one
        # boolean to another if called for the specific question with a given id.
        q_type_id = None
        for q_type, details in data[username].items():
            for question, detail in details.items():
                if question_id == detail['_question_id']:
                    q_type_id = q_type

        for question, details in data[username][q_type_id].items():
            if str(details['_question_id']) == str(question_id):
                match data[username][q_type_id][question]['active']:
                    case True:
                        user_inp = input(f'You are going to disable "{question}" question, which is currently enabled. Do you wish to continue (y/n)?: ')
                        if user_inp.lower() == "exit":
                            return
                    case False:
                        user_inp = input(f'You are going to enable "{question}" question, which is currently disabled. Do you wish to continue (y/n)?: ')
                        if user_inp.lower() == "exit":
                            return
                    case _:
                        user_inp = ""
                while True:
                    if user_inp.upper() in ["N", "NO"]:
                        return
                    elif user_inp.upper() in ["Y", "YES"]:
                        break
                    else:
                        user_inp = input("Please enter y or n: ")
                data[username][q_type_id][question]['active'] = not details['active']
                break
        # After that the program immediately writes to the file that was entered
        writer.write_file(data)

    @staticmethod
    def enable_disable(reader, writer):
        username = reader.username
        data = reader.read_file()[0]
        # Here I ask for the user to enter ids of the questions he wants to enable or disable
        while True:
            try:
                user_input = input('Which question(s) would you like to enable/disable (e.g. "1,2,9" or "1 2 9")?\nInput: ')
                if user_input.lower() == "exit":
                    return
                id_list = [num.strip() for num in user_input.replace(',', ' ').split()]
            except ValueError:
                print('Please enter numerical value(s) (e.g. "1,2,9" or "1 2 9"): ')
                continue
            break
        # I call change_answer method to update the questions with given ids
        for question_id in id_list:
            EnabledDisabled.change_answer(username, data, question_id, writer)
        print('Successfully updated questions with id:', end = ' ')
        for question_id in id_list:
            try:
                if question_id == id_list[-2]:
                    print(question_id, end = ' and ')
                elif question_id != id_list[-1]:
                    print(question_id, end=', ')
                else:
                    print(question_id, end=".\n")
            except IndexError:
                print(question_id, end=".\n")