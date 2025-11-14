import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("final_sales.csv")

#convert data column to datetime (important for sorting)
df["Date"] = pd.to_datetime(df["Date"])

#sort by date
df = df.sort_values("Date")

#create line chart
fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)",
)

#Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods - Pink Morsel Sales Dashboard"),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
    