# Vaatimusmäärittely

### Sovellusidea

Snake-peli, jossa tarkoituksena on liikuttaa käärmettä kartalla ja kerätä kartalle satunnaisiin kohtiin ilmestyviä "omenoita". Käärme kasvaa yhden ruudun verran pidemmäksi aina, kun omena on kerätty. Jos käärme törmää kartan reunaan tai itseensä, peli päättyy. Jos käärme kasvaa koko ruudukon kokoiseksi, pelaaja voittaa pelin.

### Käyttöliittymä

Peli koostuu aloitusnäytöstä, varsinaisesta pelistä, sekä game over-näkymistä. Aloitusnäytöltä pääsee varsinaiseen peliin klikkaamalla start-ruutua. Pelin päättyessä ruudulle tulee game over-näkymä. Pelin voi aloittaa alusta painamalla R-näppäintä.

### Toiminnallisuus

- Pelin aloittaminen onnistuu klikkaamalla play-näppäintä aloitusnäytöllä tai R-näppäintä muissa näkymissä.
- Pelissä käärme liikkuu itsestään. Liikkeen suuntaa voi muuttaa nuolinäppäimillä.
- "Omena" tulee kerätyksi, kun käärmeen pää kulkee samasta ruudusta, jossa "omena" sijaitsee.
- Ruudulla näkyy saavutettu score ja high score.

### Jatkokehitysideat

**Toiminnalliset:**
- Scores-näkymä, josta näkee kerättyjen "omenoiden" määrän pelikertaa kohden.
- High score-laskuri, joka päivittyy korkeimman pistemäärän mukaan.
- Scoret voitaisiin tallentaa tiedostoon niin, että peli muistaisi saadut pistemäärät myös uudelleenkäynnistyksen jälkeen.
- Tallennettujen pistemäärien nollaaminen.
- Lisää vaikeustasoja, esim. snaken liikkeen nopeuttaminen tai hidastaminen, tai esteiden lisääminen kartalle.
- Ohjenäkymä.

**Kosmeettiset**
- Jaksollisesti silmukassa kulkeva animaatio aloitusnäytöllä ja game over-näkymissä.
