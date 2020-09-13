from selenium import webdriver
import time, os, openpyxl, sys, random
import tkinter as tk
from random import choice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def openBlueLetter(psg, vsn):
	global blueLetter
	blueLetter = webdriver.Chrome()
	blueLetter.maximize_window()
	blueLetter.get('https://www.blueletterbible.org')
	time.sleep(3)
	#search_field = blueLetter.find_element_by_xpath("//nav[2]")
	# search_field = blueLetter.find_element_by_xpath("//div[@class='nav-search__wrap']/input[1]")
	search_field = blueLetter.find_element_by_xpath("//div[4]/input[@name='Criteria' and @type='text' and 1]")
	time.sleep(1)
	search_field.clear()
	search_field.send_keys(psg)
	time.sleep(1)
	#ActionChains(blueLetter).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
	#time.sleep(1)
	#version = blueLetter.find_element_by_xpath("//div/span[@title='ESV: English Standard Version']")
	time.sleep(1)
	ActionChains(blueLetter).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
	currentVersionURL = blueLetter.current_url
	blueLetter.get(blueLetter.current_url.replace('kjv', vsn))

def programGUI():
	window = tk.Tk()
	window.geometry("720x480")
	window.resizable(width=False, height=False)
	window.title('Bible Study Program')
	header = "This program should help increase productivity in anazlying scripture"
	label = tk.Label(text=header)
	passage = tk.Entry(width=45)
	version = tk.Entry(width=15)
	submit = tk.Button(text="Search", command=lambda : openBlueLetter(passage.get(), version.get()))
	passage.insert(0, "passage (John 16:33; Rev 3; Jer 5:23)")
	version.insert(0, "ESV, NLT, KJV")
	label.pack()
	passage.pack()
	version.pack()
	submit.pack()
	window.mainloop()

programGUI()