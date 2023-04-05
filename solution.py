import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 425154307 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return  loc *np.sqrt(chi2.ppf(alpha / 2, 1)/(27*2)), \
           loc *np.sqrt(chi2.ppf(1 - alpha / 2, 1)/(27*2))
