import SendEmail
import os


def main():
    send_eml = os.environ['sending_eml']
    rcpt_eml = os.environ['rcpt_eml']
    passwd = os.environ['passwd']
    subj = "Testing..."
    body = "blah"

    snd = SendEmail.SendEmail(send_eml, rcpt_eml, subj, body, passwd)

    snd.send_msg()


if __name__ == "__main__":
    main()
