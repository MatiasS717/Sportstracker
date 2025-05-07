# Testausdokumentti

Ohjelmaa on testattu unittestin avulla.

## Testikattavuus

Sovelluksen testauksen haarautumakattavuus on 97%. Testaus ei sisältänyt käyttöliittymän tiedostoja.

![](Kuvat/Testikattavuus.png)

Tiedostoille activities-commands.py, users-commands.py, sekä build.py on omat testitiedostonsa. db.py tiedostoa käytetään activities-commands ja users-commands tiedostoissa, joten sen testaus tapahtui näiden tiedostojen kautta. build.py tiedoston testaus kattoi pienen osan activities-commands ja users-commands tiedostojen funktioiden testaamisesta.
