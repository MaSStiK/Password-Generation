from flask import Flask
import json
from Password import Password

app = Flask(__name__)


@app.route('/password/generation/<length>')
def generate_password(length):
    Password_Generator = Password(length)
    password = Password_Generator.generate()
    response = app.response_class(
        response=json.dumps({
            "app_version": Password_Generator.VERSION,
            "password_length": Password_Generator.length,
            "symbols_count": str(len(Password_Generator.SYMBOLS)),
            "variant": str(Password_Generator.variants),
            "password": password
        }),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
