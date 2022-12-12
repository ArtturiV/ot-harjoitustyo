# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne on kaksitasoinen kerrosarkkitehtuuri.

```mermaid
 classDiagram
	ui ..> logic
```

Käyttöliittymästä vastavaa koodi on pakkauksessa ui ja sovelluslogiikasta vastaava pakkauksessa logic.

## Käyttöliittymä

Sovellukselle on tehty graafinen käyttöliittymä.

Sovellusta ohjataan hiirtä klikkaamalla, jolloin _gameinterface_ muuttaa pelin tilaa ja _renderer_ päivittää pelin ruudun.

## Sovelluslogiikka

_GameInterface_ ottaa _GameLoopilta_ vastaan klikkausten koordinaatteja ja antaa ne laudalle käsiteltäväksi.

```mermaid
 classDiagram
	GameLoop "1" --> "1" GameInterface
	GameInterface "1" --> "1" Board
	class GameLoop{
		handle_events()
	}
	class GameInterface{
		handle_click()
	}
	class Board{
		board_state
		player
		legal_list
		change_player()
		set_state()
		check_end()
		check_tally()
		make_move()
		legal_moves()
	}
```

Yhden siirron pelaaminen sekvenssikaaviona

```mermaid
 sequenceDiagram
	participant gl as gameloop
	participant eq as eventqueue
	participant gi as gameinterface
	participant b as board
	participant r as renderer
	participant c as clock

	gl->>eq: get()
	activate eq
	eq-->>gl: pygame.MOUSEBUTTONUP
	deactivate eq
	gl->>gi: handle_click(pygame.mouse.get_pos())
	activate gi
	gi->>b: make_move(x_coord, y_coord)
	activate b
	b-->>gi: True
	deactivate b
	gi->>b: change_player()
	gi->>b: legal_moves()
	activate b
	b-->>gi: moves
	deactivate b
	gi-->>gl: 0
	deactivate gi
	gl->>r: render()
	gl->>c: get_ticks(60)
	activate c
	c-->>gl: pygame.time.get_ticks()
	deactivate c
```
