#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np


class DataCleaner:
    """A class for holding data cleaning tools"""

    def __init__(self, df):
        self.df = df
        
    def clean_column_names(self):
        """
        Removes non-standard characters from column names
        """
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ', 
            '_').str.replace('(', '').str.replace(')', '').str.replace('/', '')
        
    def squared_feature(self, list):
        """
        For a cleaned feature column, creates a n^2 dependent features
        """
        for feature in list:
            self.df[feature + '_squared'] = self.df[feature] ** 2
        

    


