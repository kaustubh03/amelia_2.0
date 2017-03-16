######### Amelia Bot #########
######### Created By Kaustubh Saxena #########

#Library Import

import aiml
import os,time,sys,webbrowser,datetime,random,subprocess
from PyQt4 import QtCore, QtGui
from googlefinance import getQuotes
import pyowm
import json
from random import randint
import cv2
import pyttsx
from wikiapi import WikiApi
import urllib2
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
import pyglet
from twilio.rest import TwilioRestClient
import speech_recognition
import wolframalpha
import goslate
import numpy as np
from cv2 import cv
import win32api



########################## Initializers ##############################
wiki = WikiApi()
engine = pyttsx.init()
owm = pyowm.OWM('Enter API Key') ### Weather API key PYOWM
client = TwilioRestClient('Enter API Key','Enter User Key') ### Twilio Key
client_wolfram = wolframalpha.Client('Enter API Key - Wolfram')
rand=(randint(0,90000))
gs = goslate.Goslate()

############################Splash Screen############################
app = QtGui.QApplication(sys.argv)
splash_pix = QtGui.QPixmap('conti.jpg')
splash = QtGui.QSplashScreen(splash_pix)
splash.setMask(splash_pix.mask())
splash.show()
time.sleep(2)
splash.hide()

###########################Welcome Message############################
text2speak = "Welcome To Amelia 2.0"
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text2speak)

engine.runAndWait()

########################### Kernel Code Start ############################
kernel = aiml.Kernel()
########################### Temporary Brain File #########################
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
############################## Mode Selection ################################
select = raw_input("Enter Mode Of Interaction {v for Voice | t For Text} : ")

while True:

########################### VOICE CONTROL #############################
    if select=="v":
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            welcome_msg=".....----.... Speak Now ....----...."
            print welcome_msg
            audio = recognizer.listen(source)

        try:
            print "audio : {0}".format(recognizer.recognize_google(audio))
            message = recognizer.recognize_google(audio)
        except speech_recognition.UnknownValueError:
            print("Could Not Understand Audio, Please Try Text Based Interactions")
            message = raw_input("************* Say Something To Amelia : ")
        except speech_recognition.RequestError as e:
            print("Recog Error; {0}".format(e))
            message = raw_input("************* Say Something To Amelia : ")
    elif select=="t":
        message = raw_input("************* Say Something To Amelia : ")
    else:
        print "Please Select a Mode of Interaction"
        select

########################### kernel now ready for use ######################

