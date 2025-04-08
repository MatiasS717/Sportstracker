# Ohjelmistotekniikka harjoitustyö
## Kuvaus
**Sovelluksen** avulla käyttäjien on mahdollista pitää kirjaa tekemistään *liikuntasuorituksista*. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen liikuntasuorituslistansa.

## Dokumentaatio
- [Työaikakirjanpito](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet komennolla:

`poetry install`

2. Suorita vaadittavat alustustoimenpiteet komennolla:

`poetry run invoke build`

3. Käynnistä sovellus komennolla:

`poetry run invoke start`

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:

`poetry run invoke start`

### Testaus
Testit suoritetaan komennolla:

`poetry run invoke test`

### Testikattavuus
Testikattavuusraportin voi generoida komennolla:

`poetry run invoke coverage-report`

### Koodin laatu
Koodin laatua voi testata komennolla:

`poetry run invoke lint`

