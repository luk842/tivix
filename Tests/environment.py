
from behave.runner import Context
from selenium import webdriver

from Configs import config


class Setup(object):
    def __init__(self, context: Context):
        self.context = context


    @classmethod
    def prepare_browser(cls, context: Context):
        try:
            browser = context.config.userdata['browser']
        except KeyError:
            raise Exception("Please set browser! Add for example -D browser=chrome")

        if browser == "local_chrome":
            context.browser = webdriver.Chrome(
                executable_path=config.chrome_driver_localization)

        else:
            raise Exception("Browser " + browser + " not found. Please check your config file")

        context.browser.maximize_window()

    @classmethod
    def set_env(cls, context: Context):
        try:
            env = context.config.userdata['env']
        except KeyError:
            raise Exception("Please set environment! For example -D env=stage")

        if env == "tivix":
            context.url = config.url_address
        else:
            raise Exception("Environment " + env + " not found. Please check your config file")


def before_all(context):
    Setup.set_env(context)
    Setup.prepare_browser(context)


def before_scenario(context, scenario):
    context.browser.delete_all_cookies()


# def after_scenario(context, scenario):
    # context.browser.execute_script('window.localStorage.clear();')


def after_all(context):
    context.browser.quit()
