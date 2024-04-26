import unittest
import pandas as pd
from data_cleaning import drop_comments_column, remove_negative_values


class TestDataCleaning(unittest.TestCase):
    def test_drop_comments_column(self):
        # Test dropping the 'Comments' column
        df = pd.DataFrame({"A": [1, 2, 3], "Comments": [None, None, None]})
        cleaned_df = drop_comments_column(df)
        self.assertNotIn("Comments", cleaned_df.columns)

    def test_remove_negative_values(self):
        # Test removing negative values from the 'GHI' column
        df = pd.DataFrame({"GHI": [1, -2, 3]})
        cleaned_df = remove_negative_values(df)
        self.assertTrue((cleaned_df["GHI"] >= 0).all())

    # Add more test cases for other data cleaning functions


if __name__ == "__main__":
    unittest.main()
