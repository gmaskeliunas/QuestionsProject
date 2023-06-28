from menu import Menu
from user import User


def main():

    username = input("Please enter your username: ")
    user = User(username)
    menu = Menu(user)

    while True:
        menu.display_menu()
        menu.select_mode()
        menu.invoke_mode()

if __name__ == "__main__":
    main()