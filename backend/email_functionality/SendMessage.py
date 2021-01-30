import smtplib
import ssl
import traceback

from email_functionality.Message import Message


class SendMessage(Message):

    def __init__(self, fromAddr, toAddr, subject, text, attachment, passwd):
        super().__init__(fromAddr, toAddr, subject, text, attachment)
        self.passwd = passwd

    smtp_server = "smtp.gmail.com"

    def send_msg(self):
        port = 587
        context = ssl.create_default_context()

        try:
            svr = smtplib.SMTP(self.smtp_server, port)
            svr.ehlo()
            svr.starttls(context=context)
            svr.ehlo()
            svr.set_debuglevel(2)
            svr.login(self.fromAddr, self.passwd)
            svr.sendmail(
                f"{self.fromAddr}", f"{self.toAddr}",
                self.msg_builder().as_string()
            )

        except Exception as ex:
            print(ex)
            traceback.print_exc()
        finally:
            svr.quit()
