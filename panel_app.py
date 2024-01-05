import panel as pn
import pandas as pd
import plotly.express as px

pn.config.theme = 'dark'
# Daten laden
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Ein Dropdown-Widget erstellen
country_selector = pn.widgets.Select(name='Country', options=list(df['country'].unique()),
                                     styles={'width': '200%'})


# Eine Plotly-Visualisierung basierend auf der Auswahl erstellen
@pn.depends(country_selector.param.value)
def create_plot(country):
    filtered_df = df[df['country'] == country]
    return px.line(filtered_df, x='year', y='gdpPercap',
                   title=f'GDP Per Capita of {country}',
                   template="plotly_dark")


"""
# ZWEITE GRAFIK
@pn.depends(country_selector.param.value)
def create_second_plot(country):
    filtered_df = df[df['country'] == country]
    return px.scatter(filtered_df, x='year', y='lifeExp', title=f'Life Expectancy in {country}')
"""

# Dashboard erstellen
dashboard = pn.Column(pn.pane.Markdown(
        """# Title of Panel App""",
        align="center",
    ), country_selector, create_plot)

# Das Dashboard als bedienbares Objekt bereitstellen
dashboard.servable()
