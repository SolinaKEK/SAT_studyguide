#!/usr/bin/python3

import pdfplumber

PATH = './sat-practice-test-1.pdf'

with pdfplumber.open(r'./sat-practice-test-1.pdf') as pdf:
    first_page = pdf.pages[39]
    #print(first_page.extract_text(x_tolerance =1, layout=True))
    #print(first_page.extract_words())

    # entire page dimensions (0,0,612,792)
    

    PAGE_DIM = {'default_reading':[(10, 30, 290, 750),(310, 30, 600, 750)],
                'first_reading':[(10, 300, 290, 750),(310, 300, 600, 750)],
                'end_reading':[(10, 30, 290, 650),(310, 30, 600, 650)],

                'default_writing':[(10, 30, 290, 750),(330, 30, 600, 750)],
                'first_writing':[(10, 410, 290, 750),(310, 410, 600, 750)],
                'end_writing':[(10, 30, 290, 650),(310, 30, 600, 650)]
                }
    
    
    print(first_page.within_bbox((PAGE_DIM['default_reading'])[0], relative = True).extract_text(x_tolerance =1, layout=True))