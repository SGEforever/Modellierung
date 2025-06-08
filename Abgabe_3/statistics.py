import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib
import urllib.request

url = 'https://github.com/nickeubank/MIDS_Data/raw/master/US_AmericanCommunitySurvey/US_ACS_2017_10pct_sample.dta'
data_file = pathlib.Path(url.rsplit('/', 1)[-1])

if not data_file.is_file():
    # this downloads 63 MB of data. May take a few seconds.
    # We could also use `census_data = pd.read_stata(url)['inctot']`
    # but here we save the file to disk in case we need to reset it.
    urllib.request.urlretrieve(url, data_file)

census_data = pd.read_stata(data_file.resolve())['inctot']

#Statistische Indikatoren
mean = census_data.mean()
std = census_data.std()
median = census_data.median()
counts = census_data.value_counts()
#Die große Anzahl der Einkommen mit einem Wert von 0 und 9999999 lassen darauf schließen, dass diese Werte fehlerhaft sind. Dementsprechend verfälschen sie auch das Ergebnis
#deutlich, was durch den großen Unterschied zwischen mean und median deutlich wird, der in der Theorie deutlich geringer sein müsste.

#Verschiedene Methoden
#Methode 1: Die fehlenden Werte werden durch NA ersetzt und anschließend gelöscht. Bei zukünftigen Berechnungen werden sie so ignoriert. Man könnte auch auf das Löschen verzichten, um so die Anzahl der fehlerhaften Werte auslesen zu können
method_1 = census_data.copy()
method_1.replace([0, 9999999], pd.NA, inplace=True)
method_1 = method_1.dropna()

#Methode 2: Die fehlerhaften Werte 0 und 9999999 werden mit den kleinsten, bzw. größten offensichtlich korrekten Werten ersetzt und in Zukunft weiterhin beachtet
method_2 = census_data.copy()
real_min = method_1.min()
real_max = method_1.max()
method_2.replace([0], real_min, inplace=True)
method_2.replace([9999999], real_max, inplace=True)

#Welche Methode richtig ist, lässt sich jedoch nur entscheiden, wenn die genaue Art des Fehlers bekannt ist.
#Da die Werte 0 und 9999999 bei .dat Dateien jedoch in der Regel für nicht vorhandene oder fehlerhaft übertragene Daten stehen, nutze ich später Methode 1^

#Abbildung Einkommensverteilung

def gettenks(series : pd.Series) -> pd.Series:
    values = pd.Series(data=[0,0,0,0,0,0,0,0,0,0,0,0], index=[np.arange((12))])
    for i in range(10):
        minv = i * 10000
        maxv = (i+1) * 10000
        values.loc[i+1] = np.sum((series >= minv) & (series < maxv))
    values[0] = np.sum(series < 0)
    values[11] = np.sum(series > 100000)
    values.index = [i[0]*10000 if isinstance(i, tuple) else i for i in values.index]
    values.rename({110000: '>100000'}, inplace=True)
    return values

tens = gettenks(method_1)
tens.plot(kind="bar")
plt.title("Verteilung der Einkommen in 10.000er Schritten")
plt.xlabel("Einkommen (gerundet nach oben)")
plt.ylabel("Anzahl")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Lorenzkurve
income = method_1.index.values
frequency = method_1.values
total_income = income * frequency

sort_idx = np.argsort(income)
income = income[sort_idx]
frequency = frequency[sort_idx]
total_income = total_income[sort_idx]

cum_population = np.cumsum(frequency)
cum_income = np.cumsum(total_income)

cum_population = cum_population / cum_population[-1]
cum_income = cum_income / cum_income[-1]

plt.figure(figsize=(6, 6))
plt.plot(cum_population, cum_income, label='Datensatz Amerika 2017', color='blue')
plt.plot([0, 1], [0, 1], '--', color='gray', label='Perfekte Ausgeglichenheit')
plt.plot([0, 1], [0, 0], color='red')
plt.plot([1], [1], 'ro', label='Perfekte Unausgeglichenheit')

plt.xlabel('Anteil der Bevölkerung')
plt.ylabel('Anteil des Einkommens')
plt.title('Lorenzkurve')
plt.legend()
plt.grid(True)
plt.show()

#Gini-Koeffizient
def getGiniCoefficient(series: pd.Series) -> int:
    series_sorted = pd.Series(series.sort_values().values, index=np.arange(1, series.size + 1))
    t = np.sum(index * value for index, value in series_sorted.items())
    b = series.size * np.sum(series.values)
    coefficient = 2 * (t / b) - (series.size + 1) / series.size;
    return coefficient

usaCoefficient = getGiniCoefficient(method_1)
print(usaCoefficient)