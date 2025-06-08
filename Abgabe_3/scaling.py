import numpy as np
import pandas as pd

def scale_series(numeric: pd.Series, new_mean: float=None, new_std: float=None) -> pd.Series:
    orig_mean = numeric.mean()
    orig_std = numeric.std()

    if new_mean is None and new_std is None:
        return numeric.copy()
    
    if len(numeric) == 1:
        if new_mean is None:
            return pd.Series([numeric.iloc[0]])
        else:
            return pd.Series([new_mean])

    standardized = (numeric - orig_mean) / orig_std

    if new_std is not None:
        standardized *= new_std

    if new_mean is not None:
        standardized += new_mean

    return standardized

s = pd.Series(np.random.rand(100))
new_s = scale_series(s, new_mean=10.0)
print(new_s)