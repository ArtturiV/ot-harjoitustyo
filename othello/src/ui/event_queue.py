import pygame


class EventQueue:
    """Luokka hakee pelaajan syötteet.
    """

    def get(self):
        """Hakee ja palauttaa tapahtuman

        Returns:
            pygame.event: Pelaajan syöte
        """
        return pygame.event.get()
