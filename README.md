# Othello

Tietokonesovellus lautapelistä Othello

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/arkkitehtuuri.md)

## Release

### Asennus

- Lataa release [täältä](https://github.com/ArtturiV/ot-harjoitustyo/releases/tag/viikko5)

- Pura kansio haluamaasi paikkaan

- Suuntaa kansioon /ot-harjoitustyo-viikko5/othello/

- Suorita komento:

```bash
poetry install
```

### Käyttö

- Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

- Peliä pelataan ruutuja hiirellä klikkaamalla

- Sovellus suljetaan pygame-ikkunan ruksia painamalla

- Sovelluksen testit voi ajaa komennolla:

```bash
poetry run invoke test
```

- Testikattavuusraportin saa luotua komennolla:

```bash
poetry run invoke coverage-report
```

- Pylint-tarkistukset saa tehtyä komennolla:

```bash
poetry run invoke lint
```
