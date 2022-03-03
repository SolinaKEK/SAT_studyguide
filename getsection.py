#!/usr/bin/env python3

import pdfplumber
import re
# 0 , 0 , 612, 792
DIM = (0, 0, 612, 200)

with pdfplumber.open(r'tests/test1.pdf') as pdf:
    page = pdf.pages[3]
    string = page.within_bbox(DIM, relative = True).extract_text(x_tolerance =1, layout=True)
    
    print(string)
        #string = re.sub(r'[^(STOP)]*','',string)