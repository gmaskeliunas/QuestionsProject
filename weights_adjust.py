
class Weights:
    def __init__(self) -> None:
        pass

    @staticmethod
    def adjust_weights(data, username, random_key, questions):
        # Here I adjust weights for questions to be randomly chosen. I increase or decrease the chance to be shown
        # by a value of 0.1
        accuracy = data[username][questions][random_key]['accuracy']
        weight = data[username][questions][random_key]['weight']
        max_change = 0.1
        if accuracy < 0.5:
            change = max_change
        else:
            change = -max_change
        weight += change
        # If the weight of the question would be below the incremential value, I assign it to it so
        # it never goes to zero and can always be printed out with a slight chance
        if weight < max_change:
            weight = max_change

        data[username][questions][random_key]['weight'] = round(weight, 1)