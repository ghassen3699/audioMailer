import email
import smtplib 
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()
email_list = {
    'person1' : 'person1@gmail.com',
    'person2' : 'person2@gmail.com',
    'person3' : 'person3@gmail.com',
    'person4' : 'person4@gmail.com',
    'person5' : 'person5@gmail.com',
}


# Talk function 
def talk(text) :
    engine.say()
    engine.runAndwait()

# Listen function
def get_info() :
    try :
        with sr.Microphone() as source :
            print('listen')
            voice = listen.listen(source)
            info = listen.recognize_google(voice)
            return info.lower
    except :
        pass


# send the email
def send_mail(receiver, subject, message) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('#### Your email address ###','### Your Pasword ###')
    email = EmailMessage()
    email['From'] = '#### Your email address ###'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


# informations of the email
def get_email_info() :
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    talk('what is the subject of your email?')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()

    send_mail(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'Yes' in send_more :
        get_email_info()


# The principal program
get_email_info()