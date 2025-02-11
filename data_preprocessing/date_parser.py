import pandas as pd

class DateParser:
    """Parse date columns and create temporal features"""
    def __init__(self):
        self.date_columns = []

    def fit(self, X, y=None):
        self.date_columns = []
        for col in X.columns:
            try:
                pd.to_datetime(X[col], errors='raise')
                self.date_columns.append(col)
            except:
                pass
        return self

    def transform(self, X):
        """
        Transforms the input data by parsing date columns and creating temporal features.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed data with date columns parsed and temporal features added.
        """
        X = X.copy()
        for col in self.date_columns:
            X[col] = pd.to_datetime(X[col], errors='coerce')
            X[f'{col}_year'] = X[col].dt.year
            X[f'{col}_month'] = X[col].dt.month
            X[f'{col}_day'] = X[col].dt.day
        return X.drop(columns=self.date_columns)