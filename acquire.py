from zgulde.ds_imports import *


def get_data():
    df = (
        pd.read_csv("./data.csv")
        .cleanup_column_names()
        .rename(columns={"measure": "crossing_method"})
    )
    df.date = pd.to_datetime(df.date)
    canada = df[df.border == "US-Canada Border"]
    mexico = df[df.border == "US-Mexico Border"]
    return canada, mexico
