from typing import Tuple
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def split_data(df: pd.DataFrame, split_size: float) -> Tuple[MinMaxScaler, pd.DataFrame, pd.DataFrame]:
    mms = MinMaxScaler()
    timestamp_threshold = df.index[round(len(df) * split_size)]

    train_data = df[:timestamp_threshold]
    test_data = df[timestamp_threshold:]

    return mms, mms.fit_transform(train_data), mms.fit_transform(test_data)

def create_sequence(array, input_sequence: int) -> Tuple[np.array, np.array]:
    sequences = []
    labels = []
    data_length = len(array)

    for i in range(data_length - input_sequence):
        row = [a for a in array[i:i + input_sequence]]
        sequences.append(row)
        labels.append(array[i + input_sequence])

    return np.array(sequences), np.array(labels)