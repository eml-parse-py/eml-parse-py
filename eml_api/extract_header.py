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

    def msg_header_to(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('to')
        return _opened

    def msg_header_subject(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('subject')
        return _opened

    def msg_header_reply_to(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('reply-to')
        return _opened

    def msg_header_msg_id(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('message-id')
        return _opened

    def msg_header_date(self, msg):
        _opened = self.open_msg_file(msg)
        _opened.get('date')
        return _opened

