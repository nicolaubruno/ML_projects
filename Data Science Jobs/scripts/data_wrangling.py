#
# Libraries
#

import numpy as np
import pandas as pd

from IPython.display import display_html

from sklearn.preprocessing import RobustScaler

#
# Functions
#

def read_dataset(filepath):
    """
        Read and clean CSV dataset from the jobseeker website ai-jobs
        https://ai-jobs.net/
    """

    # Getting dataframe (df) from the dataset
    df = pd.read_csv(filepath)

    # Getting only the relevant columns
    df = df[['job_title', 'experience_level']].sort_values('job_title')

    # Function to count a job vacancy in a specific experience level
    def count_exp_level(df, level):
        df = df.value_counts()

        if level in df.index: return df[level]
        else: return 0

    # Aggregate over job titles considering experience levels
    df = df.groupby('job_title').agg(
        EN = ('experience_level', lambda x: count_exp_level(x, 'EN')),
        MI = ('experience_level', lambda x: count_exp_level(x, 'MI')),
        SE = ('experience_level', lambda x: count_exp_level(x, 'SE'))
    )

    # Select jobs with at least 10 vacancies
    df = df.where(df.sum(axis = 1) >= 10).dropna().astype('int64')

    # Scale data
    scaled_df = pd.DataFrame(
            RobustScaler().fit_transform(df),
            index = df.index,
            columns = df.columns
        )

    return df, scaled_df

def display_side_by_side(*args, titles = None):
    """
        Display dataframes side-by-side
    """

    html_str = ''

    for idx, df in enumerate(args):
        html_str += '<div style = "display: block; padding-right:20px; float: left;">'
        if type(titles) == list: html_str += '<p style = "text-align: center; font-weight: bold; font-size: 16px;">' + str(titles[idx]) + '</p>'
        html_str += df.to_html()
        html_str += '</div>'

    display_html(html_str, raw=True)
