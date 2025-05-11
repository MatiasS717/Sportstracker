# Ohjelmistotekniikka harjoitustyö
## Kuvaus
**Sovelluksen** avulla käyttäjien on mahdollista pitää kirjaa tekemistään *liikuntasuorituksista*. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen liikuntasuorituslistansa.

## Releases

- [Viikko5](https://github.com/MatiasS717/ot-harjoitustyo/releases/tag/Viikko5)
- [Viikko6](https://github.com/MatiasS717/ot-harjoitustyo/releases/tag/Viikko6)
- [Loppupalautus](https://github.com/MatiasS717/Sportstracker/releases/tag/loppupalautus)

## Dokumentaatio
- [Työaikakirjanpito](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/MatiasS717/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/MatiasS717/Sportstracker/blob/main/dokumentaatio/testaus.md)

## Asennus
1. Pystyt asentamaan riippuvuudet komennolla:

`poetry install`

2. Suorita alustustoimenpiteet komennolla:

`poetry run invoke build`

3. Sovelluksen käynnistys komennolla:

`poetry run invoke start`

## Komentorivitoiminnot

### Ohjelman käynnistäminen
Ohjelman pystyy käynnistämään komennolla:

`poetry run invoke start`

### Testaus
Testit voit suorittaa komennolla:

`poetry run invoke test`

### Testikattavuus
Testikattavuusraportin saa komennolla:

`poetry run invoke coverage-report`

### Koodin laatu
Koodin laatua voi testata komennolla:

`poetry run invoke lint`
