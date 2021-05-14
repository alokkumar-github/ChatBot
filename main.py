import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

import smtplib
from email.message import EmailMessage

import PyPDF2

import cv2

import numpy as np
import pyautogui


# from PIL import Image
# #Open image using Image module
# im = Image.open("images/cuba.jpg")
# #Show actual Image
# im.show()
# #Show rotated Image
# im = im.rotate(45)
# im.show()



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def send_whatsapp_msg():
    pywhatkit.sendwhatmsg('+91-9789919047','Happy BDay...',18,10)


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            return command.lower()
    except:
        pass


def run_alexa():
    try:
        command = take_command()
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
        if command is None:
            talk('I am listening... Please say the command')
        else:
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who is' in command:
                person = command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'date' in command:
                talk('sorry, I have a headache')
            elif 'are you single' in command:
                talk('I am in a relationship with wifi')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'send mail' in command:
                get_email_info()
            else:
                talk('Please say the command again.')
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'COOL_DUDE_EMAIL'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = take_command()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = take_command()
    talk('Tell me the text in your email')
    message = take_command()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = take_command()
    if 'yes' in send_more:
        get_email_info()


def scroll_up_down_waving_yellow_pieace_webcam():
    # https: // www.youtube.com / watch?v = xumx - _FGLaU & t = 135s
    cap = cv2.VideoCapture(0)

    yellow_lower = np.array([22, 93, 0])
    yellow_upper = np.array([45, 255, 255])
    prev_y = 0

    while True:
        ret, frame = cap.read()


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # huge saturation
        mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

        # contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        contours, hierarchy= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)
        # print(hierarchy)
        for c in contours:
            area = cv2.contourArea(c)
            if area > 300:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if y < prev_y:
                    pyautogui.press('space',  interval=1)
                    # pyautogui.hscroll(-30)
                    print('   moving down...')
                else:
                    print('moving up....')
                    # pyautogui.hscroll(30)
                    pyautogui.press('pageup', interval=1)
                prev_y = y


        # cv2.imshow('frame', frame)

        # cv2.imshow('mask', mask)

        if cv2.waitKey(10) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# while True:
#     # run_alexa()
#     # send_whatsapp_msg()
#
#     book = open('oop.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     print(pages)
#     for num in range(7, pages):
#         page = pdfReader.getPage(num)
#         text = page.extractText()
#         talk(text)


if __name__ == '__main__':
    scroll_up_down_waving_yellow_pieace_webcam()
