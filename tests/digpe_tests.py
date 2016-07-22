# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-22 17:43:44


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digpe import DIGPE

def cmp_json_obj(json_obj1, json_obj2):
    if json_obj1['price'] != json_obj2['price']:
        return False
    if json_obj1['price_unit'] != json_obj2['price_unit']:
        return False
    if json_obj1['time_unit'] != json_obj2['time_unit']:
        return False
    return True


def cmp_digpe_ext(ext1, ext2):
    ext1_len = len(ext1)
    ext2_len = len(ext2)
    if ext1_len != ext2_len:
        return False
    
    for i in range(ext1_len):
        if not cmp_json_obj(ext1[i], ext2[i]):
            return False
    return True


class TestDIGPEMethods(unittest.TestCase):
    def setUp(self):
        self.digpe = DIGPE()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_digpe(self):
        total = 0
        correct = 0
        for data in self.groundtruth_data:
            text = data['text']
            ext_gt = data['extraction']
            ext_pd = self.digpe.extract(text)
            
            if cmp_digpe_ext(ext_gt, ext_pd):
                correct += 1
            else:
                print '#'*50
                print '### original ###'
                print text.encode('ascii','ignore')
                print '### groundtruth data ###'
                print ext_gt
                print '### extracted data ###'
                print ext_pd

            total += 1
        print 60*'-'
        print 'pass', correct, 'out of', total
            
            




if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestDIGPEMethods('test_digpe'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

