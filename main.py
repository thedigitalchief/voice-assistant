from re import search
from click import command
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import os
import subprocess 
import sys
from bs4 import BeautifulSoup
import requests
from keyboard import press
from keyboard import press_and_release
import webbrowser


# initial variable setup with engine and listener
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)

# talk() function that takes text from the user
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
talk('Hello sir')


def take_command():

    return command

def run_computer():


run_computer()    
