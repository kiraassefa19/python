import streamlit as st
import pandas as pd
import utils
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Basic EDA with Correlation Heatmaps & Plots", layout="wide"
    )

    # Add a sidebar for file upload
    st.sidebar.title("Upload CSV Files")
    files = [
        st.sidebar.file_uploader(f"Upload File {i}", type="csv") for i in range(1, 4)
    ]

    # Check if at least one file is uploaded
    if any(file is not None for file in files):
        # Load the data
        data = [utils.fetch_data_from_file(file) for file in files]

        # Show the first few rows of each dataset
        st.subheader("First Few Rows of Each Dataset")
        for i, df in enumerate(data):
            st.write(f"Dataset {i+1}:")
            st.write(df.head())

        # Show descriptive statistics
        st.subheader("Descriptive Statistics")
        for i, df in enumerate(data):
            st.write(f"Dataset {i+1}:")
            st.write(df.describe())

        # Show missing value information
        st.subheader("Missing Value Information")
        for i, df in enumerate(data):
            st.write(f"Dataset {i+1}:")
            st.write(df.isnull().sum())

        # Correlation Heatmaps
        st.subheader("Correlation Heatmaps")
        columns_of_interest = ["GHI", "DHI", "ModA", "ModB", "Tamb", "RH", "WS", "WD"]
        for i, df in enumerate(data):
            selected_cols = [col for col in columns_of_interest if col in df.columns]
            if len(selected_cols) > 1:  # Check if there are enough numeric columns
                corr_df = df[selected_cols].corr()
                fig = utils.plot_heatmap(corr_df, f"Dataset {i+1} Correlation Heatmap")
                st.pyplot(fig)  # Call st.pyplot to display the plot
            else:
                st.write(
                    f"Dataset {i+1} has insufficient numeric columns for a heatmap."
                )

        # Show scatter plots
        st.subheader("Scatter Plots")
        for i, df in enumerate(data):
            cols = st.multiselect(
                f"Select Columns for Scatter Plot (Dataset {i+1})",
                df.columns,
                key=f"scatter_{i}",
            )
            if len(cols) == 2:
                fig, ax = plt.subplots()
                ax.scatter(df[cols[0]], df[cols[1]])
                ax.set_xlabel(cols[0])
                ax.set_ylabel(cols[1])
                st.pyplot(fig)

        # Show histograms
        st.subheader("Histograms")
        for i, df in enumerate(data):
            cols = st.multiselect(
                f"Select Columns for Histogram (Dataset {i+1})",
                df.columns,
                key=f"histogram_{i}",
            )
            if len(cols) > 0:
                fig, axs = plt.subplots(
                    nrows=len(cols), ncols=1, figsize=(6, 4 * len(cols))
                )
                for j, col in enumerate(cols):
                    axs[j].hist(df[col], bins=20)
                    axs[j].set_title(col)
                st.pyplot(fig)

    else:
        st.warning("Please upload the CSV files to proceed.")


if __name__ == "__main__":
    main()
