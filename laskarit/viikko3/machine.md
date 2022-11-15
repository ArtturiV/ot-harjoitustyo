```mermaid
 sequenceDiagram
	participant mn as Main
	participant mc as Machine
	participant f as FuelTank
	participant e as Engine

	mn->>mc: Machine()
	activate mc
	mc->>f: FuelTank()
	mc->>f: fill(40)
	mc->>e: Engine(tank)
	mc-->>mn:
	deactivate mc
	mn->>mc: drive()
	mc activate
	mc->>e: start()
	activate e
	e->>f: consume(5)
	e-->>mc:
	deactivate e
	mc->>e: is_running()
	activate e
	e->>f: fuel_contents
	f-->>e: 35
	e-->>mc: True
	deactivate e
	mc->>e: use_energy()
	activate e
	e->>f: consume(10)
	e-->>mc:
	deactivate e
	mc-->>mn:
	deactivate mc	
```
