import streamlit as st
import pandas as pd
import plotly.express as px

# Daten laden
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# country = st.selectbox('Select a Country', df['country'].unique())
country = st.sidebar.selectbox('Select a Country', df['country'].unique())
st.title(f"Streamlit App Demo 	:earth_americas:")
st.data_editor(df, hide_index=True)

# Erstellen eines Dropdown-Menüs für die Auswahl des Landes


# Filtern der Daten basierend auf der Auswahl und Erstellen eines Diagramms
filtered_df = df[df.country == country]
fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'GDP Per Capita of {country}')

# Anzeigen des Diagramms
st.plotly_chart(fig)
