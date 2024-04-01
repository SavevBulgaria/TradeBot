from sklearn.metrics import mean_squared_error

def evaluate_model(model, X: pd.DataFrame, y: pd.Series) -> float:
    """
    Evaluate the performance of the trained model.

    Parameters
    ----------
    model : LinearRegression
        The trained linear regression model.
    X : pd.DataFrame
        The input data.
    y : pd.Series
        The target variable.

    Returns
    -------
    float
        The mean squared error of the model.
    """
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)

    return mse