from flask import Flask, request
import json

app = Flask(__name__)
# Это чтоб на сайте правельно отрабатывала кодировка
app.config['JSON_AS_ASCII'] = False


@app.route('/likes')
def likes():

    namesList = []

    data = {

    }
    names = request.args.get('names')
# Всякого рода проверки. На ввод, на символы и длинну.
    if names:
        for i in (list(names.split(","))):
            if i.isalpha() and len(i) <= 10:
                # Добавляю в список и чищу словарь
                namesList.append(i)
                data.clear()

            else:
                data["error"] = True
                data["data"] = None
                data["error_message"] = "*Неверное имя пользователя*"
                print("*Неверное имя пользователя*")
                return data
                data.clear()
                namesList.clear()
# Вывод в консоль и на саит в зависимости от длинны списка имен.
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
            print(f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]}, {namesList[1]} и {namesList[2]} лайкнули это.\"')
        else:
            data["error"] = False
            data["data"] = (f'{namesList[0]}, {namesList[1]} и еще {len(namesList) - 2} человека лайкнули это.')
            data["error_message"] = None
            print (f'{(json.dumps(namesList, ensure_ascii=False))} --> \"{namesList[0]}, {namesList[1]} и еще {len(namesList) - 2} человека лайкнули это.\"')

        namesList.clear()
    else:
        print('[] --> "Это никому не нравиться"')
        return "Ничего не ввели"
    return data



if __name__ == "__main__":
    app.run(debug=True, port=8000)

