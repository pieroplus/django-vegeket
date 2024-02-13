from django.utils.crypto import get_random_string

def get_random_str(num: int):
    return get_random_string(num)