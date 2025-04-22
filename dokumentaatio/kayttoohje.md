# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla *Assets*-osion alta *Source code*.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

`poetry install`

Tämän jälkeen suorita alustustoimenpiteet komennolla:

`poetry run invoke build`

Nyt ohjelman voi käynnistää komennolla:

`poetry run invoke start`

## Sisään kirjautuminen

Sovellus käynnistyy sisäänkirjautumisnäkymään:

![](Kuvat/Login.png)

Kirjautuminen onnistuu kirjoittamalla olemassa oleva käyttäjätunnus ja salasana niiden syötekenttiin ja painamalla "Login"-painiketta.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään painikkeella "Register".

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Register"-painiketta:

![](Kuvat/Register.png)

Jos käyttäjän luominen onnistuu, siirrytään takaisin sisään kirjautumis -näkymään.

## Liikuntasuoritusten tarkastelu

Kirjauduttua sisään pääset Sportstracker näkymään, jossa näkyy liikuntasuorituksesi.

Tästä näkymästä pääset luomaan uusia liikuntasuorituksia painamalla "New activity"-painiketta.

Olemassa olevia liikuntasuorituksia pääset muokkaamaan painamalla "Edit activities"-painiketta.

![](Kuvat/Sportstracker.png)

## Uuden liikuntasuorituksen luonti

Siirryttyäsi NewActivities näkymään Sportstracker näkymästä painamalla "New activity"-painiketta, pysty luomaan uusia liikuntasuorituksia täyttämällä annetut syötekentät haluamillasi tiedoilla ja painamalla sen jälkeen "Add activity"-painiketta.

![](Kuvat/NewActivities.png)

Pääset takaisin tarkastelemaan liikuntasuorituksiasi painamalla "Return to sportstracker"-painiketta.

## Liikuntasuorituksen poistaminen

Siirryttyäsi EditActivities näkymään Sportstracker näkymästä painamalla "Edit activities"-painiketta, pysty poistamaan liikuntasuorituksia painamalla kyseisen suorituksen kohdalta "Delete"-painiketta.

![](Kuvat/EditActivities.png)

Pääset takaisin Sportstracker näkymään painamalla "Return to sportstracker"-painiketta.
