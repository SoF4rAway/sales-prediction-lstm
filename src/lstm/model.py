import os
import tensorflow as tf
from tensorflow import keras
from keras import models
import numpy as np
import pandas as pd
from lstm.data_prep import data_prep, data_preprocess, actual_data


def model(material_num, cursor):
    df = data_prep(material_num, cursor=cursor)
    data, scaler = data_preprocess(df, material_num)  # Add material_num for feed the model
    model = models.load_model("E:/Program/PKLProjekt/ML/model.h5")

    # Prediction for data_1
    pred = []
    pred_batch = data[-30:]
    current_batch = pred_batch.reshape((1, 30, 1))
    for i in range(10):
        current_pred = model.predict(current_batch)[0]
        pred.append(current_pred)
        current_batch = np.append(current_batch[:, 1:, :], [[current_pred]], axis=1)

    # Rescaling of predicted value
    true_pred = scaler.inverse_transform(pred)

    # Saving the predicted value to a DataFrame and arrange the date then set it as index
    pred_df = pd.DataFrame()
    pred_df['date'] = pd.date_range(start='2021-06-01', periods=10, freq='D')
    pred_df = pred_df.set_index('date')
    pred_df['sale_qty'] = true_pred.astype(np.int64)
    pred_df = pred_df.reset_index()

    actual_df = actual_data(df, material_num)
    actual_df = actual_df.reset_index()
    material_desc = df['material_desc'][0]

    return pred_df, actual_df, material_desc



