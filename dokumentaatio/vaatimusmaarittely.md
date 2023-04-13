# Vaatimusmäärittely

### Alustava sovellusidea

Snake-peli, jossa tarkoituksena on liikuttaa käärmettä kartalla ja kerätä kartalle satunnaisiin kohtiin ilmestyviä "omenoita". Käärme kasvaa yhden ruudun verran pidemmäksi aina, kun omena on kerätty. Jos käärme törmää kartan reunaan tai itseensä, peli päättyy. Jos käärme kasvaa koko ruudukon kokoiseksi, pelaaja voittaa pelin.

### Käyttöliittymä

Peli koostuu aloitusnäytöstä, ohjenäytöstä, varsinaisesta pelistä, sekä game over-näkymistä. Aloitusnäytöltä pääsee ohjeisiin klikkaamalla ohjeruutua, ja varsinaiseen peliin klikkaamalla start-ruutua. Pelin päättyessä ruudulle tulee game over-näkymä.

### Toiminnallisuus

- Pelin aloittaminen ja ohjenäkymään siirtyminen onnistuvat klikkaamalla oikeista kohdista aloitusnäytöllä tai game over-näytöllä.
- Pelissä käärme liikkuu itsestään. Liikkeen suuntaa voi muuttaa nuolinäppäimillä. -> Tehty
- "Omena" tulee kerätyksi, kun käärmeen pää kulkee samasta ruudusta, jossa "omena" sijaitsee. -> Tehty

### Jatkokehitys

Jos aikaa on riittävästi:

- Scores-näkymä, josta näkee kerättyjen "omenoiden" määrän pelikertaa kohden.
- High score-laskuri, joka päivittyy korkeimman pistemäärän mukaan.

