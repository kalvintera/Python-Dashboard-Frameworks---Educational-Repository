import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Funktionen, die für das Template benötigt werden
def generate_data(n_rows: int = 100):
    return pd.DataFrame(np.random.rand(n_rows, 3), columns=['a', 'b', 'c'])


def create_plot(data_df: pd.DataFrame):
    return px.scatter(data_df, x='a', y='b', color='c', size='c')


# Seitenleiste mit verschiedenen Eingabemöglichkeiten
st.sidebar.header('Sidebar - Steuerelemente')
number_input = st.sidebar.number_input('Wähle eine Zahl', 0, 100, 25)
option = st.sidebar.selectbox('Wähle eine Option', ['Option A', 'Option B', 'Option C'])
slider_val = st.sidebar.slider('Wähle einen Wert', 0, 100, 50)
date_input = st.sidebar.date_input('Wähle ein Datum')
time_input = st.sidebar.time_input('Wähle eine Zeit')


# Tabs für verschiedene Inhalte
tab1, tab2, tab3, tab4 = st.tabs(["Überblick", "Visualisierungen", "Daten", "Interaktion"])

with tab1:
    st.header('Überblick')
    st.write("Hier können grundlegende Informationen zur App und ihrer Funktionsweise hinzugefügt werden.")

with tab2:
    st.header('Visualisierungen')
    df = generate_data()
    fig = create_plot(df)
    st.plotly_chart(fig)

with tab3:
    st.header('Daten')
    uploaded_file = st.file_uploader("Lade eine CSV-Datei hoch", type='csv')
    if uploaded_file:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

with tab4:
    st.header('Interaktion')
    st.write("Hier können Benutzer mit der App interagieren.")
    user_input = st.text_input('Gib etwas ein')
    st.write(f'Du hast eingegeben: {user_input}')

# Einführung einer Expander-Komponente
with st.expander("Mehr Informationen"):
    st.write("Hier könnt ihr zusätzliche Informationen verstecken, die auf Wunsch eingesehen werden können.")

# Multiselect-Widget im Hauptbereich
options = st.multiselect(
    'Wähle mehrere Optionen',
    ['Option 1', 'Option 2', 'Option 3'],
    ['Option 1']
)

# Dynamische Anzeige von Informationen basierend auf der Seitenleistenauswahl
st.write('Die ausgewählte Zahl ist', number_input)
st.write('Die ausgewählte Option ist', option)
st.write('Der ausgewählte Wert auf dem Slider ist', slider_val)
st.write('Das ausgewählte Datum ist', date_input)
st.write('Die ausgewählte Zeit ist', time_input)

# Fußzeile
st.write("Fußzeile mit nützlichen Links und Informationen.")
