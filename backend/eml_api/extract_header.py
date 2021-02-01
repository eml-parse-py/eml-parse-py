"""
Author: Mark McMoran

Purpose: Parsing SMTP message headers, for display purposes,  providing
extensibility like; tracing mail flow of a message, this is possible through generation of a HTML file.
"""
from email.parser import BytesParser
from email.policy import default
import jinja2
from pathlib import Path


class ExtractHeader:

    def open_msg_file(self, msg):
        with open(msg, 'rb') as file:
            headers = BytesParser(policy=default).parse(file)
        return headers

    def ret_header(self, msg, val):
        _opened = self.open_msg_file(msg)
        _opened.get(val)
        return _opened

    def header_gen(self, msg):
        _opened = self.open_msg_file(msg)
        headers = _opened.items()
        return headers

    def craft_html(self, msg):
        x = Path("C:/Users/markm/Desktop/Programming Projects/eml-parse-py/backend/eml_api/templates")
        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(x))
        template = jinja_env.get_template('message_details.html')
        html_attrs = self.header_gen(msg)
        jin_pass_thru = {
            'msg_headers': html_attrs
        }
        crafted_html = template.render(jin_pass_thru)
        with open("eml_api/AnalysedHeaders.html", "w") as f:
            f.write(crafted_html)
