import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def plot_sinusoidal(length, amplitude, phase):
    x = np.linspace(0, 10, 1000)
    y = amplitude * np.sin(length * x + phase)
    fig = go.FigureWidget(data=go.Scatter(x=x, y=y, mode='lines'))

    # Añadir flecha para la amplitud
    fig.add_trace(go.Scatter(
        x=[0, 0], y=[0, amplitude],
        mode="lines+markers",
        marker=dict(symbol="circle", size=10),
        line=dict(color="red", width=2),
        name="Amplitud",
        showlegend=True,
    ))

    # Añadir flecha para la longitud de onda
    fig.add_trace(go.Scatter(
        x=[0,(2 * np.pi / length)], y=[amplitude, amplitude],
        mode="lines+markers",
        marker=dict(symbol="circle", size=10),
        line=dict(color="green", width=2),
        name="Longitud de onda",
        showlegend=True,
    ))

    fig.update_layout(title='Ecuación Sinusoidal')
    fig.show()

length_slider = widgets.FloatSlider(value=np.pi/0.5, min=0.1, max=10, step=0.1, description='Longitud de onda:')
amplitude_slider = widgets.FloatSlider(value=1, min=0.1, max=5, step=0.1, description='Amplitud:')
phase_slider = widgets.FloatSlider(value=0, min=0, max=2 * np.pi, step=0.1, description='Desfase inicial:')
widgets.interactive(plot_sinusoidal, length=length_slider, amplitude=amplitude_slider, phase=phase_slider)