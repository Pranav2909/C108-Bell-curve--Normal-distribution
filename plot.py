import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
plot = ff.create_distplot([df["Height(Inches)"].tolist()],["Data"] ,show_hist = False)
plot.show()