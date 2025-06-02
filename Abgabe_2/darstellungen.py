import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

actinides = pd.read_csv('Abgabe_2/data/actinides.csv', index_col=0,).squeeze()
actinides.plot(
    kind="bar",
    title="Logarithmische Zerfallszeit von Aktiniden",
    xlabel="Stoff",
    ylabel="Zerfallszeit in Jahren",
    logy=True
)
plt.show()

stock_price = pd.read_csv('Abgabe_2/data/stock_price.csv', index_col=0, parse_dates=True).squeeze()
stock_price.plot(
    title="Entwicklung der Aktie seit 2019 in €",
    xlabel="Datum",
    ylabel="x-facher Wert der Aktie im Vergleich zum Startwert"
)
plt.show()

waehlerstimmen = pd.read_csv('Abgabe_2/data/waehlerstimmen.csv', index_col=0).squeeze()
percentage = waehlerstimmen / waehlerstimmen.sum() * 100
percentage.plot(
    kind="bar",
    title="Zweitstimmenanteile bei der BTW 2021",
    ylabel="Anteil in %",
    xlabel="Partei"
)
plt.show()