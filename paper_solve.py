from impmodul import By
from paper_data import Dcd
from chrom_driver import driver
from win_switch import  WinSwitch
driver=driver()

class FistQw:
    def fist(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def secound(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def third(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def fourth(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()

class Answer:
    def qw1(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[0].style.display = 'block';") #currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr") #answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_0']").text #correct answer
        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input")

        if qwa == 'A':
            aa.click()
        elif qwa == 'B':
            b.click()
        elif qwa == 'C':
            c.click()
        elif qwa == 'D':
            d.click()
        print("qw1 solve")

    def qw2(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[1].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_1']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input")
        if qwa == 'A':
            aa.click()
        elif qwa == 'B':
            b.click()
        elif qwa == 'C':
            c.click()
        elif qwa == 'D':
            d.click()
        print("qw2 solve")
    def qw3(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[2].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_2']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input")

        if qwa == 'A':
            aa.click()
        elif qwa == 'B':
            b.click()
        elif qwa == 'C':
            c.click()
        elif qwa == 'D':
            d.click()

        print("qw3 solve")

    def qw4(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[3].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_3']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input")

        if qwa == 'A':
            aa.click()
        elif qwa == 'B':
            b.click()
        elif qwa == 'C':
            c.click()
        elif qwa == 'D':
            d.click()
        print("qw4 solve")

    def qw5(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[4].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_4']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input")

        if qwa == 'A':
            aa.click()
        elif qwa == 'B':
            b.click()
        elif qwa == 'C':
            c.click()
        elif qwa == 'D':
            d.click()
        print("qw5 solve")
    def sumit(self):
        driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/input[1]").click() #submit

class PaperSM:
    def wwin_all(self):
        self.handles = driver.window_handles
        size = len(self.handles)
        self.parent_handle = driver.current_window_handle
        for x in range(size):
            if self.handles[x] != self.parent_handle:
                driver.switch_to.window(self.handles[x])
                self.swinn = self.handles[x]

    def swin(self):
        if len(self.handles) != 1:
            return self.swinn
        return self.parent_handle

    def  pwin(self):
        return self.parent_handle

    def paper_solver(self):
            o=WinSwitch()
            driver.switch_to.window(o.swin())
            aa = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div[1]/h4")
            print("paper solve", aa.text)
            qw_obj = Answer()
            qw_obj.qw1()
            qw_obj.qw2()
            qw_obj.qw3()
            qw_obj.qw4()
            qw_obj.qw5()
            # driver.switch_to.window(o.swin())
            Dcd().data_ceate_dump()
            qw_obj.sumit()
            driver.close()