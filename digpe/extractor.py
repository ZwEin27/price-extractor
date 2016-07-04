# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-04 11:29:10


""" Patterns

# units? time
units? # time
time # units?

time: hh, hr...
unit: dollar, rose, candy...


"""
import re

class Extractor():

    re_digits = re.compile(r'\d+')


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
        'hf',
        'hr',
        'hour',
        'h',
        'qk',
        'qv',
        'q',
        'hummer',
        'minute',
        'min',
        '30',
        'ss',
        'second'
    ]

    time_unit_hour = [
        'hour',
        'hr',
        'h'
    ]

    time_unit_minute = [
        'minute',
        'min'
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

    reg_time_units = r'(?:'+ \
                r'(?:\d{1,3}[ ]?(?:' + r'|'.join(time_unit_hour+time_unit_minute) + r'))' + r'|' \
                r'(?:' + r'|'.join(time_units) + r')' \
                r')'
    # reg_time_units = r'15 min'

    # reg_time_units = [
    #     r'(?:\d{1,3}[ ]?(?:' + r'|'.join(time_unit_hour) + r'))',
    #     r'(?:\d{2}[ ]?(?:' + r'|'.join(time_unit_minute) + r'))'
    # ]
    #r'(?:\d{2}[ ]?(?:' + r'|'.join(time_unit_minute) + r')?)'


    reg_separator = r'[\t ]?'
    reg_price_digit = r'\d{1,4}'
    reg_price_unit = r'(?:'+ r'|'.join(price_units) + r'){0,2}' # \b
    reg_interval = r'\w{,30}'

    # patterns
    
    ## pattern for # time
    reg_price_time = r'(?:' + \
            reg_price_unit + \
            reg_separator + \
            reg_price_digit + \
            reg_separator + \
            reg_price_unit + \
            reg_separator + \
            r'(?:' + reg_separator + r'for' + reg_separator + r')?' + \
            reg_separator + \
            reg_time_units + \
            ')'
    re_price_time = re.compile(reg_price_time)
    # r'(?:=(?:[a-z]+[\t ]){,5}?|[\t ]?)' + \
    # r'(?:' + reg_separator + r'for' + reg_separator + r')?' + \


    

    ## pattern for time #
    reg_time_price = r'(?:' + \
            reg_time_units + \
            reg_separator + \
            reg_price_unit + \
            reg_separator + \
            reg_price_digit + \
            reg_separator + \
            reg_price_unit + \
            ')'
    re_time_price = re.compile(reg_time_price)
    
    ## pattern for price digits only
    reg_only_price = r'(?:' + \
            reg_price_unit + \
            reg_separator + \
            reg_price_digit + \
            reg_separator + \
            reg_price_unit + \
            ')'
    re_only_price = re.compile(reg_only_price)


    reg_combine = re.compile(r'(?:' + r'|'.join([reg_time_price, reg_price_time]) + r')')
    # print r'(?:' + r'|'.join([reg_time_price, reg_price_time, reg_only_price]) + r')'



    def __init__(self):
        pass

    def extract(self, text):
        # extractions = Extractor.reg_combine.findall(text)
        # return extractions
        # """
        text_pt_ext = Extractor.re_price_time.findall(text)
        text_tp_ext = Extractor.re_time_price.findall(text)
        text_op_ext = Extractor.re_only_price.findall(text)
        # return text_pt_ext
        # return text_tp_ext
        # return text_op_ext
        # text_dtp_ext = Extractor.re_dtime_price.findall(text)

        # if text_dtp_ext:
        #     return text_dtp_ext
        if len(text_pt_ext) > len(text_tp_ext):
            target = text_pt_ext
        elif len(text_pt_ext) < len(text_tp_ext):
            target = text_tp_ext
        else:
            pool = [text_tp_ext, text_pt_ext, text_op_ext]
            pool_max_len = [sum([len(item) for item in _]) for _ in pool]
            target = pool[pool_max_len.index(max(pool_max_len))]

        # add extra in differ formats
        extra = []
        target_digits = Extractor.re_digits.findall(' '.join(target))
        # print target_digits
        for op_ext in text_op_ext:
            for opd in Extractor.re_digits.findall(op_ext):
                if opd in target_digits:
                    break
                else:
                    extra.append(op_ext)
                    break
        target += extra
        return target
        # return text_op_ext

        # """
