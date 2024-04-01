from sklearn.linear_model import LinearRegression

def train_model(X: pd.DataFrame, y: pd.Series) -> LinearRegression:
    """
    Train a linear regression model.

    Parameters
    ----------
    X : pd.DataFrame
        The input data.
    y : pd.Series
        The target variable.

    Returns
    -------
    LinearRegression
        The trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X, y)

    return model