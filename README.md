# Aavelabyrintti

Aavelabyrintissa pelaajan tulee löytää ulos labyrintista jäämättä kiinni siellä liikkuvalle aaveelle. 

## Dokumentaatio

- [Loppupalautus](https://github.com/LottaHyppyra/ot-harjoitustyo/releases/tag/loppupalautus)

- [Työaikakirjanpito](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmäärittely](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/arkkitehtuuri.md)

- [Käyttöohje](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/kayttoohje.md)

## Asennus

1. Asenna pelin vaatimat riippuvuudet:

```bash
poetry install
```

2. Alusta tietokanta:

```bash
poetry run invoke build
```

3. Käynnistä peli:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Ohjelman suorittaminen:

```bash
poetry run invoke start
```

Tietokannan alustaminen:

```bash
poetry run invoke build
```

Testien ajaminen:

```bash
poetry run invoke test
```

Testikattavuusraportti: 

```bash
poetry run invoke coverage-report
```
Pylint:

```bash
poetry run invoke lint
```
