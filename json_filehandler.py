import json


def Read_json(f_name: str = 'src.JSON') -> dict:
    with open(f_name, 'r') as f:
        return json.load(f)


def gib(_list: str) -> list[dict] | None:
    data = Read_json()
    if len(data) > 0:
        return data[_list.lower()]
    else:
        return None


def Search_member(search_val: str, search_field: str) -> dict | None:
    data = gib('members')
    found = False

    for member in data:
        if search_val.lower() in member[search_field].lower():
            print(member)
            return member

    if not found:
        return None


def Search_department(dep_name: str) -> list[dict] | None:
    data = gib('members')

    output = []
    for member in data:
        if member['department'].lower() == dep_name.lower():
            output.append(member)

    if len(output) <= 0:
        return None
    else:
        return output
