import json

from flask import Flask, request, redirect, url_for, send_from_directory
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os
from ..eml_api import msg_convert
from ..eml_api import extract_header
from backend.email_functionality.SendMessage import SendMessage

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')

UPLOAD_LOCATION = 'emails'
PERMITTED_EXTS = {'eml', 'msg'}


def permitted_file_upload(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in PERMITTED_EXTS


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    file = request.files['file']
    filetype = file.filename.rsplit('.', 1)[1]

    if file and permitted_file_upload(file.filename):
        filename = secure_filename(file)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if filetype == 'msg':
            msgcnvt = msg_convert.MsgConvert()
            msgcnvt.msg_to_eml(file)

    return redirect(url_for('header_construct', filename=file.filename))


@app.route("/fetchmetadata/<filename>", methods=["GET"])
@cross_origin(origin='localhost', headers=['Access-Control-Allow-Origin:'])
def header_construct(filename):
    path = f'emails/{filename}'
    ex = extract_header.ExtractHeader()
    headers = ex.header_gen(path)
    headers
    kp_vals = ex.craft_html(path)
    kp_vals
    return send_from_directory(directory='emails/', filename=filename)


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
                attachment = "eml_api/AnalysedHeaders.html"
                passwd = params["passwd"]
                snd = SendMessage(fromAddr, toAddr, subject, text, attachment, passwd)
                snd.send_msg()
    except FileExistsError as NoExist:
        print(NoExist)

    return ""


if __name__ == "__main__":
    app.run(debug=True)
