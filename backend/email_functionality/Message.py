import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Message:

    def __init__(self, from_address, to_address, subject, text, attachment):
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject
        self.text = text
        self.attachment = attachment

    def message_body_crafted(self):
        message = MIMEMultipart('alternative')
        message["From"] = self.from_address
        message["To"] = self.to_address
        message["Subject"] = self.subject
        attach = self.attach_files()
        html = f"""
        <html>
        <head></head>
        <body>
        <p>Hi, <br>
      {self.text} 
      <p>
      Many thanks,<br>
      Mark from the Eml Py parse Eml team!
      </p>
        </p>
        </body>
    </html>
        """
        msg_text = MIMEText(self.text, "plain")
        msg_html = MIMEText(html, "html")
        message.attach(msg_text)
        message.attach(msg_html)
        message.attach(attach)
        return message

    def attach_files(self):
        with open(self.attachment, "rb") as attach:
            msg_part = MIMEBase("text", "html")
            msg_part.set_payload(attach.read())
            encoders.encode_base64(msg_part)
            msg_part.add_header("Content-Disposition",
                                f"attachment; filename= {os.path.basename(self.attachment)}")
            return msg_part
