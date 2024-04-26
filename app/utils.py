import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def fetch_data_from_file(file):
    """
    Function to fetch data from a CSV or Excel file.
    Args:
        file (File): Uploaded CSV or Excel file.
    Returns:
        pd.DataFrame: DataFrame containing the data from the file.
    """
    if file is not None:
        # Check file type
        file_type = file.type.split("/")[1]

        if file_type == "csv":
            # Read CSV file
            data = pd.read_csv(file)
        elif file_type in ["xlsx", "xls"]:
            # Read Excel file
            data = pd.read_excel(file, engine="openpyxl")
        else:
            return None

        return data
    else:
        return None


def process_data(data):
    """
    Function to process sample data.
    Args:
        data (pd.DataFrame): DataFrame containing the data.
    Returns:
        tuple: Tuple containing total_sales, total_expenses, and profit.
    """
def plot_data(data):
    """
    Function to plot the uploaded data.
    Args:
        data (pd.DataFrame): DataFrame containing the data to be plotted.
    """
    if data is not None:
        st.write("### Data Preview:")
        st.write(data.head())

        st.write("### Sales and Expenses Over Time:")
        st.line_chart(data.set_index("Date")[["Sales", "Expenses"]])
    else:
        st.write("No data available. Please upload a CSV or Excel file.")


def plot_heatmap(df, title):
    """
    Function to plot a correlation heatmap.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        title (str): Title for the heatmap.
    """
    fig, ax = plt.subplots()
    sns.heatmap(df, annot=True, ax=ax)
    ax.set_title(title)
    return fig