#################################Functions################################
    def main_else():
        text2speak = kernel.respond(message)
        print "Amelia : {0}".format(text2speak)
        app = QtGui.QApplication(sys.argv)
        splash_pix = QtGui.QPixmap('robo.jpg')
        splash = QtGui.QSplashScreen(splash_pix)
        splash.setMask(splash_pix.mask())
        splash.show()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak)
        engine.runAndWait()
        splash.hide()

        if kernel.respond(message) == "Lemme Think":
            try:
                results = wiki.find(message)
                article = wiki.get_article(results[0])
                print article.summary
                print "\n Link To the Article {0}".format(article.url)
            except IndexError:
                print "Googling"
                text2speak = "I don't know about it, Lets Google it"
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say(text2speak)
                engine.runAndWait()
                webbrowser.open_new("https://www.google.co.in/search?q={}".format(message))

    def status():
        all_stat = "All Components Functioning Normally"
        python_stat = "Python Core : Normal Functionality"
        aiml_stat = "Aiml Load : Normal"
        kernel_stat = "Kernel : Normal"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(all_stat)
        engine.runAndWait()
        print all_stat
        engine.say(python_stat)
        engine.runAndWait()
        print python_stat
        engine.say(aiml_stat)
        engine.runAndWait()
        print aiml_stat
        engine.say(kernel_stat)
        engine.runAndWait()
        print kernel_stat

    def quit_app():
        splash_pix = QtGui.QPixmap('bye.jpg')
        splash = QtGui.QSplashScreen(splash_pix)
        splash.setMask(splash_pix.mask())
        splash.show()
        time.sleep(0.7)
        print "Amelia : Nice Talking To You. Bye Bye"
        text2speak = "Nice Talking to You, Bye Bye"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak)
        engine.runAndWait()
        time.sleep(0)
        splash.hide()
        exit()

    def save():
        kernel.saveBrain("bot_brain.brn")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say('Saving Kernel')
        engine.runAndWait()

    def result():
        kuk = "http://result.kuk.ac.in/index.php?nu=9894274"
        page = urllib2.urlopen(kuk)

        soup = BeautifulSoup(page, "html.parser")
        # print soup.prettify()

        contents = [str(x.text) for x in soup.find(id="txtClassId").find_all('option')]  # List Comprehension
        # print contents
        matching_a = [s for s in contents if "B.TECH" in s]
        matching_b = [s for s in contents if "B.Tech" in s]
        matching_c = [s for s in contents if "BTECH" in s]
        res_count = len(matching_a) + len(matching_b) + len(matching_c)
        print "Total Number Of B.Tech Results Out : {0}".format(res_count)
        if res_count != 0:
            for res_a in matching_a:
                print res_a
                client.messages.create(from_='+13343848545',
                                       to='+919034232578',
                                       body='{0} - Check http://result.kuk.ac.in/index.php?nu=9894274'.format(res_a))
            for res_b in matching_b:
                print res_b
                client.messages.create(from_='+13343848545',
                                       to='+919034232578',
                                       body='{0} - Check http://result.kuk.ac.in/index.php?nu=9894274'.format(res_b))
            for res_c in matching_c:
                print res_c
                client.messages.create(from_='+13343848545',
                                       to='+919034232578',
                                       body='{0} - Check http://result.kuk.ac.in/index.php?nu=9894274'.format(res_c))

            print "SMS Sent Successfully."

    def imdb():
        query_entertain = raw_input("Enter Movie, Character or Cast : ")
        webbrowser.open_new("http://www.imdb.com/find?ref_=nv_sr_fn&q={0}&s=all".format(query_entertain))

    def play_music():
        randomfile = random.choice(os.listdir("D:\\Music\\Collection\\"))
        file1 = 'D:\\Music\\Collection\\' + randomfile
        music = pyglet.media.load(file1)
        print ("Song : {0}").format(randomfile)
        print ("Duration(in Seconds) : {0}").format(music.duration)
        print "Starting Playback"
        subprocess.call(['C:\\Program Files\\Windows Media Player\\wmplayer.exe', file1])
        print "Playback Stopped"

    def selfie():
        text2speak4 = "Starting Amelia Cam"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak4)
        engine.runAndWait()

        cam = cv2.VideoCapture(0)

        cv2.namedWindow("Amelia Cam")

        img_counter = 0

        text2speak5 = "Press Spacebar To Take A Photo, Press Q To View Photos and Escape Key To Quit"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak5)
        engine.runAndWait()

        while True:
            ret, frame = cam.read()
            cv2.imshow("Amelia Cam", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                cam_exit = "Exiting"
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say(cam_exit)
                engine.runAndWait()
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "camera/amelia_cam_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                photo_click = "Photo Clicked"
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say(photo_click)
                engine.runAndWait()
            elif k % 256 == 113:
                # Q pressed For View Gallery
                subprocess.Popen('explorer "C:\Path\Of\Folder"')
                viewer = "Opening Photos"
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say(viewer)
                engine.runAndWait()
        cam.release()

        cv2.destroyAllWindows()

    def weather():
        observation = owm.weather_at_place('Yamunanagar,in')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')
        print temp
        weather_result = [temp[i] for i in temp]
        print "Current Temperature : {0} C".format(weather_result[2])
        print "Max Temperature : {0} C".format(weather_result[0])
        print "Minimum Temperature : {0} C".format(weather_result[3])
        print "Humidity : {0}".format(w.get_humidity())

    def dictionary():
        message_dict = raw_input("Enter Word : ")
        dictionary = PyDictionary(message_dict)
        print (dictionary.printMeanings())
        print "Translation To Hindi : {0}".format((dictionary.translate(message_dict, 'hi')))

    def rail():
        print "*******************---------- Amelia Railway Information System (ARIS) ----------**********************"
        choice = raw_input(
            "Input : \n 0 for Train Info \n 1 for Live Train Status \n 2 for Train Route \n 3 for Train Fare Enquiry \n 4 for Train arrivals at a Station \n 5 for Cancelled Trains \n 6 Station Name to Code \n 7 Station Code to Name \n Choice : ")

        if choice == "0":
            print "********** Train Information **********"
            train = raw_input("Enter Train Number or Name : ")
            url = "http://api.railwayapi.com/route/train/{0}/apikey/Enter Railway API Key/".format(train)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())

            print "Train Name : {0}".format(data['train']['name'])
            print "Train Number : {0}".format(data['train']['number'])

            classes = data['train']['classes']

            for class_info in classes:
                print "Classes : {0} - {1}".format(class_info['class-code'], class_info['available'])

            days = data['train']['days']
            for day in days:
                print "Days : {0} - {1}".format(day['day-code'], day['runs'])

        elif choice == "1":
            print "********** Live Train Status **********"
            train = raw_input("Enter Train Number : ")
            doj = raw_input("Enter Date of Journey in YYYYMMDD Format : ")
            url = "http://api.railwayapi.com/live/train/{0}/doj/{1}/apikey/Enter Railway API Key/".format(train, doj)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())

            print "Live Status For {0} : {1}".format(train, data['position'])

        elif choice == "2":
            print "********** Train Route **********"
            train = raw_input("Enter Train Number : ")
            url = "http://api.railwayapi.com/route/train/{0}/apikey/Enter Railway API Key/".format(train)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())
            print "Train Name : {0}".format(data['train']['name'])
            for route_info in data['route']:
                print "Station Name : {0}".format(route_info['fullname'])
                print "Station Code : {0}".format(route_info['code'])
                print "Station Number : {0}".format(route_info['no'])
                print "Distance From Source : {0}".format(route_info['distance'])
                print "Scheduled Arrival : {0}".format(route_info['scharr'])
                print "Scheduled Departure : {0}".format(route_info['schdep'])
                print "Day of Running : {0}".format(route_info['day'])
                print "State : {0}".format(route_info['state'])
                print "---------------------------------------------------------"

        elif choice == "3":
            print "********** Train Fare Enquiry **********"
            train = raw_input("Enter Train No. : ")
            source = raw_input("Enter Source Station Code: ")
            dest = raw_input("Enter Destination Station Code: ")
            age = raw_input("Enter Age : ")
            quota = raw_input("Enter Quota Code (To Know - http://www.indianrail.gov.in/quota_Code.html) : ")
            doj = raw_input("Enter Date Of Journey in DD-MM-YYYY format : ")

            url = "http://api.railwayapi.com/fare/train/{0}/source/{1}/dest/{2}/age/{3}/quota/{4}/doj/{5}/apikey/Enter Railway API Key/".format(
                train, source, dest, age, quota, doj)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())
            print "*_*_*_*_*_*_*_*** Fare Enquiry ***_*_*_*_*_*_*_*"
            print "Train Number : {0} , {1}".format(data['train']['number'], data['train']['name'])
            print "From : {0} ({1})".format(data['from']['name'], data['from']['code'])
            print "To : {0} ({1})".format(data['to']['name'], data['to']['code'])
            print "Quota : {0} ({1})".format(data['quota']['name'], data['quota']['code'])
            for fare_info in data['fare']:
                print "{0} : {1} INR".format(fare_info['name'], fare_info['fare'])

        elif choice == "4":
            print "********** Train Arrivals at Station **********"
            stat_code = raw_input("Enter Station Code : ")
            hours = raw_input("Hours to search within : ")
            url = "http://api.railwayapi.com/arrivals/station/{0}/hours/{1}/apikey/Enter Railway API Key/".format(stat_code, hours)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())
            for train_stat in data['train']:
                print "Train Number : {0}".format(train_stat['number'])
                print "Train Name : {0}".format(train_stat['name'])
                print "Scheduled Arrival {0}".format(train_stat['scharr'])
                print "Scheduled Departure {0}".format(train_stat['schdep'])
                print "Actual Arrival {0}".format(train_stat['actarr'])
                print "Actual Departure {0}".format(train_stat['actdep'])
                print "Delayed Arrival : {0}".format(train_stat['delayarr'])
                print "Delayed Departure : {0}".format(train_stat['delaydep'])
                print "--------------------------------"


        elif choice == "5":
            print "Cancelled Trains"
            cancel_date = raw_input("Enter Date In DD-MM-YYYY Format : ")
            url = "http://api.railwayapi.com/cancelled/date/{0}/apikey/Enter Railway API Key/".format(cancel_date)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())
            for train_stat in data['trains']:
                print "Source : {0} - {1}".format(train_stat['source']['name'], train_stat['source']['code'])
                print "Destination : {0} - {1}".format(train_stat['dest']['code'], train_stat['dest']['code'])
                print "Train : {0} {1} ; Start Time {2}:".format(train_stat['train']['number'], train_stat['train']['name'],
                                                                 train_stat['train']['start_time'])
                print "------------------------------------------"


        elif choice == "6":
            print "********************** Station Name to Code **********************"
            station = raw_input("Enter Enter Station Name : ")
            url = "http://api.railwayapi.com/name_to_code/station/{0}/apikey/Enter Railway API Key/".format(station)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())

            for stat_name in data['stations']:
                print "Fullname :{0}".format(stat_name['fullname'])
                print "Station Code :{0}".format(stat_name['code'])
                print "State : {0}".format(stat_name['state'])
                print "Latitude Location : {0}".format(stat_name['lat'])
                print "Longitude Location : {0}".format(stat_name['lng'])
                print "----------------------------------------------------------------"

        elif choice == "7":
            print "*********************** Station Code to Name ************************"

            code = raw_input("Enter Station Code : ")
            url = "http://api.railwayapi.com/code_to_name/code/{0}/apikey/Enter Railway API Key/".format(code)
            response = urllib2.urlopen(url)
            data = json.loads(response.read())

            for stat_code in data['stations']:
                print "Station Code : {0}".format(stat_code['code'])
                print "Station Name : {0}".format(stat_code['fullname'])
                print "Latitude : {0}".format(stat_code['lat'])
                print "Longitude : {0}".format(stat_code['lng'])
                print "State : {0}".format(stat_code['state'])
                print "--------------------------------------------------------------------"

    def stock():
        stock_symbol = raw_input("Enter a Stock Symbol : ")
        print json.dumps(getQuotes(stock_symbol), indent=2)

    def google():
        text2speak6 = "Enter Your Term To Google"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak6)
        engine.runAndWait()
        goog_term = raw_input("Enter Your Term to Google : ")
        webbrowser.open('https://www.google.co.in/?gfe_rd=cr&ei=o7ahV5PkMt3mugTXnbugCw#q={0}'.format(goog_term))
        text2speak7 = "Googling it, Check Your Browser."
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text2speak7)
        engine.runAndWait()
        print "Googling it, Check Your Browser."

    def date():
        date = "Today's Date:{0}".format(datetime.date.today())
        print date
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(date)
        engine.runAndWait()

    def time_now():
        time = "Current Time:{0}".format(time.strftime("%I:%M:%S"))
        print time
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(time)
        engine.runAndWait()

    def status():
        all_stat = "All Components Functioning Normally"
        python_stat = "Python Core : Normal Functionality"
        aiml_stat = "Aiml Load : Normal"
        kernel_stat = "Kernel : Normal"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(all_stat)
        engine.runAndWait()
        print all_stat
        engine.say(python_stat)
        engine.runAndWait()
        print python_stat
        engine.say(aiml_stat)
        engine.runAndWait()
        print aiml_stat
        engine.say(kernel_stat)
        engine.runAndWait()
        print kernel_stat

    def wolfram_module():
        query_wolfram=raw_input("Enter Any Query to be Computed : ")
        res_wolfram = client_wolfram.query(query_wolfram)
        print(next(res_wolfram.results).text)

    def hand_detect():
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            drawing = np.zeros(img.shape, np.uint8)

            max_area = 0

            for i in range(len(contours)):
                cnt = contours[i]
                area = cv2.contourArea(cnt)
                if (area > max_area):
                    max_area = area
                    ci = i
            cnt = contours[ci]
            hull = cv2.convexHull(cnt)
            moments = cv2.moments(cnt)
            if moments['m00'] != 0:
                cx = int(moments['m10'] / moments['m00'])  # cx = M10/M00
                cy = int(moments['m01'] / moments['m00'])  # cy = M01/M00

            centr = (cx, cy)
            cv2.circle(img, centr, 5, [0, 0, 255], 2)
            cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
            cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)

            cnt = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            hull = cv2.convexHull(cnt, returnPoints=False)

            if (1):
                defects = cv2.convexityDefects(cnt, hull)
                mind = 0
                maxd = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    dist = cv2.pointPolygonTest(cnt, centr, True)
                    cv2.line(img, start, end, [0, 255, 0], 2)

                    cv2.circle(img, far, 5, [0, 0, 255], -1)
                print(i)
                i = 0
            cv2.imshow('output', drawing)
            cv2.imshow('input', img)

            k = cv2.waitKey(10)
            if k == 27:
                break
    def mousetrack():
        posx = 0
        posy = 0


        ########### You can add any type of a blob in to this algo ####################
        ########### For example you can use a nose detection algorythm in here##########
        def getthresholdedimg(im):
            imghsv = cv.CreateImage(cv.GetSize(im), 8, 3)
            cv.CvtColor(im, imghsv, cv.CV_BGR2HSV)  # Convert image from RGB to HSV
            imgthreshold = cv.CreateImage(cv.GetSize(im), 8, 1)
            cv.InRangeS(imghsv, cv.Scalar(23, 100, 100), cv.Scalar(25, 255, 255), imgthreshold)  ## catch the orange yellow blob
            return imgthreshold


        #################################################################################

        def getpositions(im):
            leftmost = 0
            rightmost = 0
            topmost = 0
            bottommost = 0
            temp = 0
            for i in range(im.width):
                col = cv.GetCol(im, i)
                if cv.Sum(col)[0] != 0.0:
                    rightmost = i
                    if temp == 0:
                        leftmost = i
                        temp = 1
            for i in range(im.height):
                row = cv.GetRow(im, i)
                if cv.Sum(row)[0] != 0.0:
                    bottommost = i
                    if temp == 1:
                        topmost = i
                        temp = 2
            return (leftmost, rightmost, topmost, bottommost)


        capture = cv.CaptureFromCAM(0)
        cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
        cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 720)
        frame = cv.QueryFrame(capture)
        test = cv.CreateImage(cv.GetSize(frame), 8, 3)
        cv.NamedWindow("output")
        previous_x = 0
        previous_y = 0
        while (1):
            frame = cv.QueryFrame(capture)
            cv.Flip(frame, frame, 1)
            imdraw = cv.CreateImage(cv.GetSize(frame), 8, 3)  # we make all drawings on imdraw.
            imgyellowthresh = getthresholdedimg(frame)  # we get coordinates from imgyellowthresh
            cv.Erode(imgyellowthresh, imgyellowthresh, None, 1)  # eroding removes small noises
            (leftmost, rightmost, topmost, bottommost) = getpositions(imgyellowthresh)
            if (leftmost - rightmost != 0) or (topmost - bottommost != 0):
                lastx = posx
                lasty = posy
                posx = cv.Round((rightmost + leftmost) / 2)
                posy = cv.Round((bottommost + topmost) / 2)
                if lastx != 0 and lasty != 0:
                    win32api.SetCursorPos((posx, posy))

            cv.Add(test, imdraw, test)
            cv.ShowImage("output", test)
            if cv.WaitKey(10) >= 0:
                break
        cv.DestroyWindow("output")


