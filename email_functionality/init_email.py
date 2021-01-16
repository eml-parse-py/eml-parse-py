import SendEmail


def main():
    fromAddr = "email"
    toAddr = "email
    passwd = "password"
    subject = "Testing..."
    attachment = "test.html"
    text = "blah"

    snd = SendEmail.SendEmail(fromAddr, toAddr, subject, text, attachment, passwd)

    snd.send_msg()


if __name__ == "__main__":
    main()
