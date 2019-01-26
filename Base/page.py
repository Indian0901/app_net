from Page.page_set import Page_set
from Page.page_more import Page_more
from Page.page_net import Page_net


class Get_obj:
    def __init__(self,driver):
        self.driver = driver

    def set_obj(self):
        return Page_set(self.driver)
    def more_obj(self):
        return Page_more(self.driver)
    def net_obj(self):
        return Page_net(self.driver)