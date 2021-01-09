from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__, static_folder='./app/static/parse_py_ui/build', static_url_path='/')
CORS(app)


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    file = request.form.to_dict()
    for value in file.values():
        file = value
    return f"{file}"


if __name__ == "__main__":
    app.run(debug=True)
