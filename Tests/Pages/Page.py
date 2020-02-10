
class Page(object):
    url = "/"
    base_url = "​http://qalab.pl.tivixlabs.com/"

    def __init__(self, context):
        self.browser = context.browser
        self.base_url = context.url

    def get_url(self):
        return self.base_url + self.url

    def go_to_page(self):
        self.browser.get(self.get_url())
        self.browser.implicitly_wait(10)
