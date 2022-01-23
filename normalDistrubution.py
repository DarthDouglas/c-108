import pandas as pa
import plotly.express as pe
import plotly.figure_factory as ff
import csv

df=pa.read_csv("C:\Users\Ezra\Desktop\Python\py\Phone.csv")
fig=ff.create_distplot([df["Sr.No,Mobile Brand"].tolist()],["Avg Rating"],show_hist=False)
fig.show()