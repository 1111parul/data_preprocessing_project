import pandas as pd
from data_preprocessing.text_cleaner import TextCleaner

def test_text_cleaner():
    data = {'city': ['New York', 'Los Angeles', 'NY']}
    df = pd.DataFrame(data)
    text_cleaner = TextCleaner()
    transformed_df = text_cleaner.transform(df)
    assert transformed_df['city'][0] == 'new york'