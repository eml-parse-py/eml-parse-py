from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Message:

    def __init__(self, _from, to, subject, body, attachment):
        self.__from = _from
        self._to = to
        self._subject = subject
        self._body = body
        self._attachment = attachment

    def message_text(self, body):
        content = body
        return content

    def msg_builder(self, _from, to, subject, body, part1):
        message = MIMEMultipart()
        message["From"] = _from
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        message.attach(part1)

        return message

    def attach_files(self, filename):
        with open(filename, "rb") as attach:
            part = MIMEBase("text", "html")
            part.set_payload(attach.read())
            encoders.encode_base64(part)

            part.add_header("Content-Disposition",
                            f"attachment; filename= {filename}")

            return part
