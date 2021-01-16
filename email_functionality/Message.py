from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Message:

    def __init__(self, _from, to, subject, body, attachment):
        self._from_ = _from
        self._to = to
        self._subject = subject
        self._body = body
        self._attachment = attachment

    def msg_builder(self):
        message = MIMEMultipart()
        message["From"] = self._from_
        message["To"] = self._to
        message["Subject"] = self._subject
        attach = self.attach_files()
        message.attach(MIMEText(self._body, "plain"))
        message.attach(attach)
        return message

    def attach_files(self):
        with open(self._attachment, "rb") as attach:
            part = MIMEBase("text", "html")
            part.set_payload(attach.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            f"attachment; filename= {self._attachment}")
            return part
