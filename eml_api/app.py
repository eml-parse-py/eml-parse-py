#!/usr/bin/env python
import argparse
import pathlib

import extract_header
import create_html


def main():
    _parsr = argparse.ArgumentParser(description="An SMTP message analysis application", epilog="Perfect tool for "
                                                                                                "reviewing the path "
                                                                                                "taken by a mail in a "
                                                                                                "pinch! ")
    _parsr.add_argument("--file", type=pathlib.Path,
                        help="This prints the email file including it's multipart values. ")
    _parsr.add_argument("--hfrom", type=pathlib.Path)
    _parsr.add_argument("--hto", type=pathlib.Path)
    _parsr.add_argument("--hsubject", type=pathlib.Path)
    _parsr.add_argument("--hreply-to", type=pathlib.Path)
    _parsr.add_argument("--hmsg-id", type=pathlib.Path)
    _parsr.add_argument("--hdate", type=pathlib.Path)
    _parsr.add_argument("--makehtml", type=pathlib.Path)

    args = _parsr.parse_args()
    extr = extract_header.ExtractHeader()

    htm = create_html.CreateHtml()

    headers = ['from', 'to', 'subject', 'reply-to', 'message-id', 'date']

    if args.hfrom:
        extr.ret_header(args.file, headers[0])
    elif args.file:
        extr.ret_header(args.file, headers[1])
    elif args.hto:
        extr.ret_header(args.file, headers[2])
    elif args.hsubject:
        extr.ret_header(args.file, headers[3])
    elif args.hreplyto:
        extr.ret_header(args.file, headers[4])
    elif args.hmsgid:
        extr.ret_header(args.file, headers[5])
    elif args.hdate:
        extr.ret_header(args.file, headers[6])
    elif args.makehtml:
        extr.htm
    else:
        print("Invalid option or no option selected... " + "\n\nValid options include:"
                                                           "\n  Print the header from address --hfrom"
                                                           "\n Print the header to address --hto "
                                                           "\n Print the subject of the msg --hsubject "
                                                           "\n Print the Reply-to address of the msg --hreply-to"
                                                           "\n Print the Msg ID of the Msg --hmsg-id  "
                                                           "\n Print the date of the msg: --hdate"
                                                           "\n Print the full Msg out: --file "
                                                           "\n Create HTML file comprised of the attributes found in the eml : --makehtml")


if __name__ == '__main__':
    main()
