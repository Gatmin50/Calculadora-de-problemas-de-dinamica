# Importa las bibliotecas necesarias
import plotly.graph_objects as go
import numpy as np

# Define la amplitud, la frecuencia y el desfase
amplitud = 2  # por ejemplo, 2
frecuencia = 2 * np.pi  # ajustado para que la longitud de onda sea 1 unidad
phi = np.pi / 2  # desfase inicial de pi/2 radianes, por ejemplo

# Crea algunos datos
x = np.linspace(0, 10, 1000)  
y = amplitud * np.sin(frecuencia * x + phi)  

# Crea un objeto de trazado
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Añade anotaciones para la amplitud y longitud de onda 
fig.add_annotation(
    x=0,
    y=amplitud,
    text="A",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#EB5252",
    ax=0,
    ay=-50,
)
lambda_position = 2*np.pi/frecuencia   # Calcula posición basada en frecuencia 
fig.add_annotation(
    x=lambda_position,
    y=amplitud,
    text="λ",
    showarrow=True,
    arrowhead=2,   # Cambia estilo de cabeza de flecha si es necesario 
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#11C26F",
    ax=lambda_position,   # Calcula diferencia en 'x' entre inicio y posición calculada 
    ay=0   # Ajusta posición vertical si es necesario 
)

# Muestra el gráfico 
fig.show()






# Importa las bibliotecas necesarias
import plotly.graph_objects as go
import numpy as np

# Define la amplitud, la frecuencia y el desfase
amplitud = 2  # por ejemplo, 2
frecuencia = 2 * np.pi  # ajustado para que la longitud de onda sea 1 unidad
phi = np.pi / 2  # desfase inicial de pi/2 radianes, por ejemplo

# Crea algunos datos
x = np.linspace(0, 10, 1000)  
y = amplitud * np.sin(frecuencia * x + phi)  

# Crea un objeto de trazado
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Añade anotaciones para la amplitud y longitud de onda 
fig.add_annotation(
    x=0,
    y=amplitud,
    text="A",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#EB5252",
    ax=0,
    ay=-50,
)
lambda_position = 2*np.pi/frecuencia   # Calcula posición basada en frecuencia 
fig.add_annotation(
    x=lambda_position/2,  # Coloca el texto en el centro de la longitud de onda
    y=0,
    text="λ",
    showarrow=True,
    arrowhead=4,   # Cambia estilo de cabeza de flecha si es necesario 
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#11C26F",
    ax=lambda_position/2,   # Calcula diferencia en 'x' entre inicio y posición calculada 
    ay=0   # Ajusta posición vertical si es necesario 
)

# Muestra el gráfico 
fig.show()
