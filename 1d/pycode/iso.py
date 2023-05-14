import pandas as pd
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv('data_true.csv')
# X = df['x']
# Y = df['y']
# Z = df['z']
values = df['u'].to_numpy()
values = values[:1000000]

X, Y, Z = np.mgrid[0:0.99:10j, 0:0.99:10j, 0:0.99:10j]
fig = go.Figure()

fig.add_trace(go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=d.flatten(),
    isomin=0.0,
    isomax=0.6,
    surface_count=1, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=10, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))

fig.add_trace(go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=b.flatten(),
    isomin=0.5,
    isomax=0.5,
    surface_count=1, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=2, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()

