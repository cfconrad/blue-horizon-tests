from selenium.webdriver.common.action_chains import ActionChains


class PageObject:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)


class WelcomePage(PageObject):

    def go_to_cluster(self):
        start_setup = self.get_element(
            '//main[@id="content"]//a[@href="/welcome/simple"]')
        start_setup.click()


class SideBar(PageObject):

    def page_displayed(self):
        self.get_element('//nav[@id="sidebar"]')
        self.get_element('//nav/div/a[@href="/welcome"]')
        self.get_element('//nav/div/a[@href="/variables"]')
        self.get_element('//nav/div/a[@href="/plan"]')
        self.get_element('//nav/div/a[@href="/deploy"]')
        self.get_element('//nav/div/a[@href="/wrapup"]')


class Cluster(PageObject):

    def page_displayed(self):
        instance_type_xpath_pattern = '//div[@class="instance-type-box"]/small[contains(text(),"{}")]'
        self.get_element(instance_type_xpath_pattern.format("Standard_DS3_v2"))
        self.get_element(instance_type_xpath_pattern.format("Standard_DS4_v2"))
        self.get_element(instance_type_xpath_pattern.format("Standard_F4s"))
        self.get_element(instance_type_xpath_pattern.format("Standard_F8s"))
        self.get_element(instance_type_xpath_pattern.format("Standard_A4_v2"))
        self.get_element(instance_type_xpath_pattern.format("Standard_A8_v2"))
        instance_cnt = self.get_element('//input[@id="count-display"]')
        assert instance_cnt.get_attribute('value') == "3"

    def go_to_variables(self):
        btn_variables = self.get_element('//button[@id="submit-cluster"]')
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", btn_variables)
        btn_variables.click()
