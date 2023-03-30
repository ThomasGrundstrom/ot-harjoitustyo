```mermaid
 sequenceDiagram
	main->>Machine: drive()
	Machine->>Engine: start()
	Engine->>FuelTank: consume(5)
```
