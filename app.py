import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("final_sales.csv")

#convert data column to datetime (important for sorting)
df["Date"] = pd.to_datetime(df["Date"])

#sort by date
df = df.sort_values("Date")

#Dash app
app = Dash(__name__, use_pages=False)


app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods - Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#B83280", "fontFamily": "Arial"}
        ),

        html.Div([
            html.Label(
                "Select Region:",
                style={"marginRight": "10px", "fontWeight": "bold"}
            ),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "South", "value": "south"},
                    {"label": "East", "value": "east"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True,
                style={"marginTop": "10px"}
            ),
        ],
        style={
            "padding": "15px",
            "margin": "20px",
            "border": "2px solid #ddd",
            "borderRadius": "10px",
            "backgroundColor": "#fafafa"
        }),

        dcc.Graph(id="sales-graph")
    ],
    style={"maxWidth": "1000px", "margin": "0 auto"}
)

# Callback to update line chart
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    # Filter region
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Sales": "Sales ($)", "Date": "Date"},
        template="plotly"
    )

    fig.update_layout(
        plot_bgcolor="#f0f0f0",
        paper_bgcolor="#ffffff",
        title_x=0.5,
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
