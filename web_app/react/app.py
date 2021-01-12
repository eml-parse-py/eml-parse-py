from flask import Flask, request, jsonify
from flask_cors import CORS
from eml_api import extract_header

app = Flask(__name__, static_folder='./app/static/parse_py_ui/build', static_url_path='/')
CORS(app)


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    file = request.files['file'].save(dst="message.eml")
    return ""


@app.route("/fetchmetadata", methods=["GET"])
def header_construct():
    file = "message.eml"
    ex = extract_header.ExtractHeader()
    headers = ex.header_gen(file)

    return jsonify(headers)


if __name__ == "__main__":
    app.run(debug=True)
