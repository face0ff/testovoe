import json


def allData(namesList: list) -> dict:
    data = {
    }
    if len(namesList) == 1:
        data["error"] = False
        data["data"] = (f'{namesList[0]} лайкнул(а) это.')
        data["error_message"] = None
        print(f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]} лайкнул(а) это.\"')
    elif len(namesList) == 2:
        data["error"] = False
        data["data"] = (f'{namesList[0]} и {namesList[1]} лайкнули это.')
        data["error_message"] = None
        print(f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]} и {namesList[1]} лайкнули это.\"')
    elif len(namesList) == 3:
        data["error"] = False
        data["data"] = (f'{namesList[0]}, {namesList[1]} и {namesList[2]} лайкнули это.')
        data["error_message"] = None
        print(
            f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]}, {namesList[1]} и {namesList[2]} лайкнули это.\"')
    else:
        data["error"] = False
        data["data"] = (f'{namesList[0]}, {namesList[1]} и еще {len(namesList) - 2} человека лайкнули это.')
        data["error_message"] = None
        print(
            f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]}, {namesList[1]} и еще {len(namesList) - 2} человека лайкнули это.\"')

    return data
