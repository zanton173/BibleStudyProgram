from selenium import webdriver
import time
import os
import openpyxl
import sys
import random
import tkinter as tk
from random import choice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def openBlueLetter(book, chap, vs, vsn):
        bookNames = ['Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jos', 'Jdg', 'Rth', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch', '2Ch', 'Ezr', 'Neh', 'Est', 'Job', 'Psa', 'Pro', 'Ecc', 'Sng', 'Isa', 'Jer', 'Lam', 'Eze', 'Dan', 'Hos', 'Joe', 'Amo', 'Oba', 'Jon', 'Mic', 'Nah', 'Hab', 'Zep', 'Hag', 'Zec', 'Mal', 'Mat', 'Mar', 'Luk', 'Jhn', 'Act', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Phl', 'Col', '1Th', '2Th', '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jas', '1Pe', '2Pe', '1Jo', '2Jo', '3Jo', 'Jde', 'Rev']
        books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalm', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']
        for shrti in books:
                if (book.lower() == shrti.lower()):
                        for shrtj in range(len(bookNames)):
                                shrtj = bookNames[books.index(shrti)]
                                print(str(shrtj))
                                break
                else:
                        continue
        global blueLetter
        blueLetter = webdriver.Chrome()
        blueLetter.maximize_window()
        for shrt in books:
                if (shrt.lower() == book.lower()):
                        print('test?')
        blueLetter.get('https://www.blueletterbible.org')
        time.sleep(3)
        # search_field = blueLetter.find_element_by_xpath("//nav[2]")
        # search_field = blueLetter.find_element_by_xpath("//div[@class='nav-search__wrap']/input[1]")
        search_field = blueLetter.find_element_by_xpath("//div[4]/input[@name='Criteria' and @type='text' and 1]")
        time.sleep(1)
        search_field.clear()
        search_field.send_keys(book + ' ' + chap + ':' + vs)
        time.sleep(1)
        # ActionChains(blueLetter).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        # time.sleep(1)
        # version = blueLetter.find_element_by_xpath("//div/span[@title='ESV: English Standard Version']")
        time.sleep(1)
        ActionChains(blueLetter).key_down(Keys.TAB).key_up(
                Keys.TAB).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        currentVersionURL = blueLetter.current_url
        blueLetter.get(currentVersionURL.replace('kjv', vsn))
        time.sleep(2)
        #verseSelection = blueLetter.find_element_by_xpath('//*[@id="yui-gen42"]')
        # openBlueLetterTools(blueLetter)

#openBlueLetter('John', '1', '1', 'ESV ')


def openBlueLetterTools(bl):
        ActionChains(bl).key_down(Keys.CONTROL).key_down(Keys.F4).key_up(Keys.CONTROL).perform()
        # .send_keys('tools') \
        # .key_down(Keys.TAB) \
        # .key_up(Keys.TAB) \
        # .key_down(Keys.SPACE) \
        # .key_up(Keys.SPACE) \
        # .key_down(Keys.ESCAPE) \
        # .key_up(Keys.ESCAPE) \
        # .key_down(Keys.TAB) \
        # .key_up(Keys.TAB) \
        # .key_down(Keys.ENTER) \
        # .key_up(Keys.ENTER) \
        # .perform()


def programGUI():
        window = tk.Tk()
        window.geometry("720x480")
        window.resizable(width=False, height=False)
        window.title('Bible Study Program')
        header = "This program should help increase productivity in anazlying scripture"
        label = tk.Label(text=header)

        global versesList

        book = tk.Entry(width=25)
        chapter = tk.Entry(width=25)
        verses = tk.Entry(width=25)
        version = tk.Entry(width=25)

        submit = tk.Button(text="Search", command=lambda: openBlueLetter(
                book.get(), chapter.get(), verses.get(), version.get()))

        book.insert(0, "book (John, Genesis, Revelation)")
        chapter.insert(0, "chapter")
        verses.insert(0, "verses (1:4, 33:50, 10:11)")
        version.insert(0, "ESV")

        label.pack()
        book.pack()
        chapter.pack()
        verses.pack()
        version.pack()
        submit.pack()

        versesList = verses.get()

        window.mainloop()


        # programGUI()
