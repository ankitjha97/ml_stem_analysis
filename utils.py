import pandas as pd
import numpy as np
from sklearn.metrics import mutual_info_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_auc_score
def read_data():
    df = pd.read_excel("2010 Federal STEM Education Inventory Data Set.xls", skiprows = 1)
    rows = 253
    cols = 256
    print(df.shape)
    if(rows == df.shape[0] and cols == df.shape[1]):
        return True
    else:
        return False

def check_numeric_data(data):
    for dtype in data.dtypes:
        if(dtype == 'object'):
            return False
    return True

def check_shape(X_train, y_train):
    if(X_train.shape[0] != y_train.shape[0]):
        return False
    return True

def train_data(df):
    if(df.shape > df.dropna().shape):
        return False
    return True
