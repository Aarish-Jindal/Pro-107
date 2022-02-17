import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("App Data.csv")

x = df.groupby("level")["attempt"].mean()
print(x)

fig = go.Figure(go.Bar(x = x, y = ['level 1', 'level 2','level 3','level 4'],orientation = 'h'))
fig.show()