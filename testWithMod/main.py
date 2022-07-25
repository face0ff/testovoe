from flask import Flask, request

import printAll
import valid

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/likes')
def likes():
    data = {
    }
    names = request.args.get('names')
    if names:
        namesList = valid.valid_name(names)
        if namesList:
            data = printAll.allData(namesList)
            return data
        else:
            data["error"] = True
            data["data"] = None
            data["error_message"] = "*Неверное имя пользователя*"
            print("*Неверное имя пользователя*")
            return data

    else:
        print('[] --> "Это никому не нравиться"')
        return "Ничего не ввели"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
