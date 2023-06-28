

class FreeFormQuestion:
    def __init__(self, question, answer) -> None:
        self.question = question
        self.answer = answer

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, question):
        if isinstance(question, str) is not True:
            raise ValueError("Question variable is not a string.")
        self._question = question

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, answer):
        if isinstance(answer, str) is not True:
            raise ValueError("Answer variable is not a string.")
        self._answer = answer