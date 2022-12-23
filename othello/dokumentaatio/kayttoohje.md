# Käyttöohje

## Othellon säännöt

Musta aloittaa pelin.
Pelaajat asettavat vuorotellen nappuloitaan tyhjiin ruutuihin.
Nappula on asetettava siten, että se rajaa vastustajan nappuloita omien nappuloiden väliin.
Näin rajatut nappulat vaihtuvat pelaajan nappuloiden värisiksi.
Jos vain toisella pelaajista ei ole laillisia siirtoja hypätään pelaajan vuoron ohi.
Peli loppuu, kun kummallakaan pelaajalla ei ole enää laillisia siirtoja.
Pelin voittaa pelaaja, jolla on lopuksi enemmän nappuloita laudalla.

## Asennus

- Lataa uusin release [täältä](https://github.com/ArtturiV/ot-harjoitustyo/releases)
- Pura kansio haluamaasi paikkaan
- Suuntaa kansioon /othello/
- Suorita komento: `poetry install`
- Sovellus käinnystyy komennolla `poetry run invoke start`

## Pelilaudan lukeminen

1. Aktiivinen pelaaja näkyy alapalkista
2. Aputilaa vaihtava nappi
3. Pelaajien nappuloiden määrä
4. Laillinen siirto näkyy sinisellä, jos aputila on päällä
5. Ohjelman saa suljettua ruksia painamalla

![kayttoohjesmall](https://user-images.githubusercontent.com/61615435/207054389-97c2421b-0041-44c5-a2bb-a4b03c08c014.png)

## Pelaaminen

- Siirtoja tehdään ruutuja klikkaamalla.
- Aputilan saa päälle ja pois aputila-palkkia klikkaamalla.
- Tekstilaatikot saa ohitettua klikkaamalla.
- Pelin saa suljettua ikkunan ruksia painamalla.
