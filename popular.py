from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

pencere = Tk()
pencere.title("Otomatik Popüler Tweetleyici Yazılımı")
pencere.geometry("600x600+450+150")
pencere.resizable(FALSE, FALSE)
pencere.state("normal")
pencere['bg'] = '#49A'
lbl0 = Label(text="Tweetiniz :", fg="white", bg="green", font=("Open Sans", "18", "normal"))
lbl0.pack()
inputtxt = Text(pencere, height=10,
                width=25,
                bg="light yellow")
inputtxt.pack()



def twgiris():
    msj = inputtxt.get("1.0", "end-1c")
    print(msj)
    print(type(msj))
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://twitter.com/login")
    time.sleep(2)
    kulInp = browser.find_element_by_xpath(
        "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    sfrInp = browser.find_element_by_xpath(
        "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    kulInp.send_keys("Buraya kullanıcı adınız")
    sfrInp.send_keys("Buraya şifreniz")
    sfrInp.send_keys(Keys.ENTER)
    time.sleep(3)
    tplm = ""
    for i in range(2, 7):
        pt = browser.find_element_by_xpath(f"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div/div/div[{i}]/div/div/div[2]/span").text
        # time.sleep(1)

        tplm = tplm + " " + pt + " "
        print(tplm)

    browser.get("https://twitter.com/compose/tweet")
    time.sleep(1)
    tww = browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br")
    tww.send_keys(msj+tplm)
    time.sleep(2)
    tik_i = browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span").click()


buton = Button(pencere, text="Başla", command=twgiris)
buton.pack()

mainloop()
'''
