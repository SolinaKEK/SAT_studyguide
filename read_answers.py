#!/opt/homebrew/bin/python3

import sys
import pdfplumber

PATH = 'scoring-sat-practice-test-1.pdf'

with pdfplumber.open(r'scoring-sat-practice-test-1.pdf') as pdf:
    
    page_num = 5 # answers are always on page 5 of pdf
    page = pdf.pages[page_num]

    # add ANSWERPG_DIMS to config.py
    ANSWERPG_DIMS = {'reading_dim': (10, 30, 300, 350),
                     'writing_dim': (310, 30, 600, 350),
                     'math_nocalc_dim': (10, 350, 200, 650),
                     'math_calc_dim': (210, 350, 600, 650)
                    }
    # entire page dimensions (0,0,612,792)  
    

    print(page.within_bbox(ANSWERPG_DIMS['math_calc_dim'], relative = True).extract_text(x_tolerance =1, layout=True))