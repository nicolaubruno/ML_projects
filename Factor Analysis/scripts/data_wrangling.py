# Libraries
import numpy as np
import pandas as pd

class Dataset():
    # Attributes
    #---

    # Pandas DataFrame related to the all datasets
    @property
    def df(self):
        return self._df

    # Methods
    #---

    # Constructor
    def __init__(self):
        # Set Pandas DataFrame
        self.__set_df()

        self._df


    # Get dataframe
    def get_df(self, subject = None, variables = None):
        # Complete DataFrame
        df = self.df

        # Check subject
        #---
        if subject == 'mat':
            df = self._df.where(df['subject'] == 'mat').dropna().drop(columns = ['subject'])

        elif subject == 'por':
            df = self._df.where(df['subject'] == 'por').dropna().drop(columns = ['subject'])

        # Check variables type
        #---
        if variables == 'categorical':
            df = df.select_dtypes(exclude = 'number')

        elif variables == 'numerical':
            df = df.select_dtypes(include = 'number')

        return df


    # Set a single Pandas DataFrame for all datasets
    def __set_df(self):
        # Get dataset related to the mathematics subject
        mat = pd.read_csv(
                'dataset/student-mat.csv',
                sep = ';'
            )

        mat['subject'] = 'mat'

        # Get dataset related to the Portuguese language subject
        por = pd.read_csv(
                'dataset/student-por.csv',
                sep = ';'
            )

        por['subject'] = 'por'

        # Join dataframes
        self._df = pd.concat([mat, por]).dropna()

        # Set categorical variables
        self.__set_cat_vars()

    # Set categorical variables
    def __set_cat_vars(self):
        # Variables with standard category
        std_cat_vars = [
                'school',
                'sex',
                'address',
                'famsize',
                'Pstatus',
                'Mjob',
                'Fjob',
                'reason',
                'guardian',
                'subject'
            ]

        self._df = self._df.astype({var:'category' for var in std_cat_vars})

        # Dichotomous variables
        dichotomous_vars = [
                'schoolsup',
                'famsup',
                'paid',
                'activities',
                'nursery',
                'higher',
                'internet',
                'romantic'
            ]

        self._df = self._df.astype({var:'category' for var in dichotomous_vars})

        # Likert scales
        likert_scale_01 = pd.api.types.CategoricalDtype([i for i in range(5)], ordered = True)
        likert_scale_02 = pd.api.types.CategoricalDtype([i+1 for i in range(4)], ordered = True)
        likert_scale_03 = pd.api.types.CategoricalDtype([i+1 for i in range(5)], ordered = True)

        vars_likert_01 = [
                'Medu',
                'Fedu'
            ]

        self._df = self._df.astype({var:likert_scale_01 for var in vars_likert_01})

        vars_likert_02 = [
                'traveltime',
                'studytime'
            ]

        self._df = self._df.astype({var:likert_scale_02 for var in vars_likert_02})

        vars_likert_03 = [
                'famrel',
                'freetime',
                'goout',
                'Dalc',
                'Walc',
                'health'
            ]

        self._df = self._df.astype({var:likert_scale_03 for var in vars_likert_03})
