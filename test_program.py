from builtin_test import set_keyboard_input
from user import User
from file_reader import FileReader
from file_writer import FileWriter
from enabled_disabled import EnabledDisabled
from menu import Menu

# Testing whether FileReader correctly reads the Turing users questions in data.json file
def test_reader():
    reader = FileReader(User("Turing"))
    username = reader.username
    data = reader.read_file()[0]
    assert data[username]["FreeForm"]["Hello,"]["_answer"] == "World"
    assert data[username]["FreeForm"]["What's 3+3?"]["_answer"] == "6"
    assert data[username]["FreeForm"]["What's 4+4?"]["_answer"] == "8"
    assert data[username]["FreeForm"]["What's 5+5?"]["_answer"] == "10"
    assert data[username]["FreeForm"]["What's 6+6?"]["_answer"] == "12"

# Testing enable/disable functionality; The test fails every second time, because this function overrides the data.json file
def test_enable_disable():
    reader = FileReader(User("Turing"))
    writer = FileWriter()
    username = reader.username
    set_keyboard_input(["10 11", "y", "n"])
    EnabledDisabled.enable_disable(reader, writer)
    data = reader.read_file()[0]
    assert data[username]["FreeForm"]["What's 6+6?"]["active"] is False
    assert data[username]["FreeForm"]["What's 2*2?"]["active"] is True

# Testing whether the correct methods are called
def test_add_mode_invoked(mocker):
    adding_mock_function = mocker.patch("add_mode.AddMode.add_questions")
    menu = Menu(User("Turing"))
    set_keyboard_input(["1", "exit"])
    menu.select_mode()
    menu.invoke_mode()
    adding_mock_function.assert_called_once()
