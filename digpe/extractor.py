# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-03 11:20:52


""" Patterns

# units? time
units? # time
time # units?

time: hh, hr...
unit: dollar, rose, candy...


"""


class Extractor():


    time_units = [
        'half',
        'hlf',
        'h',
        'hh',
        'hr',
        'hhr',
        'h hr',
        'fh',
        'hour',
        'hourly' 
        'q',
        'qk',
        'qv',
        'hmu',
        'hummer',
        'min',
        'minute',
        'ss',
        'second'
    ]

    price_units = [
        'dollar',
        '$',
        'rose',
        'candy',
        'nuck',
        'euro',
        'donation'
    ]


    def __init__(self):
        pass

    def extract(self, text):
        return text