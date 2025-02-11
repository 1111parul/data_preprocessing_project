import pandas as pd
from sklearn.impute import SimpleImputer
from data_preprocessing.date_parser import DateParser  # Changed to absolute import
# from data_preprocessing.text_cleaner import TextCleaner
from .text_cleaner import TextCleaner  # Relative import
 # Changed to absolute import

class Preprocessor:
    def __init__(self):
        self.date_parser = DateParser()
        self.text_cleaner = TextCleaner()

    def preprocess(self, df):
        # Date parsing
        self.date_parser.fit(df)
        df = self.date_parser.transform(df)

        # Text cleaning
        df = self.text_cleaner.transform(df)

        # Handle missing values
        num_cols = df.select_dtypes(include='number').columns
        cat_cols = df.select_dtypes(include='object').columns

        # Numerical imputation
        num_imputer = SimpleImputer(strategy='median')
        df[num_cols] = num_imputer.fit_transform(df[num_cols])

        # Categorical imputation
        cat_imputer = SimpleImputer(strategy='most_frequent', fill_value='missing')
        df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

        # Outlier handling using IQR
        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

        return df