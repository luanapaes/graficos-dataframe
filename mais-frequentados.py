import pandas as pd

# carregando o dataframe
df = pd.read_csv('data.csv')

# Converta o DataFrame em um dicionário - cada coluna virou um "array"
data_dict = df.to_dict(orient='list')

# Acessa cada coluna do dicionário e colocada cada uma em uma variável
months_as_member = data_dict['months_as_member']
weight = data_dict['weight']
days_before = data_dict['days_before']
day_of_week = data_dict['day_of_week']
time = data_dict['time']
category = data_dict['category']
attended = data_dict['attended']

import plotly.express as px
import pandas as pd

import plotly.express as px
import pandas as pd

# Crie um DataFrame com suas variáveis
df = pd.DataFrame({
    'day_of_week': day_of_week,
    'time': time
})

# Cria uma coluna com a contagem de ocorrências para cada combinação de dia da semana e hora
df_grouped = df.groupby(['day_of_week', 'time']).size().reset_index(name='count')

# Calcule as contagens para AM e PM
am_count = df_grouped[df_grouped['time'] == 'AM']['count'].sum()
pm_count = df_grouped[df_grouped['time'] == 'PM']['count'].sum()

# Determina qual período tem maior contagem
if am_count > pm_count:
    maior_periodo = "entre 00h e 12h o movimento é maior"
else:
    maior_periodo = "entre 12h e 00h o movimento é maior"

# Cria o gráfico de barras
fig = px.bar(df_grouped, x='day_of_week', y='count', color='time',
             labels={'day_of_week': 'Dia da Semana', 'count': 'Hora'},
             title='Gráfico de Barras: Contagem por Dia da Semana e Hora')

# Adiciona um parágrafo de texto com base no período com a maior contagem
fig.add_annotation(
    text=maior_periodo,
    x=0.5,  # Posição x no gráfico (0 a 1)
    y=1.2,  # Posição y no gráfico (0 a 1)
    showarrow=False,
    font=dict(size=14),
    bgcolor="lightgray",
    bordercolor="gray",
    borderwidth=1,
    borderpad=4,
    opacity=0.7
)

fig.show()
