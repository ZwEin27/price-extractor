# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 16:07:00
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 16:49:02

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
                cleaned_text = self.preprocessor.preprocess(text)
                extracted_text = self.extractor.extract(cleaned_text)
                f.write('\n' + '#'*25)
                # f.write('\n### cleaned ###\n')
                # f.write(str(cleaned_text))
                f.write('\n### extraction ###\n')
                f.write(str(extracted_text))

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestExtractorMethods('test_extract'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()