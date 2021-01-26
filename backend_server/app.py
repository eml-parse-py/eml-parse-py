from flask import Flask, request, jsonify
from flask_cors import CORS
from eml_api import extract_header
from email_functionality import SendMessage
import json
import os

app = Flask(__name__, static_folder='./app/static/parse_py_ui/build', static_url_path='/')
CORS(app)


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    file = request.files['file'].save(dst="../web_app/react/message.eml")
    return ""


@app.route("/fetchmetadata", methods=["GET"])
def header_construct():
    file = "../web_app/react/message.eml"
    ex = extract_header.ExtractHeader()
    headers = ex.header_gen(file)
    return jsonify(headers)


@app.route("/sendemail", methods=["POST"])
def send_email():
    try:
        SendEmailObj = os.path.abspath(f"email_functionality{os.sep}SendEmailObjAttributes.json")
        with open(SendEmailObj) as file:
            params = json.load(file)
            fromAddr = params["fromAddr"]
            toAddr = request.form.get('text')
            subject = params["subject"]
            text = params["text"]
            attachment = os.path.abspath(f"email_functionality{os.sep}test.html")
            passwd = params["passwd"]
            snd = SendMessage(fromAddr, toAddr, subject, text, attachment, passwd)
            snd.send_msg()

    except FileExistsError as NoExist:
        print(NoExist)

    return ""


if __name__ == "__main__":
    app.run(debug=True)
