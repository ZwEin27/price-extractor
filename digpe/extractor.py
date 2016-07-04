# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-03 21:12:46


""" Patterns

# units? time
units? # time
time # units?

time: hh, hr...
unit: dollar, rose, candy...


"""
import re

class Extractor():


    time_units = [
        'hourly',
        'half hour',
        'half hr',
        'half',
        'hlf hr',
        'hlf hour',
        'hf hr',
        'h hour',
        'h hr',
        'h h',
        'full hour',
        'full hr',
        'f hour',
        'f hr',
        'f h',
        'fh',
        'hhr',
        'hh',
        'hr',
        'hour',
        'h',
        'q',
        'qk',
        'qv',
        'hummer',
        'min',
        'minute',
        'ss',
        'second'
    ]

    price_units = [
        '\$',
        'dollar',
        'euro',
        'nuck',
        'rose',
        'candy',
        'donation'
    ]


    # patterns
    
    ## pattern for # time
    reg_price_time_digit = r'\d{1,4}'
    reg_price_time_interval = r'\w{,10}'
    reg_price_time_price_units = r'(?:'+ r'|'.join(price_units) + r')?'
    reg_price_time = r'(?:' + \
            reg_price_time_price_units + \
            reg_price_time_interval + \
            reg_price_time_digit + \
            reg_price_time_interval + \
            reg_price_time_price_units + \
            r'[\t ]?' + \
            r'(?:'+ r'|'.join(time_units) + r')' + \
            ')'
    re_price_time = re.compile(reg_price_time)


    ## pattern for # time
    reg_time_price_digit = r'\d{1,4}'
    reg_time_price_interval = r'\w{,10}'
    reg_time_price_price_units = r'(?:'+ r'|'.join(price_units) + r')?'
    reg_time_price = r'(?:' + \
            r'\d{0,2}' \
            r'[\t ]?' + \
            r'(?:'+ r'|'.join(time_units) + r')' + \
            r'[\t ]?' + \
            reg_time_price_price_units + \
            reg_time_price_digit + \
            reg_time_price_price_units + \
            ')'
    re_time_price = re.compile(reg_time_price)


    def __init__(self):
        pass

    def extract(self, text): 
        text_pt_ext = Extractor.re_price_time.findall(text)
        text_tp_ext = Extractor.re_time_price.findall(text)
        if len(text_pt_ext) > len(text_tp_ext):
            return text_pt_ext
        elif len(text_pt_ext) < len(text_tp_ext):
            return text_tp_ext
        else:
            return text_pt_ext