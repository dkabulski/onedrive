from selenium import webdriver
import string, random, names,time,re,urllib
from twocaptchaapi import TwoCaptchaApi
api = TwoCaptchaApi('API KEY HERE')
png ='captch.jpg'
days = random.randint(0, 27)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def urs_generator(size=5, chars=string.digits+string.digits): # +
    return ''.join(random.choice(chars) for _ in range(size))

def pwd_generator(size=10, chars=string.ascii_uppercase+ string.digits + string.punctuation): # + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def onedrive_utm(utm_link):
    # utm_link = 'https://onedrive.live.com?invref=e9f36c73a3e0ddc9&invscr=90'
    browser = webdriver.Chrome(executable_path = r'C:\Users\Oladimeji Olaolorun\github\Projects\chromedriver.exe')
    browser.maximize_window()
    browser.get(utm_link)
    time.sleep(3)
    username = browser.find_element_by_id('signup').click()
    time.sleep(2)
    meme = browser.find_element_by_id('MemberName')
    meme.send_keys( names.get_first_name()+urs_generator()+'@outlook.com')
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    time.sleep(1)
    passed = browser.find_element_by_id('PasswordInput').send_keys(pwd_generator())
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    time.sleep(1)
    for i in range(0,2):  # try this block of code 6 times
            try:
                images = browser.find_elements_by_tag_name('img')
                for image in images:
                    new_img =image.get_attribute('src')

                urllib.request.urlretrieve(new_img, png)  # save the image

                with open(png, 'rb') as captcha_file:
                    captcha = api.solve(captcha_file)

                results = captcha.await_result()
                results = re.sub(r"\s+", "", results, flags=re.UNICODE)
            except:
                pass
            #     if ERROR_BAD_DUPLICATES: # if not then wait 5 seconds then try again
            #         time.sleep(5)
            # else:
            #     break
    time.sleep(2)
    browser.find_element_by_xpath('//*[starts-with(@id,"wlspispSolutionElement")]').send_keys(results)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="iSignupAction"]').click()
    try:
        browser.find_element_by_xpath('//*[@id="idFirstName"]').send_keys(names.get_first_name())
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="idLastName"]').send_keys(names.get_last_name())
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="BirthDay"]').send_keys(days)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="BirthMonth"]').send_keys(months[random.randint(0, 11)])
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="BirthYear"]').send_keys(int(time.strftime('%Y')) -random.randint(20, 35))
        browser.find_element_by_id('iNext').click()
    except:
        pass
    time.sleep(60)
    browser.quit()

onedrive_utm('https://onedrive.live.com?invref=e9f36c73a3e0ddc9&invscr=90')
print('Wel done mate')
