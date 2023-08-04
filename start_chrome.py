from impmodul import os, subprocess, Options, webdriver

class StarAndDrivr:
    def starter(self):
        os.chdir("C:\Program Files\Google\Chrome\Application")  #chrome app avlabel path
        subprocess.Popen("chrome.exe --remote-debugging-port=9000 --user-data-dir=E:\chrome")
        os.chdir("C:\\Users\\Dell\\Desktop\\selenium")
        opt = Options()
        opt.add_experimental_option("debuggerAddress", "localhost:9000")
        driver = webdriver.Chrome(options=opt)
        driver.get("https://hackathon.uppolice.gov.in/CCTNS-Training/index.aspx")
        print("connected ", " chrome brower start 9000")
        print(driver.title)

