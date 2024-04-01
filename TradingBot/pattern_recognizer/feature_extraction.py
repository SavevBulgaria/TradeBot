import pandas as pd
import numpy as np

def extract_features(data: pd.DataFrame, lags: int = 5) -> pd.DataFrame:
    """
    Extract features from the data.

    Parameters
    ----------
    data : pd.DataFrame
        The input data.
    lags : int, optional
        The number of lags to use for feature extraction.

    Returns
    -------
    pd.DataFrame
        A new dataframe with the extracted features.
    """
    # Add a column of 1s to the dataframe
    data['const'] = 1

    # Add a column of the log returns of the closing price
    data['log_return'] = np.log(data['Close'] / data['Close'].shift(1))

    # Add a column of the moving averages
    for lag in range(1, lags + 1):
        data[f'ma_{lag}'] = data['Close'].rolling(window=lag).mean()

    # Add a column of the moving standard deviations
    for lag in range(1, lags + 1):
        data[f'std_{lag}'] = data['Close'].rolling(window=lag).std()

    # Drop the rows with missing values
    data.dropna(inplace=True)

    return data