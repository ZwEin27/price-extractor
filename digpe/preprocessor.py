# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:34
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 14:06:27

import re

class Preprocessor():
    def __init__(self):
        pass


    # remove irrelated

    # punctuations
    reg_punctuation = r'(?:[!"#%&\'()*+,-./:;<=>?@[\]^_`{|}~])'


    irrelation_regex_list = [
        r'(?<=\d)\.\d+(?=[\w\s])', # $160.00 => $160
        reg_punctuation
    ]
    re_irrelation = re.compile(r'|'.join(irrelation_regex_list))


    def preprocess(self, text):
        text = text.encode('ascii', 'ignore').lower()
        text = Preprocessor.re_irrelation.sub('', text)


        return text.split('\n') # future find all instead