import plotly.graph_objects as go
from pick_analysis import simulate_picking_data
from racking_layout import generate_rack_locations
from racking_outline import create_location_outlines

locations = generate_rack_locations()
df = simulate_picking_data(locations)

scatter = go.Scatter3d(
    x=df["x"], y=df["y"], z=df["z"],
    mode='markers',
    marker=dict(
        size=6,
        color=df["picks"],
        colorscale='RdBu_r',
        colorbar=dict(title='Picks per Day'),
        opacity=0.9
    ),
    text=df.apply(lambda row: f"{row.location_id} — {row.picks} picks/day", axis=1),
    hovertemplate='%{text}<extra></extra>'
)

outline_traces = create_location_outlines(df)

fig = go.Figure(data=[scatter] + outline_traces)
fig.update_layout(
    title="Pick Frequency by Location",
    scene=dict(
        xaxis=dict(title='Width (Bays)', backgroundcolor="white"),
        yaxis=dict(title='Aisles (Depth)', backgroundcolor="white"),
        zaxis=dict(title='Height (Levels)', backgroundcolor="white"),
        aspectmode='data'
    ),
    height=750,
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()

html_path = "C:/Users/asheri/PythonDevelopment/WarehouseManagementApp/img/3d_warehouse_pick_visualization.html"
fig.write_html(html_path)
html_path

