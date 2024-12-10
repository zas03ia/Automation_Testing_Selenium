import os


def save_to_excel(dataframe, filename: str):
    """
    Saves a Pandas DataFrame to an Excel file.
    """

    filepath = os.path.join("test_results", filename)
    dataframe.to_excel(filepath, index=False)
