import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

thermal = pd.read_csv('Abgabe_2/data/thermal.csv', index_col=0).squeeze()

thermal.sort_index().plot(
    logy=True,
    title="Thermische Leistung von Unobtainiumoxid bei verschiedenen Temperaturen",
    xlabel="Temperatur und Kelvin",
    ylabel="Thermische Leistung P in 10^x W",
)
plt.show()

degrees_small = thermal.index[:15]
degrees_large = thermal.index[15:]
powers_small = thermal.values[:15]
powers_large = thermal.values[15:]

plt.title("Verhalten der Werte unter 10 Kelvin")
plt.ylabel("Leistung in W")
plt.xlabel("Temperatur in Kelvin")
plt.plot(degrees_small, powers_small, label="linear")
plt.plot(degrees_small, np.power(powers_small, 2), label="quadratisch")
plt.plot(degrees_small, np.power(powers_small, degrees_small), label="exponentiell")
#plt.plot(degrees_small, np.log(powers_small), label="logarithmisch")
plt.legend()
plt.show()
#lineare Darstellung ist am Besten für Werte unter 10 Kelvin geeignet

plt.title("Verhalten der Werte über 10 Kelvin")
plt.ylabel("Leistung in W")
plt.xlabel("Temperatur in Kelvin")
plt.plot(degrees_large, np.power(powers_large, 1/4), label="4te Wurzel der Leistungswerte P")
#plt.plot(degrees_large, powers_large, label="normal")
plt.legend()
plt.show()
#Für Werte über 10 Kelvin ist die Darstellung mit den Werten der 4ten Wurzel der Leistungswerte am Besten geeignet, da sich so am Besten das Verhältnis zwischen Temperatur und Leistung erkennen lässt