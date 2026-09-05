import random


def generate_data(n, x):
    return [random.randint(1, x) for _ in range(n)]