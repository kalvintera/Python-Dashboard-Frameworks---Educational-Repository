import streamlit as st
import pandas as pd
import plotly.express as px

# Daten laden
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

st.sidebar.subheader("Filter Menu", divider="gray")

# Erstellen eines Dropdown-Menüs für die Auswahl des Landes
# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox
country = st.sidebar.selectbox('Select a Country', df['country'].unique())


st.title(f"Streamlit App Demo 	:earth_americas:")
filtered_df = df[df.country == country]
st.data_editor(filtered_df, hide_index=True)

# Filtern der Daten basierend auf der Auswahl und Erstellen eines Diagramms

fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'GDP Per Capita of {country}')
fig.update_xaxes(type='category')
fig.update_yaxes(tickprefix="$", tickformat=",.0f")  # GDP mit Währungspräfix, Tausender-Trennzeichen
# (.0f -> keine Nachkommastellen)

# Anzeigen des Diagramms
st.plotly_chart(fig)
