## Luokkakaavio

![luokkakaavio](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/kuvat/luokkakaavio.jpg)

## Sekvenssikaavio

![sekvenssikaavio](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/kuvat/sekvenssikaavio1.png)

# Pelihahmon liikuttaminen

Nuolinäppäimen painamiseen reagoiva tapahtumankäsittelijä kutsuu player -luokan metodia move(), joka saa parametriksi pelaajan koordinaatteihin tapahtuvan muutoksen. Player -luokan metodi move() selvittää ensin voiko pelaaja siirtyä uuteen ruutuun. Jos pelaaja liikkui tyhjään lattiaruutuun tai ruutuun, jossa on suitsuke, metodi palauttaa False merkiksi, ettei pelaaja löytänyt ulos labyrintista. Jos pelaaja siityi lopetusruutuun, palauttaa metodi True. UI -luokan metodi play() jatkaa loopissa, joka piirtää näkyviin labyrintin, jossa pelaaja on siirtynyt uuteen ruutuun.
