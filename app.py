from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def divide():
    c = 'nothing'

    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        c = a/b
    # except ZeroDivisionError as e:
    #     return 'B can not be 0'
    except Exception as e:
        print(e)

    return str(c)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
