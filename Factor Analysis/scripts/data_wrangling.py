# Libraries
import numpy as np
import pandas as pd

class Dataset():
    # Attributes
    #---

    # DataFrame related to both subjects
    @property
    def df(self):
        return self._df

    # DataFrame related to the mathematics subject
    @property
    def df_mat(self):
        return self._df_mat

    # DataFrame related to the Portuguese language subject
    @property
    def df_por(self):
        return self._df_por

    # Methods
    #---

    # Constructor
    def __init__(self):
        # Columns to identify the same student in both datasets
        self.__common_cols = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]

        # Set Pandas DataFrames related to both datesets
        df = self.__load_df()

    # Get dataframe
    def get_df(self, subject = None, dtype = None):
        # Select subjects
        #---

        # Mathematics
        if subject == 'mat':
            df = self.df_mat

        # Portuguese language
        elif subject == 'por':
            df = self.df_por

        # Both
        else:
            df = self.df

        # Select variables type
        #---

        # Float
        if dtype == 'float':
            df = df.select_dtypes(include = 'float32')

        elif dtype == 'int':
            df = df.select_dtypes(include = 'Int32')

        elif dtype == 'category':
            df = df.select_dtypes(include = 'category')

        return df

    # Build dataframe containing information from all datasets
    def __load_df(self):
        #----- Get all datasets -----#

        # Mathematics
        self._df_mat = pd.read_csv(
                'dataset/student-mat.csv',
                sep = ';'
            )

        # Portuguese
        self._df_por = pd.read_csv(
                'dataset/student-por.csv',
                sep = ';'
            )

        # Both subjects
        self._df = pd.merge(self.df_mat, self.df_por, how = 'inner', left_on = self.__common_cols, right_on = self.__common_cols, suffixes = ('_mat', '_por'))

        # Set variables type
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
        self._df_mat = self._df_mat.astype({col:'category' for col in cols})
        self._df_por = self._df_por.astype({col:'category' for col in cols})

        #----- Dichotomous variables -----#

        cols = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
        self._df = self._df.astype({col:'category' for col in merged_cols(cols)})
        self._df_mat = self._df_mat.astype({col:'category' for col in cols})
        self._df_por = self._df_por.astype({col:'category' for col in cols})

        #----- Likert scales -----#

        likert_scale_01 = pd.api.types.CategoricalDtype([i for i in range(5)], ordered = True)
        likert_scale_02 = pd.api.types.CategoricalDtype([i+1 for i in range(4)], ordered = True)
        likert_scale_03 = pd.api.types.CategoricalDtype([i+1 for i in range(5)], ordered = True)

        vars_likert_01 = ['Medu', 'Fedu']
        self._df = self._df.astype({var:likert_scale_01 for var in merged_cols(vars_likert_01)})
        self._df_mat = self._df_mat.astype({col:likert_scale_01 for col in vars_likert_01})
        self._df_por = self._df_por.astype({col:likert_scale_01 for col in vars_likert_01})

        vars_likert_02 = ['traveltime', 'studytime']
        self._df = self._df.astype({var:likert_scale_02 for var in merged_cols(vars_likert_02)})
        self._df_mat = self._df_mat.astype({col:likert_scale_02 for col in vars_likert_02})
        self._df_por = self._df_por.astype({col:likert_scale_02 for col in vars_likert_02})

        vars_likert_03 = ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
        self._df = self._df.astype({var:likert_scale_03 for var in merged_cols(vars_likert_03)})
        self._df_mat = self._df_mat.astype({col:likert_scale_03 for col in vars_likert_03})
        self._df_por = self._df_por.astype({col:likert_scale_03 for col in vars_likert_03})

        #----- Discrete numeric variables -----#

        cols = ['age', 'failures', 'absences']
        self._df = self._df.astype({col:'Int32' for col in merged_cols(cols)})
        self._df_mat = self._df_mat.astype({col:'Int32' for col in cols})
        self._df_por = self._df_por.astype({col:'Int32' for col in cols})

        #----- Continuous numeric variables -----#

        cols = ['G1', 'G2', 'G3']
        self._df = self._df.astype({col:'float32' for col in merged_cols(cols)})
        self._df_mat = self._df_mat.astype({col:'float32' for col in cols})
        self._df_por = self._df_por.astype({col:'float32' for col in cols})
