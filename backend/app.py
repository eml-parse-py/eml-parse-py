import json

from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from flask_cors import cross_origin, CORS
from werkzeug.utils import secure_filename
import os
from eml_api import msg_convert
from eml_api import extract_header
from email_functionality.SendMessage import SendMessage

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

UPLOAD_LOCATION = 'emails'
PERMITTED_EXTS = {'eml', 'msg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_LOCATION


def permitted_file_upload(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in PERMITTED_EXTS


@app.route("/uploadfile", methods=["POST"])
def handle_file_upload():
    if request.files:
        file = request.files['file']

        if file.filename == "":
            print('file must have a name')
            return redirect(request.url)
        if not permitted_file_upload(file.filename):
            print("Disallowed extension")
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('Email file saved')
    return redirect(url_for('header_construct', filename=file.filename))


@app.route("/fetchmetadata/<filename>", methods=["GET"])
@cross_origin(origin='localhost', headers=['Access-Control-Allow-Origin:'])
def header_construct(filename):
    file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
    ex = extract_header.ExtractHeader()
    headers = ex.header_gen(file_path)
    headers
    kp_vals = ex.craft_html(file_path)
    kp_vals
    return jsonify(headers)


@app.route("/sendemail", methods=["POST"])
def send_email():
    try:
        if request.form.get('text') is None:
            print("Please enter an email... ")
        else:
            SendEmailObj = "email_functionality/SendEmailObjAttributes.json"
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
