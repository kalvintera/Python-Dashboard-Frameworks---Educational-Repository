# Gradio hat Pillow (PIL) als Abhängigkeit, die automatisch mitinstalliert wird
# type PIL: Python Imaging Library
from PIL import ImageOps, ImageFilter
import gradio as gr
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


country_choices = list(df['country'].unique())
default_country = country_choices[0]


# Funktionen:
def apply_filter(image, filter_type):
    """
    Wendet den gewählten Filter auf das hochgeladene Bild an.
    :param image: (PIL.Image) Das hochgeladene Bild.
    :param filter_type: Der gewählte Filter.
    :return: PIL.Image: Das bearbeitete Bild.
    """

    if filter_type == "Graustufen":
        return image.convert("L")
    elif filter_type == "Invertieren":
        return ImageOps.invert(image.convert("RGB"))
    elif filter_type == "Unschärfe":
        return image.filter(ImageFilter.GaussianBlur(5))
    elif filter_type == "Schärfen":
        return image.filter(ImageFilter.SHARPEN)
    elif filter_type == "Kantenerkennung":
        return image.filter(ImageFilter.FIND_EDGES)
    else:
        return image

# Funktion, um das Diagramm basierend auf dem ausgewählten Land zu erstellen


def create_line_plot(country: str) -> px.line:
    """
    Erstellt ein vollständig angepasstes Line Chart mit Plotly
    :param country: Das ausgewählte Land
    :return: Plotly-Figur
    """
    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df['country'] == country]

    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita of {country}",
        labels={"year": "Year", "gdpPercap": "GDP Per Capita"},
        template="plotly_dark"
    )

    fig.update_traces(line_color='orange')
    fig.update_xaxes(type='category')
    fig.update_yaxes(tickprefix="$", tickformat=",.0f")  # GDP mit Währungspräfix, Tausender-Trennzeichen

    return fig

# ------------------------------------------------------------------------
# -------------------- APP INTERFACE -------------------------------------


# Gradio-Interface mit mehreren Funktionen - Blocks sind Container um Layout zu organisieren
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Einfache Bildbearbeitungs- und Visualisierungs-Demo
        Diese Anwendung erlaubt:
        - Anwendung von Filtern auf Bilder.
        - Visualisierung der BIP-Daten.
        """
    )

    # Filtersektion
    with gr.Row(equal_height=True): # equal_height: Gleiche Höche für Spalten
        with gr.Column(scale=1):
            gr.Markdown("### Bildbearbeitung - Input")
            filter_selector = gr.Radio(
                choices=["Graustufen", "Invertieren", "Unschärfe", "Schärfen", "Kantenerkennung"],
                label="Filter auswählen",
                value="Graustufen"
            )
            image_input = gr.Image(type="pil", label="Bild hochladen", scale=4)

            apply_button = gr.Button("Filter anwenden")

        with gr.Column(scale=1):

            gr.Markdown("### Output")
            image_output = gr.Image(type="pil", label="Bearbeitetes Bild", scale=4)

        apply_button.click(
            apply_filter,
            inputs=[image_input, filter_selector],
            outputs=image_output
        )

    # Einfache Visualisierung
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Daten Visualisierung")
            country_dropdown = gr.Dropdown(
                label="Wähle ein Land",
                choices=list(df['country'].unique()),
                value=list(df['country'].unique())[0]
            )
            # plot_output = gr.Plot(label="GDP Per Capita")
            plot_output = gr.Plot(create_line_plot(default_country))

            country_dropdown.change(
                fn=create_line_plot,
                inputs=[country_dropdown],
                outputs=[plot_output]
            )


demo.launch()