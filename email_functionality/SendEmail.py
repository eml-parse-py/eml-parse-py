from Message import Message
import smtplib


class SendEmail(Message):

    def __init__(self, _from, to, subject, body, attachment):
        Message.__init__(self, _from, to, subject, body, attachment)

    def send_msg(self):
        with smtplib.SMTP("server", 25) as server:
            server.login("login", "password")
            server.sendmail(
                self._from, self._to, self.body
            )
        print('Msg has been sent!\n')

