"""
Author: Mark McMoran

Purpose: Parsing SMTP message headers, for display purposes,  providing
extensibility like; tracing mail flow of a message.

"""
from email.parser import BytesParser
from email.policy import default


class ExtractHeader:

    def open_msg_file(self, msg):
        with open(msg, 'rb') as file:
            headers = BytesParser(policy=default).parse(file)
        return headers

    def ret_header(self, msg, val):
        _opened = self.open_msg_file(msg)
        _opened.get(val)
        return _opened

    def header_gen(self, msg):
        _opened = self.open_msg_file(msg)
        headers = _opened.items()
        return headers
