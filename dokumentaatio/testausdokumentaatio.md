# Testausdokumentti

Pysnaken testaus on suoritettu automatisoidulla unittestillä sekä manuaalisesti.


### Testit

Automaattiset *poetry run invoke test*-komennolla suoritettavat testit löytyvät [testikansiosta](https://github.com/ThomasGrundstrom/ot-harjoitustyo/tree/master/src/tests)


### Testikattavuus

Automaattisten testien kattavuus on 68%. Testauksessa ei oteta huomioon index.py-tiedostoa, eikä testikansiota itseään.

![](./kuvat/testcoverage.png)

Pygamea käyttävien luokkien testaaminen osoittautui haastavaksi käyttäen unittestiä, mutta testikattavuutta saisi todennäköisesti lisättyä vielä jonkin verran.


### Laatuongelmat

Pysnakeen ei ole tehty virheilmoituksia, koska ohjelman manuaalinen testaus on osoittanut, että ohjelma ei kaadu. Ohjelman toiminnallisuus on sen verran yksinkertainen, että koodia silmäilemällä voi nähdä ettei virhetilanteita synny ohjelman suorituksen aikana.
