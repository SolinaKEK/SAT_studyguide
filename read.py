#!/usr/bin/env python3

# Authors: Santiago Rodriguez, Solina Kim
# Last Updated
# Notes:
#       section switcher
# -----------------------------------------
# Imports
from matplotlib.pyplot import get
import pdfplumber
import os
from config import *
import re
import collections
import sys

#Globals
DIR = 'tests'
PAGE_TYPES = PAGE_DIM.keys()
BOOK = {} 


#Functions
def getPath(directory=DIR):
    for filename in os.listdir(directory):
        file = os.path.join(directory,filename)
        if os.path.isfile(file) and file.endswith('.pdf'):
            yield file
        

def getText(filepath = None):
    if not os.path.isfile(filepath):
        return 1
    
    with pdfplumber.open(r'`filepath`') as pdf:
        for page in pdf:
            section = get_section(page) # checking section number to figure out type of page
            
            left = page.within_bbox((PAGE_DIM['default_reading'])[0], relative = True).extract_text(x_tolerance =1, layout=True)    
            right = page.within_bbox((PAGE_DIM['default_reading'])[1], relative = True).extract_text(x_tolerance =1, layout=True)    
            #type of page
            #     page                       [type of page]   left  = 0 / right = 1                 default values

def appendtoBook(pageNumber ,left, right, pageType):
    BOOK[pageNumber][0] = left  #array of text
    BOOK[pageNumber][1] = right #array of text
    BOOK[pageNumber]['type'] = pageType # string


def switch_section(page):
    string = page.within_bbox(STOP_DIM, relative = True).extract_text(x_tolerance =1, layout=True).strip()
    string = re.sub(r'[^(STOP)]*','',string)
    
    if string == 'STOP':
            return True
    else:
            return False

def read_answers(page, pagetype):
    print(page.within_bbox(ANSWERPG_DIMS['math_calc_dim'], relative = True).extract_text(x_tolerance =1, layout=True))
    pass

def get_section(page):
    section = page.within_bbox(DIM, relative = True).extract_text(x_tolerance =1, layout=True).strip()
    yield section

def main():
    getPath(DIR)


if __name__ == '__main__':
    main()