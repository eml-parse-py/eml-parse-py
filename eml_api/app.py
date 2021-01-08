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

    if args.hfrom:
        extr.msg_header_from(args.hfrom)
    elif args.file:
        extr.open_msg_file(args.file)
    elif args.hto:
        extr.msg_header_to(args.hto)
    elif args.hsubject:
        extr.msg_header_subject(args.hsubject)
    elif args.hreplyto:
        extr.msg_header_reply_to(args.hreplyto)
    elif args.hmsgid:
        extr.msg_header_msg_id(args.hmsgid)
    elif args.hdate:
        extr.msg_header_date(args.hdate)
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
