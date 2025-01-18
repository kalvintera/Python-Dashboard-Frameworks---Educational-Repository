# Python Dashboard Frameworks - Educational Repository

## Über dieses Repository
Dieses Repository wurde als Lehrmaterial für Kurse im Bereich Data Science und Webentwicklung erstellt. Es bietet einen praktischen Vergleich zwischen verschiedenen Python-Frameworks, die zur Erstellung von interaktiven Dashboards verwendet werden können: Streamlit, Panel und Voilà. Zusätzlich enthält es Übungstemplates für Streamlit, die Studenten dazu ermutigen, ihre eigene Projekte zu entwerfen und die Steuerelemente von Streamlit zu erkunden.

## Struktur des Repositories
- `panel_app.py`: Eine einfache Panel-App, die die Erstellung eines Dashboards mit Dropdown-Selektion und Plotly-Diagrammen demonstriert.
- `voila_app.ipynb`: Ein Jupyter Notebook, das mithilfe von Voilà in eine Web-App verwandelt werden kann. Es beinhaltet interaktive Widgets und Diagramme.
- `gradio_app.py`: Eine einfache Gradio-App, die basic features vorstellt.
- `streamlit_app.py`: Eine Streamlit-App, die zeigt, wie man ein interaktives Dashboard mit Streamlit erstellt.
- `streamlit_exercise_template_1.py`: Ein Streamlit-Übungstemplate, das verschiedene interaktive Widgets enthält.
- `streamlit_exercise_template_2.py`: Ein weiteres Übungstemplate, das auf die fortgeschrittene Nutzung von Streamlit abzielt.

## Über das verwendete Dataset
Für die Demos in diesem Repository wird ein öffentlich zugängliches Dataset von GitHub verwendet, das historische Daten zum Bruttoinlandsprodukt (BIP) pro Kopf für verschiedene Länder enthält. Dieses Dataset ist Teil der [Gapminder-Daten](https://www.gapminder.org/data/), die von der Gapminder Foundation bereitgestellt werden.

### Datenquelle
Das Dataset wurde vom GitHub-Repository [plotly/datasets](https://github.com/plotly/datasets) bezogen und steht unter diesem [direkten Link](https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv) zur Verfügung.

### Inhalt des Datasets
Das Dataset umfasst folgende Spalten:
- `country`: Name des Landes
- `year`: Das Jahr der Beobachtung
- `pop`: Bevölkerungszahl des Landes in dem Jahr
- `continent`: Kontinent, zu dem das Land gehört
- `lifeExp`: Durchschnittliche Lebenserwartung in dem Land für das Jahr
- `gdpPercap`: Bruttoinlandsprodukt pro Kopf, angepasst um Kaufkraftparität

### Verwendung im Kurs
Dieses Dataset wird verwendet, um grundlegende Konzepte der Datenvisualisierung und interaktiven Dashboard-Erstellung zu vermitteln. Es eignet sich hervorragend, um Trends über Zeit zu analysieren und Einblicke in die wirtschaftliche Entwicklung verschiedener Länder zu gewinnen.

### Datenschutz und Lizenz
Bitte beachten Sie, dass dieses Dataset öffentlich zugänglich ist und für Bildungszwecke genutzt wird. Für weitere Informationen über die Lizenz und die Nutzung der Daten, besuchen Sie bitte die Gapminder-Website oder das [GitHub-Repository](https://github.com/plotly/datasets).

### Über das COVID-19 Impf-Dataset
Zusätzlich zu den Gapminder-Daten verwenden wir für einige Demos ein Dataset, das Einblicke in die weltweiten COVID-19-Impfungen bietet. Dieses Dataset wird bereitgestellt von Our World in Data und enthält detaillierte Informationen zu den Fortschritten der Impfkampagnen in verschiedenen Ländern.

### Über das COVID-19-Dataset von Our World in Data
Für die Dash-Demos in diesem Repository wird ein weiteres Dataset verwendet, das Informationen über die COVID-19-Pandemie beinhaltet, insbesondere im Hinblick auf Impfungen. Das Dataset wird von Our World in Data gepflegt und regelmäßig aktualisiert, um die neuesten verfügbaren Daten widerzuspiegeln.

### Datenquelle
Das COVID-19-Dataset ist verfügbar über das GitHub-Repository von Our World in Data. Sie können das Impf-Dataset über folgenden Link direkt beziehen: [COVID-19 Vaccination Data](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv).

### Inhalt des COVID-19-Datasets
Das Dataset umfasst verschiedene Datenpunkte, darunter:
- `location`: Der Name des Landes oder der Region
- `date`: Das Datum der Datenerfassung
- `total_vaccinations`: Die Gesamtzahl der verabreichten Impfstoffdosen
- `people_vaccinated`: Die Anzahl der Personen, die mindestens eine Dosis erhalten haben
- `people_fully_vaccinated`: Die Anzahl der Personen, die vollständig geimpft sind
- `daily_vaccinations`: Die durchschnittliche tägliche Anzahl der verabreichten Impfdosen

### Datenschutz und Lizenz
Die Daten von Our World in Data sind unter einer Creative Commons Lizenz verfügbar, die eine Verwendung zu Bildungszwecken erlaubt. Weitere Details zur Lizenz und den Nutzungsbedingungen finden Sie auf der [Our World in Data Website](https://ourworldindata.org/).

Es ist wichtig, dass die Studierenden die Quellen ihrer Daten verstehen und lernen, wie man Daten ethisch und verantwortungsbewusst für öffentliche Gesundheitsanalysen nutzt.
## Vorbereitung für die Verwendung
Stellen Sie sicher, dass Sie die folgenden Pakete in Ihrer Python-Umgebung installiert haben:
- Streamlit
- Panel
- Voilà
- Gradio
- Plotly
- Pandas
- ipywidgets
- plotly
- plotly-express
- extra-streamlit-components (Optional)


Sie können sie installieren, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:
```bash
pipenv install 
```

## Apps starten
Um die Apps zu starten, navigieren Sie in Ihrem Terminal zu dem Verzeichnis dieses Repositories und führen Sie den entsprechenden Befehl aus:

**Für Panel-App:**
```bash

panel serve panel_app.py --show
```
**Für Voilà-App:**
```bash
voila voila_app.ipynb
```
**Für Streamlit-Apps:**
```bash
streamlit run streamlit_app.py
```
## Für Übungstemplates:
```bash
streamlit run streamlit_exercise_template_1.py
streamlit run streamlit_exercise_template_2.py
```

**Für Gradio-Apps:**
```bash
python gradio_app.py
```

## Zweck der Demos
Die Demos wurden erstellt, um Studenten zu helfen:

Die Architektur und Funktionsweise der jeweiligen Frameworks zu verstehen.
Praktische Erfahrungen im Umgang mit Data-Science-Tools zu sammeln.
Eigene Dashboards zu erstellen und zu präsentieren.
Prototyping-Fähigkeiten zu entwickeln, die in realen Projekten angewendet werden können.