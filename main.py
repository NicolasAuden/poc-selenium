# Import unittest module for creating unit tests
import unittest
# Import time module to implement
import time

import sys

# Import webdriver module
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import remote_connection
from selenium.webdriver.support.ui import Select

from selenium.webdriver import DesiredCapabilities

from pyunitreport import HTMLTestRunner

class RancherFirefoxTestCase(unittest.TestCase):

    def setUp(self):
        # Define the FireFox driver
        remote_cnx = remote_connection.RemoteConnection(
            remote_server_addr='http://selenium-hub.fr:80/wd/hub', resolve_ip=False)
        self.driver = webdriver.Remote(
            command_executor=remote_cnx,
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
            )

        # Close the browser when the test is done
        self.addCleanup(self.driver.quit)

    def testRancherPage(self):
        # Go to Rancher
        self.driver.get('https://rancher.devops.fr')

        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page (Rancher takes some time to load)
        time.sleep(10)

        # A test to ensure the page has keyword "Rancher" in the page title
        self.assertIn("Rancher", self.driver.title)

        # A test to ensure the page is up and contain the string "Welcome to Rancher"
        self.assertIn("Welcome to Rancher", self.driver.page_source)
        
        # Take a screenshot of the results
        self.driver.save_screenshot('./screenshot.png')

# Boilerplate code to start the unit tests
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='report'))
