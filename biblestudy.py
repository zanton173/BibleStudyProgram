from selenium import webdriver
import time, os, openpyxl, sys, random
from random import choice
from selenium.webdriver.common.keys import Keys

def openBlueLetter():
	global blueLetter
	blueLetter = webdriver.Chrome()
	blueLetter.get('https://www.blueletterbible.org')

def programGUI():
	
