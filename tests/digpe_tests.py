# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 13:13:14


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digpe import DIGPE





class TestDIGPEMethods(unittest.TestCase):
    def setUp(self):
        self.price_extractor = DIGPE()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_cleaner(self):
        with open(os.path.join(TEST_DATA_DIR, 'cleaned_text'), 'wb') as f:
            for data in self.groundtruth_data:
                text = data['text']
                cleaned_text = self.price_extractor.clean(text)
                f.write('#'*25 + '\n')
                f.write('\n### original ###\n')
                f.write(text)
                f.write('\n### clean ###\n')
                f.write(cleaned_text)


    def test_extractor(self):
        for data in self.groundtruth_data:
            text = data['text']
            extraction = data['extraction']
            self.price_extractor.extract(text)


    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        # suite.addTest(TestDIGPEMethods("test_cleaner"))
        # suite.addTest(TestDIGPEMethods("test_extractor"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

