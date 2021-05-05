import smtplib
import ssl
import traceback

from .Message import Message


class SendMessage(Message):

    def __init__(self, from_address, to_address, subject, text, attachment, passwd):
        super().__init__(from_address, to_address, subject, text, attachment)
        self.passwd = passwd

    smtp_server = "smtp.gmail.com"

    def send_smtp_message(self):
        port = 587
        context = ssl.create_default_context()

        try:
            smtp_conversation = smtplib.SMTP(self.smtp_server, port)
            smtp_conversation.ehlo()
            smtp_conversation.starttls(context=context)
            smtp_conversation.ehlo()
            smtp_conversation.set_debuglevel(2)
            smtp_conversation.login(self.from_address, self.passwd)
            smtp_conversation.sendmail(
                self.from_address, self.to_address,
                self.message_body_crafted().as_string()
            )

        except Exception as ex:
            print(ex)
            traceback.print_exc()
        finally:
            smtp_conversation.quit()
