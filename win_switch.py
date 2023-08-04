from chrom_driver import driver
driver=driver()

class WinSwitch:
    def __init__(self):
        self.handles = driver.window_handles
        self.size = len(self.handles)
        self.parent_handle = driver.current_window_handle
        for x in range(self.size):
            if self.handles[x] != self.parent_handle:
                driver.switch_to.window(self.handles[x])
                self.swinn = self.handles[x]
    def wincount(self):
        return self.size

    def swin(self):
        if len(self.handles) != 1:
            return self.swinn
        return self.parent_handle

    def  pwin(self):
        return self.parent_handle
WinSwitch()