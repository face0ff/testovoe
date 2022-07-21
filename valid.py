from flask import Flask, request
import validation

app = Flask(__name__)


@app.route('/likes')
def get_likes():
    total = request.args.get('names')

    return validation.validation_names(total)


if __name__ == '__main__':
    app.run()
22222222222222222222222222222222222222222222222222222222222222222222222222222222
from flask import Flask, request

app = Flask(__name__)

data = {}
error_message = "*Неверное имя пользователя*"
namesList = []


@app.route('/')
def index():
    return "hello"


@app.route('/likes')
def likes():
    names = request.args.get('names')
    listOfNames = (list(names.split(",")))

    if names:
        for i in listOfNames:
            if i.isalpha() and len(i) <= 10:
                if len(listOfNames) == 1:
                    data["error"] = False
                    data["data"] = f'{listOfNames[0]} лайкнул это.'
                    data["error_message"] = None
                    namesList.append(i)
                    # print(f'{listOfNames} --> \"{listOfNames[0]} лайкнул это.\"')
                elif len(listOfNames) == 2:
                    data["error"] = False
                    data["data"] = (f'{listOfNames[0]} и {listOfNames[1]} лайкнули это.')
                    data["error_message"] = None
                    namesList.append(i)
                    # print(f'{listOfNames} --> \"{listOfNames[0]} и {listOfNames[1]} лайкнули это.\"')
                elif len(listOfNames) == 3:
                    data["error"] = False
                    data["data"] = (f'{listOfNames[0]}, {listOfNames[1]} и {listOfNames[2]} лайкнули это.')
                    data["error_message"] = None
                    namesList.append(i)
                    # print(f'{listOfNames} --> \"{listOfNames[0]}, {listOfNames[1]} и {listOfNames[2]} лайкнули это.\"')

                else:
                    data["error"] = False
                    data["data"] = (
                        f'{listOfNames[0]}, {listOfNames[1]} и еще {len(listOfNames) - 2} человека лайкнули это.')
                    data["error_message"] = None
                    namesList.append(i)
                    # print(f'{listOfNames} --> \"{listOfNames[0]}, {listOfNames[1]} и еще {len(listOfNames) - 2} человека лайкнули это.\"')
            else:
                data["error"] = True
                data["data"] = None
                data["error_message"] = error_message



    else:
        # Надо бы дописать
        print('[] --> "Это никому не нравиться"')
        return "Нечего не ввели"

    print(namesList)
    return data


if __name__ == "__main__":
    app.run(debug=True)