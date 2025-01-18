import panel as pn
import pandas as pd
import plotly.express as px

pn.config.theme = 'dark'
# Daten laden
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Ein Dropdown-Widget erstellen - Beispiele Widgets: https://panel.holoviz.org/reference/index.html#widgets
# Select : https://panel.holoviz.org/reference/widgets/Select.html
# Select Beispiel : # select = pn.widgets.Select(name='Select', options=['Biology', 'Chemistry', 'Physics'])
country_selector = pn.widgets.Select(name='Country', options=list(df['country'].unique()),
                                     styles={'width': 'max'})


# Eine Plotly-Visualisierung basierend auf der Auswahl erstellen
@pn.depends(country_selector.param.value)
def create_plot(country):
    filtered_df = df[df['country'] == country]
    return px.line(filtered_df, x='year', y='gdpPercap',
                   title=f'GDP Per Capita of {country}',
                   template="plotly_dark")


# Instanziierung der Vorlage mit Widgets, die in der Sidebar angezeigt werden
template = pn.template.BootstrapTemplate(
    title='Panel App',
    sidebar=[country_selector],
)

# Dashboard erstellen
template.main.append(
    pn.Column(
        pn.pane.Markdown(
            """# Title of Panel App""",
            align="center",
        ),
        create_plot,

    )
)

template.servable()



