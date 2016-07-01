# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:34
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 16:02:26

import re

class Preprocessor():
    def __init__(self):
        pass

    re_space = re.compile(r'\s')
    re_digits = re.compile(r'\d')
    re_single_space = re.compile(r'(?:(?<=[ \t])[ \t]+|(?<=[\A\n])[ \t]+|[ \t]+(?=[\Z\n]))')

    
    
    # punctuations
    # !"#%&\'()*+,-./:;<=>?@[\]^_`{|}~
    reg_punctuation = r'(?:[!"#%&\'()*+,-./:;<=>?@[\]^_`{|}~])'


    irr_units = [
        r'lb',
        r'c',
    ]
    reg_irr_units = r'(?:\b\d{1,2}\'\d{1,2}\b|\d+(' + r'|'.join(irr_units) + '))'      # 5'9/160lb/36C


    # remove irrelated
    irrelation_regex_list = [
        r'(?:(?<=\d)\.00\b)',               # $160.00 => $160
        r'(?:\d{4,}\.)',                  # 925354849.80 => 80
        r'(?:\d{4,}[a-z]+\d{4,}\.)',      # 92535l4849.80 => 80
        r'(?:\d+[ \t]*%)',                  # 1000%
        reg_irr_units,
        reg_punctuation
    ]
    re_irrelation = re.compile(r'|'.join(irrelation_regex_list))



    # phone numbers
    reg_phone_number = [
        r'(?:\d{7,})',
        r'(?:\d{8}[ ]\d{3})',
        r'(?:\d{7}[ ]\d{4})',
        r'(?:\d{5}[ ]\d{4}[ ]\d{4})',
        r'(?:\d{5}[ ]\d{4}[ ]\d{2}[ ]\d{2})',
        r'(?:\d{4}[ ]\d{4}[ ]\d{2})',
        r'(?:\d{4}[ ]\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2})',
        r'(?:\d{4}[ ]\d{3}[ ]\d{3})',
        r'(?:\d{3}[ ]\d{7,8})',
        r'(?:\d{3}[ ]\d{4}[ ]\d{4})',
        r'(?:\d{3}[ ]\d{4}[ ]\d{3})',
        r'(?:\d{3}[ ]\d{3}[ ]\d{4})',
        r'(?:\d{3}[ ]\d{3}[ ]\d{3}[ ]\d{1})',
        r'(?:\d{3}[ ]\d{3}[ ]\d{2}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{3}[ ]\d{3}[ ]\d{1}[ ]\d{3})',
        r'(?:\d{3}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{4})',
        r'(?:\d{2}[ ]\d{8,10})',
        r'(?:\d{2}[ ]\d{4}[ ]\d{4})',
        r'(?:\d{2}[ ]\d{1}[ ]\d{8}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{3}[ ]\d{3}[ ]\d{3})',
        r'(?:\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2})',
        r'(?:\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1})'
    ]
    re_phone_number = re.compile(r'|'.join(reg_phone_number))
    
    


    def preprocess(self, text):
        text = text.encode('ascii', 'ignore').lower()
        text = Preprocessor.re_irrelation.sub(' ', text)
        text = Preprocessor.re_single_space.sub('', text)
        text = Preprocessor.re_phone_number.sub('', text)



        return text.split('\n') # future find all instead

