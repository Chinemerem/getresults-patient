import time

from getresults.tests.base_selenium_test import BaseSeleniumTest


class SeleniumTest(BaseSeleniumTest):

    def navigate_to_admin_getresults_patient(self):
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Getresults_Patient', body.text)
        self.browser.find_element_by_link_text('Getresults_Patient').click()

    def navigate_to_admin_patient_patient(self):
        self.navigate_to_admin()
        self.login()
        self.navigate_to_admin_getresults_patient()
        time.sleep(2)
        element = self.browser.find_element_by_link_text('Patients')
        element.click()
