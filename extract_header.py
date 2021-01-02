from email.parser import BytesParser
from email.policy import default

"""
Author: Mark McMoran

Purpose: Parsing SMTP message headers, for display purposes, it could provide 
extensibility for purposes like tracing mail flow of a given message.

"""


class ExtractHeader:
    """

    Global Vars...

    """
    _crlf = r'\r\n'
    _lf = r'\n'

    def open_msg(msgfile):
        with open(msgfile, 'rb') as msg:
            headers = BytesParser(policy=default).parse(msg)
        return headers

    def msg_header_from(self):
        pass

