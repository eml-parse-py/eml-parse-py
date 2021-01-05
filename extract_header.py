"""
Author: Mark McMoran

Purpose: Parsing SMTP message headers, for display purposes, it could provide 
extensibility for purposes like tracing mail flow of a given message.

"""
from email.parser import BytesParser
from email.policy import default


class ExtractHeader:

    _crlf = r'\r\n'
    _lf = r'\n'

    def open_msg_file(self, msg):
        with open(msg, 'rb') as file:
            headers = BytesParser(policy=default).parse(file)
        return headers

    def msg_header_from(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('from')
        return _opened
