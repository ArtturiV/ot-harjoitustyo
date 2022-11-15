```mermaid
 sequenceDiagram
	participant m as main
	participant lh as laitehallinto
	participant rtt as rautatietori
	participant r6 as ratikka6
	participant b244 as bussi244
	participant ll as lippu_luukku
	participant kk as kallen_kortti

	m->>lh: HKLLaitehallinto()
	m->>rtt: Lataajalaite()
	m->>r6: Lukijalaite()
	m->>b244: Lukijalaite()
	m->>lh: lisaa_lataaja(rautatientori)
	m->>lh: lisaa_lukija(ratikka6)
	m->>lh: lisaa_lukija(bussi244)
	m->>ll: Kioski()
	m->>ll: osta_matkakortti("Kalle")
	activate ll
	ll->>kk: Matkakortti(Kalle)
	ll-->>m: return
	deactivate ll
	m->>rtt: lataa_arvoa(kallen_kortti, 3)
	activate rtt
	rtt->>kk: kasvata_arvoa(3)
	rtt-->>m: return
	deactivate rtt
	m->>r6: osta_lippu(kallen_kortti, 0)
	activate r6
	r6->>kk: kortti.arvo
	activate kk
	kk-->>r6: 3
	deactivate kk
	r6->>kk vahenna_arvoa(1.5)
	r6-->>m: True
	deactivate r6
	m->>b244: osta_lippu(kallen_kortti, 2)
	activate b244
	b244->>kk: kortti.arvo
	activate kk
	kk-->>b244: 1.5
	deactivate kk
	b244-->>m: False
```
