import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def data_prep(material, cursor):
    df = data_fetch(material, cursor=cursor)
    clean_df = data_clean(df)
    return clean_df


def data_fetch(material, cursor):
    # Fetch data from server
    cursor.execute("SELECT posting_date, material_desc, material, bill_qty_sku FROM v_sales_2021 WHERE material=%s", (str(material),))
    data = cursor.fetchall()

    col = []
    for elt in cursor.description:
        col.append(elt[0])

    df = pd.DataFrame(data=data, columns=col)

    return df


def data_clean(df):
    clean_df = df
    # Cleaning up the data
    clean_df['date'] = pd.to_datetime(clean_df['posting_date'])
    clean_df['material'] = clean_df['material'].astype(np.int64)
    clean_df['sale_qty'] = clean_df['bill_qty_sku'].astype(np.int64)
    clean_df = clean_df.groupby(['material', 'date']).agg(
        {'sale_qty': 'sum', 'material': 'first', 'date': 'first', 'material_desc':'first'})
    clean_df = clean_df.reset_index(drop=True)

    return clean_df


def data_preprocess(df, material):
    clean_df = df
    # Tidying up the data
    prep_df = clean_df.loc[(df['material'] == material)].copy()
    prep_df = prep_df.set_index('date')
    prep_df = prep_df.drop(['material'], axis=1)
    prep_df = prep_df.resample('D').sum()
    prep_df = prep_df.fillna(0)

    # Scaling the data
    scaler = MinMaxScaler()
    scaler.fit(prep_df)
    scaled_df = scaler.transform(prep_df)

    return scaled_df, scaler


def actual_data(df, material):
    clean_df = df
    # Tidying up the data
    actual_df = df.loc[(df['material'] == material)].copy()
    actual_df = actual_df.set_index('date')
    actual_df = actual_df.drop(['material'], axis=1)
    actual_df = actual_df.resample('D').sum()
    actual_df = actual_df.fillna(0)

    return actual_df

