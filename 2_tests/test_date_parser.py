import pandas as pd
from data_preprocessing.date_parser import DateParser

def test_date_parser():
    data = {'purchase_date': ['2023-01-15', '2022-12-01', '2021-07-23']}
    df = pd.DataFrame(data)
    date_parser = DateParser()
    date_parser.fit(df)
    transformed_df = date_parser.transform(df)
    assert 'purchase_date_year' in transformed_df.columns
    assert 'purchase_date_month' in transformed_df.columns
    assert 'purchase_date_day' in transformed_df.columns