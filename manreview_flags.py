#!/opt/homebrew/bin/python3
# author: solina kim
# last updated: feb 23, 2022
# notes:
#   This script contains a set of keywords that indicate a need for manual review in the READING & WRITING section
#   This script also tests flagging pages based on keywords.

from tkinter import W
import pdfplumber
import re

PATH = './sat-practice-test-1.pdf'
FLAG = 'Adapted from'

start_page = 4
flag  = False
flagged_pages = []

with pdfplumber.open(r'./sat-practice-test-1.pdf') as pdf:
    for i in range(start_page, len(pdf.pages)):
        page = pdf.pages[i]
        string = page.within_bbox((0,0,612,792), relative = True).extract_text(x_tolerance =1, layout=True).strip()
    
        re.sub(r'[^(adapted from)]*','',string)
        if FLAG in string:
            flag = True
            print(flag)
            flagged_pages.append(str(i+1))
        else:
            flag = False

print(flagged_pages)
