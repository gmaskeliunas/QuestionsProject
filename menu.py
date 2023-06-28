import sys
from add_mode import AddMode
from question_statistics import Statistics
from enabled_disabled import EnabledDisabled
from practice_mode import PracticeMode
from test_mode import TestMode

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
# This method invokes the selected menu item by calling respective methods
        match self.mode.lower():
            case "1":
                AddMode.add_questions(self.user.username)
                # self.adding_questions()
            case "2":
                Statistics.view_statistics(self.user.username)
            case "3":
                Statistics.view_statistics(self.user.username)
                EnabledDisabled.enable_disable(self.user.username)
                # self.enable_disable()
            case "4":
                PracticeMode.practice(self.user.username)
            case "5":
                TestMode.test_mode(self.user.username)
            case "6":
                ...
                # self.test_mode()
            case "exit":
                sys.exit("The program closed successfully.")