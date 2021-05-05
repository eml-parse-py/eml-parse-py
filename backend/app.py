import json
import os
from flask import Flask, request, redirect, url_for
from flask_cors import cross_origin, CORS
from werkzeug.utils import secure_filename

from eml_api import extract_header
from email_functionality.SendMessage import SendMessage
from eml_api import handle_msg_file

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

UPLOAD_LOCATION = 'emails'
PERMITTED_EXTENSIONS = {'eml', 'msg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_LOCATION


def permitted_file_upload(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in PERMITTED_EXTENSIONS


@app.route("/uploadfile", methods=["POST"])
def handle_email_upload():
    if request.files:
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url, 400)
        if not permitted_file_upload(file.filename):
            return redirect(request.url, 400)
        else:
            upload_location_config = app.config['UPLOAD_FOLDER']
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_location_config, filename))
            file_path = f"{upload_location_config}/{filename}"
            extract_header_object = extract_header.ExtractHeader(file_path)
            save_message_as_json = extract_header_object.handle_saved_message_data()
            json_filename = extract_header_object.timestamped_file_format()
            generate_html_attachment = extract_header_object.create_html_attachment()
        return redirect(url_for('get_json_message_data', json_message_data=json_filename), 302)


@app.route("/fetchmetadata/<json_message_data>", methods=["GET"])
@cross_origin(origin='localhost', headers=['Access-Control-Allow-Origin'])
def get_json_message_data(json_message_data):
    with open(json_message_data) as file:
        json_data = json.load(file)
    return json_data, 200


@app.route("/sendemail", methods=["POST"])
def send_email():
    if request.form.get('text') is None:
        print("Enter a valid SMTP address.. ")
    else:
        EmailAttributes = "email_functionality/SendEmailObjAttributes.json"
        try:
            with open(EmailAttributes) as file:
                params = json.load(file)
                from_address = params["fromAddr"]
                to_address = request.form.get('text')
                subject = params["subject"]
                text = params["text"]
                attachment = "eml_api/AnalysedHeaders.html"
                password = params["passwd"]
                send_message_object = SendMessage(from_address, to_address, subject, text, attachment, password)
                send_message_object.send_smtp_message()
        except FileExistsError as NonExistentFile:
            print(NonExistentFile)
    return to_address


if __name__ == "__main__":
    app.run(debug=True)
