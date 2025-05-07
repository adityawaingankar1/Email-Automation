import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

listener = sr.Recognizer()
tts=pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone as source:
        print("program is listening....")
        voice=listener.listen(source)
        data=listener.recognize_google(voice)
        print(data)
        return data.lower()

dict={"harsh":"harsh.deshmukh234@gmail.com"}   
    
def send_mail(receiver, subject, body):   
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("adityawaingankar1@gmail.com","iksgchdpoyswbajt")
    email=EmailMessage()
    email["From"]="adityawaingankar1@gmail.com"
    email["To"]=receiver
    email["Subject"]=subject
    email.set_content(body)
    server.send_message(email)
    
def main_poc():
    talking_tom("To whom do you want to send this email?")
    name=mic()
    receiver=dict[name]
    talking_tom("what is the subject of the email?")
    subject=mic()
    talking_tom("Speak the message of the email")
    body=min()
    send_mail(receiver, subject, body)
    print("your email has been sent")
main_poc()