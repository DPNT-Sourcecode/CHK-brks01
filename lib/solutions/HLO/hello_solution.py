

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    if not friend_name:
        return "None"
    return f"Hello, {friend_name}!"
