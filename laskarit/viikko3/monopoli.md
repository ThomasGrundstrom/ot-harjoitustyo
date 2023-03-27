<script src="https://cdn.jsdelivr.net/npm/mermaid@8.11.0/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>

```mermaid
 classDiagram
	Pelilauta <|-- Pelaaja
	Pelilauta <|-- Ruutu
	Pelilauta <|-- Nopat
	class Pelaaja{
		+String pelinappula
		+int ruutu
	}
	class Ruutu{
		+int numero
		+int seuraava
	}
	class Nopat{
		+int arvo
	}
```
