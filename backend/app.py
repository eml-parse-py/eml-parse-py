from flask import Flask, request, jsonify
from flask_cors import CORS

from email_functionality.SendMessage import SendMessage
from eml_api import extract_header

import json
import os

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
CORS(app)
eml_file = "message.eml"


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    file = request.files['file'].save(dst=os.path.abspath("message.eml"))
    return ""


@app.route("/fetchmetadata", methods=["GET"])
def header_construct():
    file = "message.eml"
    ex = extract_header.ExtractHeader()
    headers = ex.header_gen(file)
    kp_vals = ex.craft_html(file)
    kp_vals
    return jsonify(headers)


@app.route("/sendemail", methods=["POST"])
def send_email():
    try:
        if request.form.get('text') is None:
            print("Please enter an email... ")
        else:
            SendEmailObj = os.path.abspath(f"email_functionality{os.sep}SendEmailObjAttributes.json")
            with open(SendEmailObj) as file:
                params = json.load(file)
                fromAddr = params["fromAddr"]
                toAddr = request.form.get('text')
                subject = params["subject"]
                text = params["text"]
                attachment = os.path.abspath(f"eml_api{os.sep}AnalysedHeaders.html")
                passwd = params["passwd"]
                snd = SendMessage(fromAddr, toAddr, subject, text, attachment, passwd)
                snd.send_msg()

    except FileExistsError as NoExist:
        print(NoExist)
        ex = extract_header.ExtractHeader()
        ex.craft_html(eml_file)

    return ""


if __name__ == "__main__":
    app.run(debug=True)
