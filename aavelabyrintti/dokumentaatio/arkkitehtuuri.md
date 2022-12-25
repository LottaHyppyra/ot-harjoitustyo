# Käyttöliittymä

Käyttöliittymässä on useampi eri näkymä.

- Aloitusvalikko
- Ohjeet
- Tulostaulu
- Peli
    - Ennen pelin alkua kysytään pelaajan nimeä omassa näkymässään. 

Käyttöliittymän eri näkymät on toteutettu tiedostossa src/ui/main.py luokassa Game().

# Luokkakaavio

![luokkakaavio](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/kuvat/luokkakaavio.jpeg)

# Sekvenssikaaviot

## Pelihahmon liikuttaminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Player
  participant Ghost
  UI->>UI: play()
  User->>UI: press arrow key down
  UI->>Player: move(0,1)
  Player-->>UI: False
  UI->>Ghost: move(16,20)
  UI->>UI: play()
  ```

Nuolinäppäimen painamiseen reagoiva tapahtumankäsittelijä kutsuu player -luokan metodia move(), joka saa parametriksi pelaajan koordinaatteihin tapahtuvan muutoksen. Player -luokan metodi move() selvittää ensin voiko pelaaja siirtyä uuteen ruutuun. Jos pelaaja liikkui tyhjään lattiaruutuun tai ruutuun, jossa on suitsuke, metodi palauttaa False merkiksi, ettei pelaaja löytänyt ulos labyrintista. Jos pelaaja on liikkunut eikä käyttänyt suitsuketta, kutsutaan ghost luokan metodia(move), joka saa parametrikseen pelaajan uudet koordinaatit. UI -luokan metodi play() jatkaa loopissa, joka piirtää näkyviin labyrintin, jossa pelaaja ja aave ovat siirtyneet uusiin ruutuihin.

## Pelihahmo siirtyy maaliruutuun

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Player
  participant Results
  participant ResultsRepository
  UI->>UI: play()
  User->>UI: press arrow key down
  UI->>Player: move(0,1)
  Player-->>UI: True
  UI->>UI: print_won()
  UI->>Results: add_result("Pelaaja", 50)
  Results->>ResultsRepository: add_result_to_database("Pelaaja", 50)
```
Nuolinäppäimen painamiseen reagoiva tapahtumankäsittelijä kutsuu player -luokan metodia move(), joka saa parametriksi pelaajan koordinaatteihin tapahtuvan muutoksen. Player -luokan metodi move() selvittää ensin voiko pelaaja siirtyä uuteen ruutuun. Jos pelaaja liikkui maaliruutuun, metodi palauttaa True merkiksi, että pelaaja on löytänyt ulos labyrintista. UI -luokan metodi play() jatkaa loopissa, joka kutsuu saman luokan metodia print_won(), mikä piirtää voittonäkymän. Jos pelaaja on antanut nimen pelin alussa, kutsuu UI luokka Results luokan add_result() metodia, joka saa parametreikseen pelaajan nimen ja kierroksen siirtojen määrän. Results -luokka kutsuu vielä results_repository luokan metodia add_result_to_database(), mikä saa parametreikseen pelaajan nimen ja siirtojen määrän, ja lisää tuloksen tietokantaan.
