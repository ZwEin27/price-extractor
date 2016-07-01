# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-01 16:02:51


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digpe.preprocessor import Preprocessor


class TestPreprocessorMethods(unittest.TestCase):
    def setUp(self):
        self.preprocessor = Preprocessor()
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_preprocess(self):
        with open(os.path.join(TEST_DATA_DIR, 'preprocessed_text'), 'wb') as f:
            for data in self.groundtruth_data:
                text = data['text']
                cleaned_text = self.preprocessor.preprocess(text)
                f.write('\n' + '#'*25)
                # f.write('\n### original ###\n')
                # f.write(text.encode('ascii', 'ignore'))
                f.write('\n### clean ###\n')
                f.write(str(cleaned_text))

        


if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestPreprocessorMethods('test_preprocess'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

