from flask import Flask, request, jsonify
from flask_cors import CORS
from eml_api import extract_header
from email_functionality import SendEmail
import json

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


@app.route("/sendemail", methods=["POST"])
def send_email():
    try:
        with open(f"email_functionality\\SendEmailObjAttributes.json", "r") as file:
            params = json.load(file)
            fromAddr = params["fromAddr"]
            toAddr = params["toAddr"]
            subject = params["subject"]
            text = params["text"]
            attachment = params["attachment"]
            passwd = params["fromAddr"]

    except FileExistsError as NoExist:
        print(NoExist)
    snd = SendEmail.SendEmail(fromAddr, toAddr, subject, text, attachment, passwd)
    data = request.form
    return ""


if __name__ == "__main__":
    app.run(debug=True)
