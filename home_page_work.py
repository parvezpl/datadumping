from impmodul import By, WebDriverWait, EC
from chrom_driver import driver
driver=driver()

class Penting:
    def click_pending(self):
        totall_pending = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome").text

        if totall_pending != 0:
            pendig_click=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a")
            pendig_click.click()
            print("click pending list")
        else:
            print("Not pending any thing")

    def total_pending(self):

        if driver.find_element(By.XPATH,
                               "/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text == '0':
            print("NO PENDING QUESTIONS")
            return '0'
        else:
            totall_pending = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome")
            print(totall_pending.text)
            return totall_pending.text

class Subject:
    def sub_click(self):
        try:
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()
            element = WebDriverWait(driver, 61).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a")))
            driver.find_element(By.XPATH,
                                              "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

        except:
            pass
    def qw(self):
        driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

    def home_page(self):
        try:
            driver.find_element(By.XPATH,"/html/body/div/div[1]/a/div[1]/i").click() #traingi module pr click
            print("direct click traing pr")
        except:
            driver.find_element(By.XPATH,"/html/body/nav/button/span").click()
            driver.find_element(By.XPATH,"/html/body/nav/div/ul/li[1]/a").click()
class PrSolver:
    def conti_all(self):
        try :
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").click() #home
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click() #paper list
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click() #open peper
        except Exception as e:
            print(e)
            from paper_data import WinSwitch
            w=WinSwitch().wincount()
            if  w !=1:
                driver.switch_to.window(WinSwitch().swin())
                driver.close()
            PrSolver().conti_all()