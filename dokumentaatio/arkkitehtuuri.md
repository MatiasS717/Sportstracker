# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria.

- UI
- Backend
- Database

UI vastaa sovelluksen käyttöliittymästä, Backend SQL-komennoista, sekä Database tietokannasta.

## Käyttöliittymä

Käyttöliittymä sisältää viisi erilaista näkymää:

- Kirjautuminen.
- Uuden käyttäjän luominen.
- Sportstracker-näkymä.
- Uusien liikuntasuoritusten lisäys.
- Käyttäjän liikuntasuoritusten muokkaus.

Jokainen käyttöliittymän osa on omassa tiedostossaan ja muodostaa oman luokkansa. Näkymistä vain yksi näkyy kerrallaan. UI-luokka vasta eri näkymien näyttämisestä vuorollaan.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat tietokannan taulujen entiteetit User ja Activity, jotka kuvaavat käyttäjiä ja käyttäjien liikuntasuorituksia.

```mermaid
 classDiagram
      Activity "*" --> "1" User
      class User{
          username
          password
      }
      class Activity{
          id
          activity
          tracker
	  training_type
      }
```

Toiminnallisista kokonaisuuksista vastaa Backend, joka jakautuu komentojen osalta users-commands ja activities-commands tiedostoihin.

users-commands tiedoston käskyjä ovat esimerkiksi:

`login(username, password)`

`register(username, password)`

activities-commands tiedoston käskyjä ovat esimerkiksi:

`add-activity(activity, tracker, training-type, user-id)`

`delete-activity(activity, tracker, training-type, user-id)`

## Tietojen pysyväistallennus

Backend hoitaa tietojen tallennuksen SQLite-tietokantaan luomalla tietokannan ja taulut tietokantaan build.py tiedostossa. db.py hoitaa yhteyden luonnin tietokantaan ja activities-commands, sekä users-commands tiedostot toteuttavat SQL-komennot. Käyttäjät tallennetaan database.db tiedoston tauluun `users` ja liikuntasuoritukset tauluun `activities`.

## Päätoiminnallisuudet

### Sisäänkirjautuminen

Kun kirjautumisnäkymän syötekenttiin kirjoitetaan käyttäjätunnus ja salasana, minkä jälkeen klikataan painiketta Login, etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant users_commands
  participant database
  User->>UI: click "Login" button
  UI->>users_commands: login("Pekka", "12345")
  users_commands->>database: login("Pekka", "12345")
  database-->>users_commands: user
  users_commands-->>UI: user
  UI->UI: _show_sportstracker_view()
```

Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan users_commands funktiota login antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää tietokannasta onko käyttäjätunnus olemassa ja täsmääkö salasanat. Jos nämä asiat onnistuvat, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi Sportstracker, eli sovelluksen varsinaisen päänäkymän ja näyttää käyttäjälle hänen liikuntasuorituksensa. 

### Uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus, joka ei ole jo käytössä, sekä salasanat, jotka täsmäävät keskenään, minkä jälkeen klikataan "Register" etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant users_commands
  participant database
  User->>UI: click "Register" button
  UI->>users_commands: try:register("Pekka", "12345")
  users_commands-->>UI: no IntegrityError
  UI->>users_commands: register("Pekka", "12345")
  users_commands->>database: register("Pekka", "12345")
  UI->UI: _show_login_view()
```

Tapahtumakäsittelijä kutsuu users_commands tiedoston funktiota register antaen parametreiksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää onko käyttäjätunnus jo olemassa tietokannassa. Jos käyttäjää ei löydy, luodaan tietokantaan uusi käyttäjä. Tämän jälkeen käyttöliittymä vaihtaa näkymäksi Login, josta uudella käyttäjällä voidaan kirjautua sisään. 

### Liikuntasuorituksen luominen

Uuden liikuntasuorituksen luovan "Add activity"-painikkeen klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant activities_commands
  participant database
  User->>UI: click "Add activity" button
  UI->>activities_commands: get_activities(user_id)
  activities_commands-->>UI: activities
  UI->>activities_commands: if activity not in activities:add_activity("Running", 5, "Endurance", user_id)
  activities_commands->>database: add_activity("Running", 5, "Endurance", user_id
  UI->UI: message:"You successfully added an activity"
```

Tapahtumakäsittelijä kutsuu activities-commands tiedoston funktiota get-activities, minkä jälkeen tarkastetaan onko kyseisellä käyttäjällä olemassa jo kyseinen liikuntasuoritus. Jos ei ole, kutsutaan funktiota add_activity, mikä lisää liikuntasuorituksen tietokantaan. Lopuksi käyttöliittymä kertoo viestillä onnistuneesti lisätystä liikuntasuorituksesta.

### Liikuntasuorituksen poistaminen

Liikuntasuorituksen poistavan "Delete" painikkeen klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant activities_commands
  participant database
  User->>UI: click "Delete" button
  UI->>activities_commands: delete_activity("Running", 5, "Endurance", user_id)
  activities_commands->>database: delete_activity("Running", 5, "Endurance", user_id)
  UI->UI: destroy(),edit_activities_start(),pack()
```

Tapahtumakäsittelijä kutsuu activities-commands tiedoston funktiota delete_activity antaen parametriksi poistettavan liikuntasuorituksen tiedot. Komento poistaa liikuntasuorituksen tietokannasta. Tämän jälkeen UI käynnistää näkymän uudestaan, jotta sivun lista liikuntasuorituksista päivittyy.
