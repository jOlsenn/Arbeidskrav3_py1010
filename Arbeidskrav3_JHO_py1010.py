# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:50:56 2026

@author: Jan-Halvor Olsen
"""

# [Oppgave a]

# [Importerer pandas biblioteket slik at vi kan lese inn excel filen og jobbe med dataene]
import pandas as pd

# [Leser inn excel filen for oppgaven]
data = pd.read_excel("support_uke_24.xlsx")

# [Her henter vi ut hver kolonne ved navn og lagrer dem i egne arrayer, 
# dette er slik at vi kan jobbe med dataen]
u_dag = data["Ukedag"].values
kl_slett = data["Klokkeslett"].values
varighet = data["Varighet"].values
score = data["Tilfredshet"].values



# [Oppgave b]

# [Importerer pandas for å kunne telle og strukturere dataene]
import pandas as pd

# [Importerer matplotlib for å kunne lage søylediargammet for å visualisere det]
import matplotlib.pyplot as plt

# [Leser inn excel filen]
data = pd.read_excel("support_uke_24.xlsx")

# [Henter ut ukedagene]
u_dag = data["Ukedag"].values

# [Her teller vi hvor mange ganger hver ukedag forekommer]
dag_telling = pd.Series(u_dag).value_counts()

# [Setter dagene i riktig rekkefølge slik at grafen ikke blir feil sortert]
rekkefolge = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
dag_telling = dag_telling.reindex(rekkefolge)

# [Lager figuren for søylediagrammet]
plt.figure()

# [Her lages selve søylediagrammet med ukedagene bortover og 
# antall henvendelser oppover]
plt.bar(dag_telling.index, dag_telling.values)

# [Gir diagrammet en tittel]
plt.title("Antall henvendelser per ukedag")

# [Gir navn til x-aksen for å vise at det er ukedager det er snakk om]
plt.xlabel("Ukedag")

# [Gir navn til y-aksen med antall, slik at det er lett å forstå]
plt.ylabel("Antall")

# [Viser diagrammet i consolen]
plt.show()



# [Oppgave c]

# [Importerer pandas for å kunne jobbe med tidsverdier]
import pandas as pd

# [Leser inn excel filen]
data = pd.read_excel("support_uke_24.xlsx")

# [Henter ut varighet]
varighet = data["Varighet"].values

# [Gjør om varigheten til riktig tid format slik at vi kan sammenligne 
# verdiene riktig og ikke blir oppfattet som tekst]
varighet_tid = pd.to_timedelta(varighet.astype(str))

# [Finner korteste og lengste samtale]
korteste = min(varighet_tid)
lengste = max(varighet_tid)

# [Printer resultatet]
print("Korteste samtale var:", korteste)
print("Lengste samtale var:", lengste)



# [Oppgave d]

# [Importerer pandas for å kunne regne med tidsverdier]
import pandas as pd

# [Leser inn excel filen]
data = pd.read_excel("support_uke_24.xlsx")

# [Henter ut varighet]
varighet = data["Varighet"].values

# [Gjør om varigheten til riktig format slik at vi kan regne på den og den ikke
# blir sett som en tekststring]
varighet_tid = pd.to_timedelta(varighet.astype(str))

# [Regner ut gjennomsnittlig samtaletid]
snitt = varighet_tid.mean()

# [Gjør om til sekunder slik at svaret blir enklere å forstå]
tot_sek = int(snitt.total_seconds())

# [Regner om til minutter og sekunder. På minutter så regner vi om det
# hele tallet, og på sekunder så regner vi ut hvor mye som "er igjen"]
minutter = tot_sek // 60
sekunder = tot_sek % 60

# [Printer resultatet]
print("Gjennomsnitt samtaletid er:", minutter, "min og", sekunder, "sek")



# [Oppgave e]

# [Importerer pandas for å kunne jobbe med klokkeslett]
import pandas as pd

# [Importerer matplotlib for å kunne lage kakediagram]
import matplotlib.pyplot as plt

# [Leser inn excel filen]
data = pd.read_excel("support_uke_24.xlsx")

# [Henter ut klokkeslett]
kl_slett = data["Klokkeslett"].values

# [Gjør om klokkeslettene til tidsformat slik at vi kan hente ut timen og at 
# det ikke blir oppfattet som en tekst string.]
tider = pd.to_datetime(kl_slett.astype(str), format="%H:%M:%S")

# [Her lager vi tellere for hver tidsperiode]
kl_08_10 = 0
kl_10_12 = 0
kl_12_14 = 0
kl_14_16 = 0

# [Går gjennom alle klokkeslettene]
for tid in tider:

    # [Henter ut hvilken time samtalen har skjedd i]
    time = tid.hour

    # [Her sjekker vi hvilken tidsperiode klokkeslettet tilhører]
    if 8 <= time < 10:
        
        # [Om klokken er mellom 08 og 10 økes telleren for denne perioden med 1]
        kl_08_10 += 1
        
    elif 10 <= time < 12:
        
        # [Om klokken er mellom 10 og 12 økes telleren for denne perioden med 1]
        kl_10_12 += 1
        
    elif 12 <= time < 14:
        
        # [Om klokken er mellom 12 og 14 økes telleren for denne perioden med 1]
        kl_12_14 += 1
        
    elif 14 <= time < 16:
        
        # [Om klokken er mellom 14 og 16 økes telleren for denne perioden med 1]
        kl_14_16 += 1

# [Lager en figur for kakediagrammet]
plt.figure()

# [Her lager vi kakediagrammet med antall henvendelser i hver tidsperiode]
plt.pie([kl_08_10, kl_10_12, kl_12_14, kl_14_16],
        
        # [Her setter vi navn på hver del av kakediagrammet]
        labels=["08-10", "10-12", "12-14", "14-16"],
        
        # [Denne viser prosent inne i kakediagrammet med 1 desimal]
        autopct="%1.1f%%")

# [Gir diagrammet en tittel slik at det er lett å se hva det viser]
plt.title("Henvendelser per tidsrom")

# [Viser diagrammet i consolen]
plt.show()



# [Oppgave f]

# [Importerer pandas for å kunne jobbe med tilfredshet]
import pandas as pd

# [Leser inn excel filen]
data = pd.read_excel("support_uke_24.xlsx")

# [Henter ut tilfredshet]
score = data["Tilfredshet"].values

# [Her filtrerer jeg bort de som ikke har gitt noe tilbakemelding, slik at 
# de ikke blir tatt med på den totale scoren]
gyldige_scores = pd.Series(score).dropna()

# [Teller antall positive og negative score]
pos = len(gyldige_scores[gyldige_scores >= 9])
neg = len(gyldige_scores[gyldige_scores <= 6])

# [Totalt antall svar på tilfredshet]
tot = len(gyldige_scores)

# [Regner ut prosent for positiv og negativ score]
prosent_pos = (pos / tot) * 100
prosent_neg = (neg / tot) * 100

# [Regner ut NPS]
nps = prosent_pos - prosent_neg

# [Printer resultatet]
print("NPS er:", round(nps, 2))