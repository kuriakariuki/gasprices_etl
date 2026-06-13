import pandas as pd

def transform_gasprices(data):
    df = data.rename(columns= {"name":"cities"})
    df= data.drop(columns=["lowername"])

    return df