import json


def load_notions() -> dict:
    with open("notes/notions.json", "r") as read_file:
        return json.loads(read_file.read())


# def get_record(data: dict):
#     data
