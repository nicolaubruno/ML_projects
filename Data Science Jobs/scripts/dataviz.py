
#----- Libraries -----#

# Data and numerical libraries
import numpy as np
import pandas as pd

# System
from IPython.display import display_html

#----- Functions -----#

def display_side_by_side(*args, titles = None):
    """
        Display Pandas dataframes side-by-side

        Argumens:
        *args: Pandas dataframes
        titles: List with the title of each dataframe
    """

    html_str = ''

    for idx, df in enumerate(args):
        html_str += '<div style = "display: block; padding-right:20px; float: left;">'
        if type(titles) == list: html_str += '<p style = "text-align: center; font-weight: bold; font-size: 16px;">' + str(titles[idx]) + '</p>'
        html_str += df.to_html()
        html_str += '</div>'

    display_html(html_str, raw=True)
