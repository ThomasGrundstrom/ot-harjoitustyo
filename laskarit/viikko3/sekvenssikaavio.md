```mermaid
 sequenceDiagram
	participant main
	participant Machine
	participant FuelTank
	Machine->>FuelTank: fill(40)
	participant Engine
	Machine->>Engine: __init__(FuelTank)
	main->>Machine: drive()
	Machine->>Engine: start()
	Engine->>FuelTank: consume(5)
	Machine->>Engine: is_running()
	Engine-->>Machine: True
	Machine->>Engine: use_energy()
	Engine->>FuelTank: consume(10)
	Machine-->>main
```
