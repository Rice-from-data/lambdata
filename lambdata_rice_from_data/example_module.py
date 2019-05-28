#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np


def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '')
    return df

def squared_feature(df,list):
    for feature in list:
        df[feature + '_squared'] = df[feature] ** 2
    return df

