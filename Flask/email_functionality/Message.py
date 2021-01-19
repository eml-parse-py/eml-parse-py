from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Message:

    def __init__(self, fromAddr, toAddr, subject, text, attachment):
        self.fromAddr = fromAddr
        self.toAddr = toAddr
        self.subject = subject
        self.text = text
        self.attachment = attachment

    def msg_builder(self):
        message = MIMEMultipart()
        message["From"] = self.fromAddr
        message["To"] = self.toAddr
        message["Subject"] = self.subject
        attach = self.attach_files()
        message.attach(MIMEText(self.text, "plain"))
        message.attach(attach)
        return message

    def attach_files(self):
        with open(self.attachment, "rb") as attach:
            part = MIMEBase("text", "html")
            part.set_payload(attach.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            f"attachment; filename= {self.attachment}")
            return part
