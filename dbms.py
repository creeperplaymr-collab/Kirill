'''import sqlite3
connection= sqlite3. connect("lessonForDataBase.sl3", 5)
cur= connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT); ")
connection.commit()
connection.close()'''

import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
connection= sqlite3.connect("lessonForDataBase.sl3")
cur= connection.cursor()
cur.execute("CREATE TABLE second_table news (date_time TEXT, title TEXT); ")
connection.commit()

response= requests.get('https://tengrinews.kz/news/')
title.tag= soup.find('span', class_='content_main_item_title')
headline= title_tag.text.strip()
