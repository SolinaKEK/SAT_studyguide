#!/opt/homebrew/bin/python3
# author: solina kim
# last updated: feb 23, 2022
# notes:
#   reading section always starts on page 4
#   other sections are "switched" to after a bold 'STOP' message at the bottom of the page
#   this script will check for the 'STOP' message an update 'index'

import pdfplumber
import re

PATH = './sat-practice-test-1.pdf'
STOP_DIM = (250,610,330,660) # note: very very tight dimensions lol (but for the better honestly?)

start_page = 4
switch  = False

with pdfplumber.open(r'./sat-practice-test-1.pdf') as pdf:
    for i in range(start_page, len(pdf.pages)):
        page = pdf.pages[i]
        string = page.within_bbox(STOP_DIM, relative = True).extract_text(x_tolerance =1, layout=True).strip()
        string = re.sub(r'[^(STOP)]*','',string)
        if string == 'STOP':
            switch = True
            #print(string)
            #print(switch)
        else:
            switch = False