########################### Exit #########################
    if message == "quit" or message == "exit":
        quit_app()

########################### Save The Brain ########################
    elif message == "save":
        save()

########################## RESULT #################################
    elif message == "result":
        result()

########################### IMDB Search #########################
    elif message == "imdb":
        imdb()

############################ Play Music #########################
    elif message =="play music":
        play_music()

############################ Camera #############################
    elif message == "selfie":
        selfie()

######################### Weather ##############################
    elif message == "weather":
        weather()

########################## Translate ###########################
    elif message == "dictionary":
        dictionary()

########################### Railways ###########################
    elif message == "rail":
        rail()

######################### Stock Market #########################
    elif message == "stock" :
        stock()

######################### Google ###############################
    elif message == "google":
        google()

########################## Date and Time##########################
    elif message=="date":
        date()

    elif message=="time":
        time_now()

######################### Status ########################
    elif message=="status":
        status()
######################### Wolfram Alpha ###################
    elif message=="wolf":
        wolfram_module()
########################## Location ########################
    elif "where is" in message:
        message = message.split(" ")
        location = message[2]
        print "Hold on Boss, I will show you where " + location + " is."
        voic_comm = "Hold on Boss, I will show you where" + location + "is."
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(voic_comm)
        engine.runAndWait()
        webbrowser.open("https://www.google.co.in/maps?q={0}".format(location))

