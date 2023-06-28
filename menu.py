import sys
from add_mode import AddMode
from question_statistics import Statistics
from enabled_disabled import EnabledDisabled
from practice_mode import PracticeMode
from test_mode import TestMode
from file_reader import FileReader
from file_writer import FileWriter

class Menu:

    def __init__(self, user) -> None:
        self.mode = "1"
        self.user = user

    @staticmethod
    def display_menu() -> None:
        print("===== MENU =====")
        print("1. Add Mode")
        print("2. Statistics Viewing")
        print("3. Enable/Disable Questions Mode")
        print("4. Practice Mode")
        print("5. Test Mode")
        print("6. Profile Selection")
        print("7. Exit")
        print("================")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if mode.lower() not in ["1", "2", "3", "4", "5", "6", "exit"]:
            print("Please select a correct mode from the menu.")
            self.display_menu()
        else:
            self._mode = mode

    def select_mode(self):
        user_mode = input(f"{self.user.username}: ")
        self.mode = user_mode

    def invoke_mode(self):
        reader = FileReader(self.user)
        writer = FileWriter()
    # This method invokes the selected menu item by calling respective methods
        match self.mode.lower():
            case "1":
                AddMode.add_questions(reader, writer)
            case "2":
                Statistics.view_statistics(reader)
            case "3":
                Statistics.view_statistics(reader)
                EnabledDisabled.enable_disable(reader, writer)
            case "4":
                PracticeMode.practice(reader, writer)
            case "5":
                TestMode.test_mode(reader, writer)
            case "6":
                new_user = input("Please enter a new username: ")
                while True:
                    if new_user.lower() == "exit":
                        return
                    elif new_user != self.user.username:
                        self.user.username = new_user
                        print(f"Successfully switched to {new_user} user!")
                        return
                    elif new_user == self.user.username:
                        new_user = input("Please enter a different username: ")
                        continue
            case "exit":
                sys.exit("The program closed successfully.")