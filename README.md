# Othello

Tietokonesovellus lautapelistä Othello

## Dokumentaatio

[Käyttöohje](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/dokumentaatio/testaus.md)

## Asennus

- Lataa uusin release [täältä](https://github.com/ArtturiV/ot-harjoitustyo/releases)

- Pura kansio haluamaasi paikkaan

- Suuntaa kansioon /othello/

- Suorita komento:

```bash
poetry install
```

## Käyttö

Komentorivikomennot toimivat vain kansiossa /othello/

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
