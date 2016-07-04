# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 16:07:00
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-04 11:26:39

import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digpe.preprocessor import Preprocessor
from digpe.extractor import Extractor


class TestExtractorMethods(unittest.TestCase):
    def setUp(self):
        self.preprocessor = Preprocessor()
        self.extractor = Extractor()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_extract(self):
        with open(os.path.join(TEST_DATA_DIR, 'extracted_text'), 'wb') as f:
            for data in self.groundtruth_data:
                text = data['text']
                cleaned_text_list = self.preprocessor.preprocess(text)
                extracted_text_list = [self.extractor.extract(cleaned_text) for cleaned_text in cleaned_text_list]
                extracted_text = [val for sublist in extracted_text_list for val in sublist]  
                f.write('\n' + '#'*25)
                f.write('\n### cleaned ###\n')
                f.write(str(cleaned_text_list))
                f.write('\n### extraction ###\n')
                f.write(str(extracted_text))

    def test_extract_text(self):
        # text = 'no law enforcement in call 30 90 rose hh 180 rose call'
        # text = '30 min 150 rose 100 hr 200 rose just for 1 girl txt u outcall only'
        # text = '1 hour 120 rose \r'
        # text = 'tired of the c nt game the girl that complain well im not leaving until your sleeping in a c m stain incall $160 hh donation $260 hour donation outcall start at $280 donation cat'
        # text = 'young sweet n fun 23 year old middle eastern besuty in orange'
        text = '15 min $50'
        print self.extractor.extract(text)

        # ['15 min']
        # []
        # ['15 ', '$50']

        # ['30 min', ' 150 rose 100 hr']
        # ['30 min 150 rose', '100 hr 200 rose']

        # ['1 hour']
        # ['1 hour 120 rose']
        # ['1 ', ' 120 rose']
    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestExtractorMethods('test_extract'))
        # suite.addTest(TestExtractorMethods('test_extract_text'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()
