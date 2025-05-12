import pandas as pd
import plotly.graph_objects as go
from pick_analysis import simulate_picking_data
from racking_layout import generate_rack_locations
from racking_outline import create_location_outlines

df = generate_rack_locations()
df = simulate_picking_data(df)

fig = go.Figure()

fig.add_traces(create_location_outlines(df))

fig.add_trace(go.Scatter(
    x=df["x"],
    y=df["y"],
    mode='markers',
    marker=dict(
        size=10,
        color=df["picks"],
        colorscale='RdBu_r',
        colorbar=dict(title='Picks per Day'),
        opacity=0.8,
        cmin=0,
        cmax=df["picks"].max()
    ),
    text=df.apply(lambda row: f"{row.location_id} — {row.picks} picks/day", axis=1),
    hovertemplate='%{text}<extra></extra>'
))

fig.update_layout(
    title="2D Visualization of an Arbitrary Warehouse Activity (Picks per Day)",
    xaxis_title= "Project Height (ft)",
    yaxis_title= "Width (ft)",
    height=750,
    width=1000,
    template='plotly_white',
    yaxis=dict(scaleanchor="x", scaleratio=1)  # 1:1 aspect ratio
)

fig.write_html("img/2d_warehouse_visualization.html")
fig.show()

