# Testausdokunmentti

## Yksikkötestaus

### Laudan toiminta

Laudan toiminnasta vastaa `Board`-luokka, jonka testaus tapahtuu [TestBoard](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/src/tests/board_test.py)-luokassa.

### Syötteiden tulkinta

Pelaajan antamia syötteitä tulkitsee `GameInterface`-luokka.
Luokkaa testataan [TestGameInterface](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/src/tests/game_interface_test.py)-luokassa. Luokalle annetaan `Board`-luokan olio

### Pelisilmukka

Pelisilmukasta vastaavaa `GameLoop`-luokkaa testataan [TestGameLoop](https://github.com/ArtturiV/ot-harjoitustyo/blob/master/othello/src/tests/game_loop_test.py)-luokassa.
Koska `GameLoop` vastaa käyttäjän syötteiden lukemisesta emmekä voi testatessa antaa sille syötteitä, on käytettävä valekomponentteja.
Luokalle injektoiduista riippuvuuksista `StubRenderer` ja `StubClock` eivät tee mitään,
`StubGameInterface` palauttaa annetuista koordinaateista huolimatta määrittelemämme arvon ja `StubEventQueue` palauttaa määrittelemämme eventin.

### Testauskattavuus

Testattujen luokkien haaraumakattavuus on 92%.

![CoverageReport](https://user-images.githubusercontent.com/61615435/209342892-ef7b8db7-5da5-4bb4-ace9-f319d9102714.png)

Koska `GameLoop`-luokka lukee käyttäjän syötteitä, ei siinä päästy 100% haaraumakattavuuteen. 
Esimerkiksi ei hiiren koordinaatteihin voinut vaikuttaa ja täten ei päästy testaamaan aputilan nappulan toimintaa.

## Järjestelmätestaus

### Asennus

Sovelluksen asennus on suoritettu käyttöohjeen mukaan Linux-ympäristössä.

### Toiminnallisuudet

Kaikki listatut toiminnallisuudet on todettu toimiviksi eikä virhetilanteita tullut vastaan.
