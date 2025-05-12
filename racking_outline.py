import plotly.graph_objects as go

def create_location_outlines(df):
    lines = []
    for _, row in df.iterrows():
        x0, x1 = row['x_left'], row['x_right']
        y0, y1 = row['y_inside'], row['y_outside']
        z0, z1 = row['z_bottom'], row['z_top']

        corners = [
            (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z0),
            (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1), (x0, y0, z1),
            (x1, y0, z1), (x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1), (x0, y1, z0)
        ]
        x, y, z = zip(*corners)
        lines.append(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='gray', width=1), showlegend=False))

    return lines