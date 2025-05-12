import plotly.graph_objects as go

def create_location_outlines(df):
    outlines = []
    for _, row in df.iterrows():
        h = row["height"]
        w = row["width"]
        x0 = row["x"] - h / 2
        x1 = row["x"] + h / 2
        y0 = row["y"] - w / 2
        y1 = row["y"] + w / 2

        outlines.append(go.Scatter(
            x=[x0, x1, x1, x0, x0],
            y=[y0, y0, y1, y1, y0],
            mode='lines',
            line=dict(color='gray', width=1),
            showlegend=False
        ))
    return outlines
