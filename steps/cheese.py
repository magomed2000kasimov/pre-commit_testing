from behave import *
from selenium import webdriver


@given('I am on the Google search page')
def open_google_search(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.google.com/")
    pass


@when('I search for "Cheese"')
def searchCheese(context):
    input_edit = context.browser.find_element_by_css_selector("[title='Search']")
    input_edit.send_keys('Cheese')
    button = context.browser.find_element_by_css_selector('.FPdoLc input.gNO89b')
    button.click()


@then('hen the page title should start with "cheese"')
def title(context):
    pass


@then('quit browser')
def quit_browser(context):
    context.browser.quit()
