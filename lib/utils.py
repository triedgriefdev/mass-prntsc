import random
import string


def random_string(length: int):
    return "".join(random.choice(list(string.ascii_lowercase)) for _ in range(length))
