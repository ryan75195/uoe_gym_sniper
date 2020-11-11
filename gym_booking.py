from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

def sleep(seconds):
    start = time.time()
    # print(start)
    while True:
     print(time.time() - start > seconds)
     print(seconds - (time.time() - start))
     if time.time() - start > seconds:
         break

def book(time, username, password):
    driver = webdriver.Firefox()

    startURL = "https://www.sport.ed.ac.uk/online-booking/"
    driver.get(startURL)
    sleep(2)
    driver.find_element_by_css_selector(
        "html body div#Container.page-container div#CentralRegion.main div#RColumn.main-navigation div#logindisplay div.unauthenticatedLogonControl div a").click()
    sleep(2)
    driver.find_element_by_css_selector(
        f"html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div#LogOnWrapper.activeAreaWrapper div#LogOn.activeArea div.inputForm form div fieldset p input#UserName").send_keys(
        username)
    sleep(2)
    driver.find_element_by_css_selector(
        f"html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div#LogOnWrapper.activeAreaWrapper div#LogOn.activeArea div.inputForm form div fieldset p input#Password").send_keys(
        password)
    sleep(2)
    driver.find_element_by_css_selector(
        ".inputForm > form:nth-child(1) > div:nth-child(1) > fieldset:nth-child(1) > p:nth-child(5) > input:nth-child(1)").click()
    sleep(2)
    Select(driver.find_element_by_name("SiteID")).select_by_visible_text('Pleasance Sports Centre')
    sleep(2)
    # driver.find_element_by_css_selector(
        # "html body div#Container.page-container div#CentralRegion.main div.main-subcontent div.subcontent-unit-border-blue div#SearchCriteria.NormalStateSearch div#SearchBoxContent form.CriteriaDropDowns fieldset div#SearchDropdowns p#ActivitySelection select#Activity").click()
    sleep(2)
    Select(driver.find_element_by_name("Activity")).select_by_visible_text('Gym Access')
    sleep(2)
    driver.find_element_by_css_selector(
        "html body div#Container.page-container div#CentralRegion.main div.main-subcontent div.subcontent-unit-border-blue div#SearchCriteria.NormalStateSearch div#SearchBoxContent form.CriteriaDropDowns fieldset div#SearchDropdowns p#DateSelection input#SearchDate.hasDatepicker").click()
    sleep(2)
    selectDate(driver)
    sleep(2)

    sleep(2)
    driver.find_element_by_css_selector("html body div#Container.page-container div#CentralRegion.main div.main-subcontent div.subcontent-unit-border-blue div#SearchCriteria.NormalStateSearch div#SearchBoxContent form.CriteriaDropDowns fieldset div#SearchDropdowns div#SearchCriteriaFooter div#SearchButtonDiv input.NavigationButton").click()
    sleep(5)
    table = driver.find_element_by_css_selector("html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div#SearchResultsWrapper.activeAreaWrapper div#SearchResults.activeArea div#activeAreaMain div#accordion.ui-accordion.ui-widget.ui-helper-reset.ui-accordion-icons div.SiteResults.ui-accordion-content.ui-helper-reset.ui-widget-content.ui-corner-bottom.ui-accordion-content-active table.ActivitySearchResults.sortable")
    sleep(2)
    table.find_elements_by_xpath(f'//*[text()="{time}"]')[0].find_elements_by_xpath("./..")[0].find_elements_by_xpath("//*[contains(@id,'basketControl')]")[0].click()
    sleep(2)
    driver.find_element_by_css_selector("html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div#BasketDetailWrapper.activeAreaWrapper div#BasketDetail.activeArea div#activeAreaMain div#CheckoutSection div.hiddenCheckoutForm form input#TermsAccepted").click()
    sleep(2)
    driver.find_element_by_css_selector("html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div#BasketDetailWrapper.activeAreaWrapper div#BasketDetail.activeArea div#activeAreaMain div#CheckoutSection div.hiddenCheckoutForm form p.checkoutButtonParagraph input#CheckoutSubmit.button").click()
    sleep(2)
    driver.find_element_by_css_selector("html body div#Container.page-container div#CentralRegion.main div.main-content div.main-content-proper div.activeAreaWrapper div.activeArea p.CheckoutFoCLink a").click()
    sleep(2)
    driver.close()a


def selectDate(driver):
    table = driver.find_element_by_css_selector(
        "html body div#ui-datepicker-div.ui-datepicker.ui-widget.ui-widget-content.ui-helper-clearfix.ui-corner-all table.ui-datepicker-calendar tbody")
    currentDate = datetime.now().day
    if 30 - currentDate < 3:
        offset = 30 - currentDate
        driver.find_element_by_css_selector("html body div#ui-datepicker-div.ui-datepicker.ui-widget.ui-widget-content.ui-helper-clearfix.ui-corner-all div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-all a.ui-datepicker-next.ui-corner-all span.ui-icon.ui-icon-circle-triangle-e").click()
        sleep(2)
        table.find_elements_by_xpath(f'//a[text()="{3-offset}"]')[0].click()
    else:
        table.find_elements_by_xpath(f'//a[text()="{currentDate+3}"]')[0].click()



if __name__ == '__main__':

   while True:
       if datetime.now().time().hour == 6 and datetime.now().time().minute == 0 and datetime.now().time().second < 10:
            book("","","")
