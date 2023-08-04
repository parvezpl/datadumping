from impmodul import pd, By
from chrom_driver import driver
from win_switch import WinSwitch
driver=driver()

class TotalAnswer:
    def qw1a(self):
        # driver.execute_script(
        #     "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[0].style.display = 'block';") #currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr") #answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_0']").text #correct answer
        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")

        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text


    def qw2a(self):
        # driver.execute_script(
        #     "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[1].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_1']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")
        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text

    def qw3a(self):
        # driver.execute_script(
        #     "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[2].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_2']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text



    def qw4a(self):
        # driver.execute_script(
        #     "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[3].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_3']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text

    def qw5a(self):
        # driver.execute_script(
        #     "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[4].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_4']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text




class Totalans:
    def total_ans(self):
        ans_object = TotalAnswer()
        a = ans_object.qw1a()
        b = ans_object.qw2a()
        c = ans_object.qw3a()
        d = ans_object.qw4a()
        e = ans_object.qw5a()
        return [a, b, c, d, e]


class TotalQw(Totalans):
    def tatal_qw(self):
        aqw = driver.find_elements(By.XPATH, "//th[@class ='text-gray-800 p-1']")
        allqw = []
        for i in aqw:
            allqw.append(i.text)
        return allqw

class MakeDict:
    def make_dict(self):
        obj = TotalQw()
        a = obj.tatal_qw()
        b = obj.total_ans()
        return dict(zip(a, b))

class DataExport:
    def data_frame(self): # qw and answer ka data frame taiyar krta hai
        qw = TotalQw().tatal_qw()
        aa = TotalQw().total_ans()
        dt = {'question': qw,
              'answer': aa}
        data = pd.DataFrame(dt)
        return data

    def data_dump(self,ddata):
        # DataExport().data_frame()
        # data=DataExport().data_frame()
        d=ddata
        d.to_excel("F:\program\selenium\cctns\paperdata.xlsx", index=False)
        print("data dump")

class ReadData:
    def read_data(self):
        dff= pd.read_excel("F:\program\selenium\cctns\paperdata.xlsx", index_col=0 )
        df=pd.DataFrame(dff)
        return df


class Dataa:
    def __init__(self):
        try:
            self.dff = pd.read_excel('F:\program\selenium\cctns\paperdata.xlsx', index_col=0)
            self.df =pd.DataFrame(self.dff)
            # print(self.df)
            axx = DataExport().data_frame()
            self.codata(self.dff, axx )

        except:
            print("co")
            d = DataExport().data_frame()
            self.wdata(d)

    def rdata(self):
        return self.df

    def wdata(self, d):
        d.to_excel("F:\program\selenium\cctns\paperdata.xlsx", index=True)
        print("export")

    def codata(self,a ,b):
        aa=pd.concat([a, b], ignore_index=True)
        self.wdata(aa)


class Dcd:
    def data_ceate_dump(self):
        s=WinSwitch().pwin()
        driver.switch_to.window(s)
        Dataa()
        print("data dump>>>>>>>")
