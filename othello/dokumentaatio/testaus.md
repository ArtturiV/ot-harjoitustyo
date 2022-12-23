# Testausdokunmentti

## Yksikkötestaus

### Laudan toiminta

Laudan toiminnasta vastaa `Board`-luokka, jonka testaus tapahtuu TestBoard-luokassa.

### Syötteiden tulkinta

Pelaajan antamia syötteitä tulkitsee `GameInterface`-luokka.
Luokkaa testataan TestGameInterface-luokassa. Luokalle annetaan `Board`-luokan olio

### Pelisilmukka

Pelisilmukasta vastaavaa `GameLoop`-luokkaa testataan TestGameLoop-luokassa.
Koska `GameLoop` vastaa käyttäjän syötteiden lukemisesta emmekä voi testatessa antaa sille syötteitä, on käytettävä valekomponentteja.
Luokalle injektoiduista riippuvuuksista `StubRenderer` ja `StubClock` eivät tee mitään,
`StubGameInterface` palauttaa annetuista koordinaateista huolimatta määrittelemämme arvon ja `StubEventQueue` palauttaa määrittelemämme eventin.

### Testauskattavuus

Testattujen luokkien haaraumakattavuus on 92%.

Koska `GameLoop`-luokka lukee käyttäjän syötteitä, ei siinä päästy 100% haaraumakattavuuteen. 
Esimerkiksi ei hiiren koordinaatteihin voinut vaikuttaa ja täten ei päästy testaamaan aputilan nappulan toimintaa.

## Järjestelmätestaus

# Asennus

Sovelluksen asennus on suoritettu käyttöohjeen mukaan Linux-ympäristössä.

# Toiminnallisuudet

Kaikki listatut toiminnallisuudet on todettu toimiviksi eikä virhetilanteita tullut vastaan.
