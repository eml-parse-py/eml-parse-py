from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Message:
    filename = ""

    def message_text(self):
        content = ""
        return content

    def msg_env(self, _from, to, subject, body, part1):
        message = MIMEMultipart()
        message["From"] = _from
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        message.attach(part1)

        return message

    def attach_files(self):
        with open(self.filename, "rb") as attach:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attach.read())
            encoders.encode_base64(part)

            part.add_header("Content-Disposition",
                            f"attachment; filename= {self.filename}")

            return part
