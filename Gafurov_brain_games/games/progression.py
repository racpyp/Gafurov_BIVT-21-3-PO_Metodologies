import random

def generate_question():
    start = random.randint(1, 10)
    ratio = random.randint(2, 10)
    length = random.randint(5, 10)
    place_of_miss = random.randint(0, length - 1)

    progression = [start * (ratio ** i) for i in range(length)]

    answer = progression[place_of_miss]
    progression[place_of_miss] = '..'
    question_format = '{} ' * (length-1) + '{}'
    question = question_format.format(*progression)
    return question, answer