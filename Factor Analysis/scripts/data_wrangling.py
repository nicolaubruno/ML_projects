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
        # Columns to identify the same student in both datasets
        self.__common_cols = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]

        # Set Pandas DataFrames related to both datesets
        df = self.__load_df()

    # Get dataframe
    def get_df(self, subject = None, variables = None):
        df = self._df

        # Get information related to a specific subject
        #---
        if subject == 'mat':
            df = df[~df['G3_mat'].isnull()]

        return df

    # Build dataframe containing information from all datasets
    def __load_df(self):
        #----- Get all datasets -----#

        # Mathematics
        mat = pd.read_csv(
                'dataset/student-mat.csv',
                sep = ';'
            )

        # Portuguese
        por = pd.read_csv(
                'dataset/student-por.csv',
                sep = ';'
            )

        # Join dataframes
        self._df = pd.merge(mat, por, how = 'outer', left_on = self.__common_cols, right_on = self.__common_cols, suffixes = ('_mat', '_por'))
        self.__set_vars_type()

    # Set categorical variables
    def __set_vars_type(self):
        # Merged cols
        def merged_cols(cols):
            merged_cols = []

            for col in cols:
                if col in self.__common_cols:
                    merged_cols.append(col)

                else:
                    merged_cols.append(col + '_mat')
                    merged_cols.append(col + '_por')

            return merged_cols

        #----- Variables with standard category -----#

        cols = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian']
        self._df = self._df.astype({col:'category' for col in merged_cols(cols)})

        #----- Dichotomous variables -----#

        cols = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
        self._df = self._df.astype({col:'category' for col in merged_cols(cols)})

        #----- Likert scales -----#

        likert_scale_01 = pd.api.types.CategoricalDtype([i for i in range(5)], ordered = True)
        likert_scale_02 = pd.api.types.CategoricalDtype([i+1 for i in range(4)], ordered = True)
        likert_scale_03 = pd.api.types.CategoricalDtype([i+1 for i in range(5)], ordered = True)

        vars_likert_01 = ['Medu', 'Fedu']
        self._df = self._df.astype({var:likert_scale_01 for var in merged_cols(vars_likert_01)})

        vars_likert_02 = ['traveltime', 'studytime']
        self._df = self._df.astype({var:likert_scale_02 for var in merged_cols(vars_likert_02)})

        vars_likert_03 = ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
        self._df = self._df.astype({var:likert_scale_03 for var in merged_cols(vars_likert_03)})

        #----- Discrete numeric variables -----#

        cols = ['age', 'failures', 'absences']
        self._df = self._df.astype({col:'Int32' for col in merged_cols(cols)})

        #----- Continuous numeric variables -----#

        cols = ['G1', 'G2', 'G3']
        self._df = self._df.astype({col:'float32' for col in merged_cols(cols)})

    # Get only grades
    def get_grades(self, subject = None):
        # Mathematics
        if subject == 'mat' or subject == 'por':
            df = self.get_df(subject, 'numerical')[['G1', 'G2', 'G3']].astype('float32')

        # All subjects
        elif subject == 'both':
            mat_df = self.get_df('mat', 'numerical')[['G1', 'G2', 'G3']].astype('float32')
            por_df = self.get_df('mat', 'numerical')[['G1', 'G2', 'G3']].astype('float32')

            df = pd.merge(mat_df, por_df)

        return df
