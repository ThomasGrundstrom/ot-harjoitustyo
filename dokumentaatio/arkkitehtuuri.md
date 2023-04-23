## Luokkakaavio:

```mermaid
 classDiagram
	Screen <|-- Gamemap
	Gamemap <|-- Actions
	Actions <|-- Snake
	Gamemap <|-- Snake
	Snake <|-- Apple
	Gamemap <|-- Apple
	class Screen{
		+pygame
		+screen
		+clock
		+draw_screen()
		+loop()
	}
	class Gamemap{
		+List grid
		+List zeros
		+updateavailable()
		+update()
	}
	class Actions{
		+pygame
		+check_actions()
	}
	class Snake{
		+int x
		+int y
		+bool up
		+bool down
		+bool left
		+bool right
		+List positions
		+moveup()
		+movedown()
		+moveleft()
		+moveright()
		+move_snake()
	}
	class Apple{
		+int y
		+int x
		+List available
		+set_available()
		+spawn()
	}

```


## Sekvenssikaavio:

```mermaid
 sequenceDiagram
	participant game
	participant Screen
	participant Gamemap
	participant Actions
	participant pygame
	participant Snake
	participant Apple
	game->>Screen: loop()
	Screen->>Gamemap: update()
	Gamemap->>Actions: check_actions()
	Actions->>pygame: event.get()
	pygame-->>Actions:
	Actions-->>Gamemap:
	Gamemap->>Snake: move_snake()
	Snake-->>Gamemap:
	Gamemap-->>Gamemap: updateavailable()
	Gamemap->>Apple: set_available(zeros)
	Apple-->>Gamemap:
	Gamemap-->>Screen: grid
	Screen-->>Screen: draw_screen()

```
