import pandas as pd
from data_preprocessing.preprocessor import Preprocessor

def test_preprocessor():
    data = {
        'age': [25, 30, 35, None, 40, 150, 45],
        'salary': [50000, 60000, None, 70000, 80000, 90000, 1000000],
        'gender': ['M', 'F', 'F', 'M', None, 'F', 'M'],
        'city': ['New York', 'Los Angeles', 'NY', 'LA', 'NYC', 'San Fran', ''],
        'purchase_date': ['2023-01-15', '2022-13-01', '2021-07-23',
                        'invalid', '2020-05-12', None, '2023-03-30']
    }
    df = pd.DataFrame(data)
    preprocessor = Preprocessor()
    transformed_df = preprocessor.preprocess(df)
    assert transformed_df.isnull().sum().sum() == 0