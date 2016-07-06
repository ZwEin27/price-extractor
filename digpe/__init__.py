# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 11:29:35
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-05 20:23:53

from digpe.preprocessor import Preprocessor
from digpe.extractor import Extractor
from digpe.normalizer import Normalizer


class DIGPE():

    def __init__(self):
        self.preprocessor = Preprocessor()
        self.extractor = Extractor()
        self.normalizer = Normalizer()


    def extract(self, text):
        cleaned_text_list = self.preprocessor.preprocess(text)
        extracted_text_list = self.extractor.extract_from_list(cleaned_text_list)
        normalized_text_list = self.normalizer.normalize_from_list(extracted_text_list)

        ans = []
        for normalized in normalized_text_list:
            if not normalized['time_unit'] or normalized['time_unit'] == '' or normalized['time_unit'] in UNIT_TIME_HOUR:
                ans.append(normalized)
        return ans


    def extract_from_list(self, text_list):
        return [self.extract(text) for text in text_list]


