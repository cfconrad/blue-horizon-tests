from selenium import webdriver
import configparser
from pageobjects import WelcomePage
from pageobjects import SideBar
from pageobjects import Cluster
import pytest


def test_simpleFlow():
    config = configparser.RawConfigParser()
    config.read('test.properties')
    driver = webdriver.Firefox(service_log_path='/tmp/geckodriver.log')
    driver.get("http://{}:{}@{}/".format(config.get('aks', 'username'),
                                         config.get('aks', 'pw'), config.get('aks', 'ip')))
    driver.maximize_window()
    SideBar(driver).page_displayed()
    WelcomePage(driver).go_to_cluster()
    cluster = Cluster(driver)
    cluster.page_displayed()
    cluster.go_to_variables()
