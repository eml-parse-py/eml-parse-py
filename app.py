#!/usr/bin/env python
import argparse
import pathlib

import extract_header


def main():
    _parsr = argparse.ArgumentParser(description="An SMTP message analysis application", epilog="Perfect tool for "
                                                                                                "reviewing the path "
                                                                                                "taken by a mail in a "
                                                                                                "pinch! ")
    _parsr.add_argument("--file", type=pathlib.Path,
                        help="This prints the email file including it's multipart values. ")
    _parsr.add_argument("--hfrom", type=pathlib.Path)

    args = _parsr.parse_args()
    extr = extract_header.ExtractHeader()

    if args.hfrom:
        extr.msg_header_from(args.hfrom)
    elif args.file:
        extr.open_msg_file(args.file)
    else:
        print("Invalid option or no option selected...\n\n " + "Valid options include: \n  --hfrom \n  --file " )


if __name__ == '__main__':
    main()
