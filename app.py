import extract_header


class App:

    def main(self):
        pass

    def callExtraction(self, smtp_msg):
        extr = extract_header.ExtractHeader()

        extr.open_msg(smtp_msg)


if __name__ == "__main__":
    App()
