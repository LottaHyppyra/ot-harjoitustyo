# Aavelabyrintti

Aavelabyrintissa pelaajan tulee löytää ulos labyrintista jäämättä kiinni siellä liikkuvalle aaveelle. 

## Dokumentaatio

- [Työaikakirjanpito.md](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmaarittely.md](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/LottaHyppyra/ot-harjoitustyo/blob/master/aavelabyrintti/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot

Ohjelman suorittaminen:

```bash
poetry run invoke start
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
