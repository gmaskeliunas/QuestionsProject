

class User:
    def __init__(self, username) -> None:
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            raise ValueError("Username is not str type.")
        self._username = username
