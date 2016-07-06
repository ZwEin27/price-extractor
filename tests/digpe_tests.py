# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-05 20:20:05


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth


class TestDIGPEMethods(unittest.TestCase):
    def setUp(self):
        self.preprocessor = Preprocessor()
        self.extractor = Extractor()
        self.normalizer = Normalizer()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_digpe(self):
        for data in self.groundtruth_data:
            text = data['text']
            cleaned_text_list = self.preprocessor.preprocess(text)
            extracted_text_list = self.extractor.extract_from_list(cleaned_text_list)
            normalized_text_list = self.normalizer.normalize_from_list(extracted_text_list)




if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestDIGPEMethods('test_digpe'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

