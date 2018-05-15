import random


class SwipeUtils(object):
    num = (0.65, 0.75, 0.85)
    num2 = (0.1, 0.2, 0.3)

    def __init__(self, driver):
        self.driver = driver

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_down(self, t=1000):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * random.choice(self.num2))
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_up(self, t=1000):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * random.choice(self.num))
        self.driver.swipe(x1, y2, x1, y1, t)
