"""
Author:
Mark McMoran

Purpose:
Parsing SMTP messages for tracing purposes.

Features:
- HTML generation of email data
- Parses .EML & .MSG files by injecting their headers into JSON files respective to their name/(s).

"""
import jinja2
from email.parser import BytesParser
from email.policy import default
import json


class ExtractHeader:

    def __init__(self, msg_file_path):
        self.msg_file_path = msg_file_path
        self.msg_extension = msg_file_path.rsplit('.', 1)[1].lower()
        try:
            self.message_file_object = "MsOxMessage(msg_file_path)"
        except:
            print("This file wasn't a .MSG file.")

    def parse_msg_upload(self):

        return ""

    def parse_eml_upload(self):
        with open(self.msg_file_path, "rb") as file:
            headers = BytesParser(policy=default).parse(file)
            list_headers = headers.items()
            json_output = json.dumps(list_headers)
        return json_output

    def get_message_data_json(self):
        if self.msg_extension == "eml":
            return self.parse_eml_upload()
        else:
            return self.parse_msg_upload()

    def handle_saved_message_data(self):
        if self.msg_extension == "eml":
            eml_json = self.parse_eml_upload()
            self.save_message_json(eml_json)
        else:
            # msg_json = self.parse_msg_upload()
            # self.save_message_json(msg_json)
            pass

    def timestamped_file_format(self):
        import datetime
        date_time = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        return f"{date_time}.json"

    def save_message_json(self, json_data):
        filename = self.timestamped_file_format()
        print(f"{filename} is the name of this file..\n\n\n\n")
        with open(filename, "w") as file:
            json.dump(json_data, file)

    def create_html_attachment(self):
        """
        Purpose:
        Attaches onto email that end user has analysed,
        generates the output based off of JSON data generated
        from message.
        """
        directory_of_script = 'eml_api/'
        jinja_env_variable = jinja2.Environment(loader=jinja2.FileSystemLoader(f"{directory_of_script}templates"))
        template_file = jinja_env_variable.get_template('message_details.html')
        jinja_dictionary = {
            'message_headers': self.get_message_data_json()
        }
        craft_html = template_file.render(jinja_dictionary)
        with open(f"{directory_of_script}AnalysedHeaders.html", "w") as file:
            file.write(craft_html)
