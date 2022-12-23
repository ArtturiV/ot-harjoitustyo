import pygame


class GameLoop:
    """Pelisilmukka, joka lukee pelaajan syötteet ja päivittää pelin tilan.

    Attributes:
        game_state: Muuttuja kuvaa missä tilassa peli on.
        0 = peli jatkuu normaalisti
        1 = Ei laillisia siirtoja, vuoro vaihtuu
        2 = Musta voitti, peli loppuu
        3 = Valkoinen voitti, peli loppuu
        4 = Tasapeli, peli loppuu
        help_mode: Onko pelin aputila päällä vai ei
    """

    def __init__(self, gameinterface, clock, renderer, event_queue):
        """Luokan konstruktori

        Args:
            gameinterface (olio): Pelilaudan kanssa keskustelevan luokan olio
            clock (olio): Pelin kello
            renderer (olio): Pelin renderöinnistä vastaava olio
            event_queue (olio): Pelaajan syötteet lukeva olio
        """
        self.gameinterface = gameinterface
        self.clock = clock
        self.renderer = renderer
        self.event_queue = event_queue
        self.game_state = 0
        self.help_mode = False

    def start(self):
        """Käynnistää pelisilmukan. Ensin silmukka lukee pelaajan syötteen.
        Jos syöte on False katkeaa silmukka ja peli sulkeutuu, muuten toimitaan syötteen mukaan.
        Syötteen lukemisen jälkeen tarkistetaan missä tilassa peli on. Jos peli on tilassa 0 eli
        peli jatkuu normaalisti, renderöidään peli, kutsutaan kelloa ja silmukka alkaa alusta.
        Jos pelin tila on joku muu kuin 0 renderöidään pelin tilaa vastaava viesti ja jatketaan.
        Pelin tilan ollessa 2, 3 tai 4 on peli päättynyt ja peli lopetetaan.
        """
        while True:
            if self._handle_events() is False:
                break
            if self.game_state > 0:
                if self._render_state(self.game_state) is False:
                    break
                if self.game_state > 1:
                    break
                self.game_state = 0
            self._render()
            self.clock.tick(60)

    def _handle_events(self):
        """Metodi lukee käyttäjän syötteen. Jos syöte on hiiren klikkaus,
        tarkistetaan onko klikkaus pelilaudalla. Jos syöte on pelilaudalla,
        annetaan se gameinterface oliolle tulkittavaksi ja annetaan game_state
        muuttujalle uusi arvo. Jos klikkaus ei ole pelilaudalla, tarkoittaa
        se että pelaaja on klikannut laudan alla olevaa palkkia ja asetetaan
        pelin aputila päälle tai pois. Mikäli pelaaja klikkaa pygame-ikkunan
        rastia, palauttaa metodi False.

        Returns:
            Boolean: False jos pelaaja klikkaa ruksia, muuten True
        """
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] < 811:
                    self.game_state = self.gameinterface.handle_click(
                        mouse_pos)
                else:
                    self.help_mode = not self.help_mode
            elif event.type == pygame.QUIT:
                return False
        return True

    def _handle_state(self):
        """Hoitaa syötteiden lukemisen, kun pelin ruudulla näkyy viesti.

        Returns:
            int: 1 = ohita viesti, 2 = lopeta peli
        """
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return 1
            if event.type == pygame.QUIT:
                return 2
        return 0

    def _render(self):
        """Kehottaa renderer-oliota renderöimään pelin.
        """
        self.renderer.render(self.help_mode)

    def _render_state(self, state):
        """Renderöi pelin tilaa vastaavan viestin. Viesti näkyy ruudulla
        kolmen sekunnin ajan tai kunnes pelaaja klikkaa.
        Esimerkiksi "Musta voitti"

        Args:
            state (int): Pelin tila

        Returns:
            Boolean: False jos peli lopetetaan, muuten True
        """
        self._render()
        self.renderer.render_state(state)
        start_time = self.clock.get_ticks()
        current_time = self.clock.get_ticks()
        event = 0
        while current_time - start_time < 3000:
            current_time = self.clock.get_ticks()
            event = self._handle_state()
            if event > 0:
                break
        if event == 2:
            return False
        return True
