import pandas as pd
import numpy as np


def drop_comments_column(df):
    # Drop the 'Comments' column
    cleaned_df = df.drop(columns=["Comments"])
    return cleaned_df


def remove_negative_values(df):
    # Remove rows with negative values in the 'GHI' column
    cleaned_df = df[df["GHI"] >= 0]
    return cleaned_df


# # 1. Handling Missing Values
# # Drop the 'Comments' column
# df_cleaned = df.drop(columns=["Comments"])

# # 2. Dealing with Negative Values
# # Remove rows with negative values in the 'GHI' column
# df_cleaned = df_cleaned[df_cleaned["GHI"] >= 0]

# # 3. Data Transformation
# # Convert the 'Timestamp' column to datetime format
# df_cleaned["Timestamp"] = pd.to_datetime(df_cleaned["Timestamp"])

# # Display the cleaned DataFrame
# print("Cleaned DataFrame:")
# print(df_cleaned.head())

# # Summary statistics after cleaning
# print("\nSummary Statistics after Cleaning:")
# print(df_cleaned.describe())

# # Check for missing values after cleaning
# print("\nMissing Values after Cleaning:")
# print(df_cleaned.isnull().sum())