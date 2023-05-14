# Ohjelmistotekniikka, Pysnake

Pysnake on Pythonilla tehty versio tunnetusta snake-pelistä. Pelissä tarkoituksena on ohjata snakea ruudulla ja kerätä mahdollisimman paljon omenoita. Joka kerta kun snake syö omenan, snaken pituus kasvaa yhden ruudun verran. Jos snake törmää itseensä, tai johonkin ruudun reunoilla olevista seinistä, häviät pelin. Jos taas saat kerättyä niin paljon omenoita, että snake täyttää koko ruudun, voitat pelin.

## Dokumentaatio

[Käyttöohje](https://github.com/ThomasGrundstrom/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[vaatimusmaarittely.md](https://github.com/ThomasGrundstrom/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/ThomasGrundstrom/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/ThomasGrundstrom/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/ThomasGrundstrom/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


## Ohjelman komentorivikomennot:

**Aluksi pitää ladata tarvittavat riippuvuudet komellolla:** _**poetry install**_

- Ohjelman käynnistäminen toimii komennolla: **poetry run invoke start**
- Ohjelman testit suoritetaan komennolla: **poetry run invoke test**
- Testikattavuusraportti komennolla: **poetry run invoke coverage-report**
- Pylint-tarkistukset komennolla: **poetry run invoke lint**

