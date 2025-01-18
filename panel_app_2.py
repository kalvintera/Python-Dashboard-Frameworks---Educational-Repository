import panel as pn
import pandas as pd
import plotly.express as px

# you must activate the Panel extension and include "plotly" as an argument.
# This step ensures that plotly.js is properly set up.
# https://panel.holoviz.org/reference/panes/Plotly.html

pn.extension("plotly", "tabulator", sizing_mode="stretch_width")


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

select_continent_options = list(df["continent"].unique())
select_country_options = list(df["country"].unique())
max_year = df["year"].max()

# Widgets - Filter Funktionen

continent_filter = pn.widgets.Select(name="Continent", options=["All"] + select_continent_options, value="All")
year_slider = pn.widgets.IntSlider(
    name="Year", start=df["year"].min(),
    end=df["year"].max(),
    step=5,
    value=df["year"].min()
)
country_filter = pn.widgets.Select(name="Country", options=["All"] + select_country_options, value="All")

median_df = df.groupby(['continent', 'year'], as_index=False).agg({
    'lifeExp': 'median',
    'pop': 'sum'
})


# Filterfunktion für Table
@pn.depends(
    continent_filter.param.value,
    year_slider.param.value,
    country_filter.param.value
)
def update_table(continent, year, country):
    """
    Aktualisiert die Tabellendaten basierend auf den ausgewählten Filtern für Kontinent, Jahr und Land.

    Diese Funktion filtert die Daten im DataFrame `df` basierend auf den Benutzeroptionen:
    - `continent_filter`: Filtert die Daten nach dem ausgewählten Kontinent.
    - `year_slider`: Zeigt Daten für Jahre im angegebenen Bereich.
    - `country_filter`: Filtert die Daten nach dem ausgewählten Land.

    :param continent: Kontinent, nach dem gefiltert werden soll. Wenn "All" - alle Kontinente berücksichtigt.
    :param year: Das Startjahr für den Filterbereich.
    :param country: Der Name des Landes, nach dem gefiltert werden soll.
    :return: Eine Tabelle mit den gefilterten Daten
    """
    filtered_df = df.copy()
    if year < max_year:
        filtered_df = filtered_df[(filtered_df['year'] >= year) & (filtered_df['year'] <= max_year)]
        filtered_df["year"] = filtered_df["year"].astype(int)

    if continent != "All":
        filtered_df = filtered_df[filtered_df["continent"] == continent]

    if country != "All":
        filtered_df = filtered_df[filtered_df["country"] == country]
    formatters = {
        'year': {"type": "number", "format": "0"}
    }

    return pn.widgets.Tabulator(filtered_df, layout="fit_data_fill", height=400, formatters=formatters)


# Liniendiagramm-Callback
@pn.depends(continent_filter.param.value, year_slider.param.value)
def update_line_chart(continent, year):
    filtered_df = median_df.copy()
    if continent != "All":
        filtered_df = filtered_df[filtered_df["continent"] == continent]
    if year < max_year:
        filtered_df = filtered_df[(filtered_df['year'] >= year) & (filtered_df['year'] <= max_year)]
    else:
        filtered_df = filtered_df[(filtered_df['year'] >= max_year - 10) & (filtered_df['year'] <= max_year)]

    chart = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        color="continent",
        title="Life Expectancy Over Time",
        labels={"lifeExp": "Life Expectancy", "year": "Year"},
        markers=True,
    )
    return pn.pane.Plotly(chart, height=600)


# Donut-Chart/Pie-Chart
@pn.depends(continent_filter.param.value, year_slider.param.value)
def update_donut_chart(continent, year):
    median_copy = median_df.copy()
    filtered_df = median_copy[median_copy["year"] == year]
    if continent != "All":
        filtered_df = filtered_df[filtered_df["continent"] == continent]
    chart = px.pie(
        filtered_df,
        values="pop",
        names="continent",
        title=f"Population Distribution in {year}",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    return pn.pane.Plotly(chart, height=600)


# Dashboard Layout
dashboard = pn.template.MaterialTemplate(
    title="Population Analysis Dashboard",
    sidebar=[
        "## Filter Options",
        continent_filter,
        country_filter,
        year_slider,
    ],
    main=[
        pn.Row(
            pn.Column(update_donut_chart, width=400),  # Feste Breite für Donut-Chart: width=400
            pn.Column(update_line_chart, sizing_mode="stretch_width"),  # Flexibler: sizing_mode="stretch_width"

        ),

        pn.Row(update_table)
    ],
)

# Serve Dashboard
dashboard.servable()