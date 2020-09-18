from flask import Flask, request
import logging


logging.basicConfig(filename='main_app.log')
# logger = logging.getLogger('main_app')


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
        # logger.error(e)
        print(e)

    return str(c)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
