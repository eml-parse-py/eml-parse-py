import smtplib
import ssl
import traceback


from Message import Message


class SendEmail(Message):

    def __init__(self, _from, to, subject, body, passwd: str):
        super().__init__(self, _from, to, subject, body)
        if passwd is None:
            passwd = "No password specified... \n"
        else:
            self.passwd = passwd

    smtp_server = "smtp.gmail.com"
    port = 587

    def send_msg(self):
        context = ssl.create_default_context()
        _from = self._from_
        _passwd = self.passwd
        try:
            svr = smtplib.SMTP(self.smtp_server)
            svr.ehlo()
            svr.starttls(context=context)
            svr.ehlo()
            svr.set_debuglevel(2)
            svr.login(_from, _passwd)
            svr.sendmail(
                f"{self._from_}", f"{self._to}", f"{self._body}"
            )
            print("msg sent... ")
        except Exception as ex:
            print(ex)
            traceback.print_exc()
        finally:
            svr.quit()
