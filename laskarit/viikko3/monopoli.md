```mermaid
 classDiagram
	Monopoli "1" --> "2..8" Pelaaja
	Pelaaja "1" --> "1" Pelinappula
	Monopoli "1" --> "1" Pelilauta
	Pelilauta "1" --> "40" Ruutu
	Pelinappula "*" --> "1" Ruutu

	class Pelaaja{
		Pelinappula
		heita_noppaa()
	}
	class Ruutu{
		numero
		seuraava_ruutu()
	}
	class Pelinappula
		vari
		Ruutu
	}	
```
