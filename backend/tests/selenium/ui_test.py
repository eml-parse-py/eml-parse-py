from selenium import webdriver
import unittest
from os import sep

PATH = f"C:{sep}Program Files (x86){sep}chromedriver.exe"

baseUrl = "http://localhost:3000"


class TestUploadLogic(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.driver.implicitly_wait(5)

    def test_upload_file(self):
        self.driver.get(baseUrl)
        file_upload = self.driver.find_element_by_xpath('//*[@id="file_upload"]')
        file_upload.send_keys(
            f"C:{sep}Users{sep}markm{sep}Desktop{sep}Programming Projects{sep}eml-parse-py{sep}backend{sep}emails{sep}msg.eml")

        self.assertTrue(
            "Content type / MIME Type: message/rfc822" in self.driver.find_element_by_xpath('//*[@id="mimetype"]').text,
            "Content Type does match up..\n ")

    def test_insert_email_address(self):
        self.driver.get(baseUrl)
        email_address = self.driver.find_element_by_xpath('//*[@id="Email Address"]')
        email_address.send_keys("example@smtpaddress.com")
        self.assertNotEqual(
            "example@smtpaddress.com" in self.driver.find_element_by_xpath('//*[@id="Email Address"]').text,
            "Unexpected SMTP address")

    def test_submitting_uploaded_file(self):
        self.driver.get(baseUrl)
        upload_file_button = self.driver.find_element_by_xpath('//*[@id="file-input"]/form/div[1]/button').click()
        message_output = self.driver.find_element_by_xpath('//*[@id="msg-headers"]')
        assert message_output.text in 'DomainKey-Signature'

    def test_send_the_email_with_attach(self):
        self.driver.get(baseUrl)
        send_message = self.driver.find_element_by_xpath('//*[@id="Email-form"]/button').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
