import streamlit as st
import pandas as pd
import plotly.express as px


# Laden der Daten
@st.cache_data
def load_data():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
    )
    return df


df = load_data()


# Eine Funktion, um einen Plot zu erstellen
def create_fig(df, x, y, title, color=None):
    fig = px.scatter(df, x=x, y=y, color=color, title=title)
    return fig


# Definieren der Seiten
def overview_page():
    st.title('Überblick über GitHub-Dashboard-Daten')
    st.write(df.head())


def visualization_page():
    st.title('Visualisierungen der GitHub-Dashboard-Daten')
    st.plotly_chart(create_fig(df, 'date', 'daily_vaccinations', 'Tägliche Impfungen'))


def analysis_page():
    st.title('Analyse der GitHub-Dashboard-Daten')
    # Platzhalter für weitere Analysen


# Seitenleiste für Navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Wähle eine Seite:', ['Überblick', 'Visualisierungen', 'Analyse'])

# Seite anzeigen basierend auf Auswahl
if page == 'Überblick':
    overview_page()
elif page == 'Visualisierungen':
    visualization_page()
elif page == 'Analyse':
    analysis_page()


# Zusätzliche Widgets in der Seitenleiste
st.sidebar.header('Weitere Einstellungen')
st.sidebar.markdown(
    'Hier können zusätzliche Widgets hinzugefügt werden, um die Daten zu filtern oder die Darstellung anzupassen.'
)