######################### Translate ########################
    elif message =="translate":
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say('Enter Your Phrase : ')
        engine.runAndWait()
        query_phrase = raw_input("Enter Your Phrase : ")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say('Enter Language To Continue')
        engine.runAndWait()
        lang = raw_input("Enter Language to Continue : ")
        print(gs.translate(query_phrase, lang))

########################### Hand Detect #######################
    elif message =="hand detect":
        hand_detect()
########################## Mouse Tracking #####################
    elif message =="touchless":
        mousetrack()

######################### Help ##########################
    elif message == "help":
        print "********************* Project Amelia Handbook ******************** \n"
        print "save - Save The Brain in a .brn File."
        print "quit - Quit Amelia and Shut Down."
        print "google - Google Your Search Term."
        print "play music - Play a Random Music File."
        print "date - Today's Date."
        print "time - Current Time."
        print "dictionary - Search for your term meanings."
        print "weather - Current Weather Details."
        print "selfie - Opens Camera To Click Photos."
        print "rail - Enter ARIS System to get information regarding Indian Railways."
        print "stock - Get Information Of Stock Market."
        print "imdb - Search For any Movie, Actor, TV Show in IMDb."
        print "result - Get B.tech results Notification on your phone."
        print "status - Check Status of the Amelia's Working. \n"
        print "wolf - To Start Computational Engine"

    elif message == "":
        print "Please Enter Input"


######################### Normal Response From AIML And if Not found WIKI and Google######################
    else:
        main_else()
