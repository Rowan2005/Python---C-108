import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data1.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = True)

fig.show()