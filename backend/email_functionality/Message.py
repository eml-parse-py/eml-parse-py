import os
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
        message = MIMEMultipart('alternative')
        message["From"] = self.fromAddr
        message["To"] = self.toAddr
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
        txt = MIMEText(self.text, "plain")
        html_v = MIMEText(html, "html")
        message.attach(txt)
        message.attach(html_v)
        message.attach(attach)
        return message

    def attach_files(self):
        with open(self.attachment, "rb") as attach:
            part = MIMEBase("text", "html")
            part.set_payload(attach.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            f"attachment; filename= {os.path.basename(self.attachment)}")
            return part
