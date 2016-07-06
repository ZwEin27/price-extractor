# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 16:07:00
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-04 18:31:38

import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digpe.preprocessor import Preprocessor
from digpe.extractor import Extractor
from digpe.normalizer import Normalizer


class TestExtractorMethods(unittest.TestCase):
    def setUp(self):
        self.preprocessor = Preprocessor()
        self.extractor = Extractor()
        self.normalizer = Normalizer()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_normalize(self):
        with open(os.path.join(TEST_DATA_DIR, 'normalized_text'), 'wb') as f:
            for data in self.groundtruth_data:
                text = data['text']
                cleaned_text_list = self.preprocessor.preprocess(text)
                extracted_text_list = self.extractor.extract_from_list(cleaned_text_list)
                normalized_text_list = self.normalizer.normalize_from_list(extracted_text_list)
                f.write('\n' + '#'*25)
                f.write('\n### original ###\n')
                f.write(text.encode('ascii', 'ignore'))
                f.write('\n### cleaned ###\n')
                f.write(str(cleaned_text_list))
                f.write('\n### extracted ###\n')
                f.write(str(extracted_text_list))
                f.write('\n### normalized ###\n')
                f.write(str(normalized_text_list))

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestExtractorMethods('test_normalize'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()
