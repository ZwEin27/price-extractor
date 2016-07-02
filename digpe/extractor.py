# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 17:00:18


""" Patterns

# units? time
units? # time
time # units?

time: hh, hr...
unit: dollar, rose, candy...


"""


class Extractor():

    time_units = [
        'hh', 
        'ss',
        'hr',

    ]

    price_units = [
        'dollar',
        '$',
        'rose',
        'candy'
    ]


    def __init__(self):
        pass

    def extract(self, text):
        return text