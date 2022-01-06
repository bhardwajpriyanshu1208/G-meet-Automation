# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def Glogin(mail_address, password):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element_by_xpath(
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def turnOffMicCam():
	# turn off Microphone
	time.sleep(2)
	search_box = driver.find_element_by_css_selector('.DPvwYc.JnDFsc.ZXaXZ')
	search_box.click()
	driver.implicitly_wait(3000)

	# turn off camera
	time.sleep(1)
	search_box = driver.find_elements_by_css_selector('.DPvwYc.JnDFsc.ZXaXZ')
	search_box[1].click()
	driver.implicitly_wait(3000)


def joinNow():
	# Join meet
	# print(1)
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element_by_css_selector(
		'.NPEfkd.RveJvd.snByac').click()
	# print(1)


def AskToJoin():
	# Ask to Join meet
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element_by_css_selector(
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	# Ask to join and join now buttons have same xpaths


## turn on captions
def turn_onn_caption():
	driver.implicitly_wait(2000)
	TurnOnCaptions = driver.find_element_by_css_selector(".xEp89c")
	TurnOnCaptions.click()


## see no. of students
def count_students():
	n = driver.find_element_by_css_selector('.uGOf1d')
	print(n.text)

# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})

driver_path = "C:/Users/psbd1/OneDrive/Documents/python/codes/Web-automation/env/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# opt = webdriver.ChromeOptions()
opt.binary_location = brave_path

driver = webdriver.Chrome(executable_path=driver_path, options=opt)

# login to Google account
Glogin('19001003089@jcboseust.ac.in','Priyanshu@123')

# go to google meet
driver.get('https://meet.google.com/ttj-znjy-prg')
turnOffMicCam()
# AskToJoin()
joinNow()
turn_onn_caption()
count_students()





# captionbox


staleElement = True
while staleElement :

        try :

            Caption_tray = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[7]/div")
            Captions = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[7]/div/div[2]/div")
            if Captions.is_displayed() :
                    Caption_text= Captions.text
                    Caption_text = Caption_text.lower()
                    print(Caption_text)
                    
                    
        except(StaleElementReferenceException):

            staleElement = True

        except(NoSuchElementException) :
                staleElement = True

        changed_numstudents = int(students.text)
        print(changed_numstudents)
        if changed_numstudents > Total_numStudents :
                Total_numStudents = changed_numstudents
        elif changed_numstudents < Total_numStudents :
        
                if changed_numstudents <= math.floor(0.2*Total_numStudents):  
                                EndCall=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button/i")
                                EndCall.click()
                        
                


        if count ==0 :

                 words = ("Priyanshu", "Jondoe" , "Johndoe" , "Jon Doe" ,"June Doe" , "Jon" )
                 if any(name in Caption_text for name in words): 

                        UnMute = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[1]/div/div/span/button/div[2]")
                        UnMute.click()
                        mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
                        mixer.music.load("Enter path of your voice recording here")
                        mixer.music.play()
                        time.sleep(4)
                        mixer.music.stop()
                        UnMute.click()
                        count+=1
