# Arkkitehtuurikuvaus

## Käyttöliittymä

Ohjelma koostuu seuraavista näkymistä:

- Alkuvalikko
- Pelinäkymä
- Voittonäkymä
- Häviönäkymä

Näkymät on toteutettu Screen-luokan metodeina ja jokin niistä on aina ruudulla. Näkymien näyttämisestä ja vaihtamisesta vastaa Screen-luokka.

Kun sovellus käynnistetään, ensimmäisenä näkyviin tulee alkuvalikko. Alkuvalikosta siirrytään pelinäkymään painamalla valikossa olevaa play-näppäintä. Pelitilasta pääsee voittonäkymään vain voittamalla pelin, eli kasvattamalla snaken koko ruudun kokoiseksi. Pelitilasta häviönäkymään siirtyminen tapahtuu, jos snake törmää johonkin ruudun reunoilla olevista seinistä tai itseensä.


## Luokkakaavio:

Ohjelma koostuu luokista Screen, Startmenuactions, Gamemap, Actions, Snake, Apple ja Scorecounter. Ohjelman luokkakaavio näyttää seuraavalta:

```mermaid
 classDiagram
	Screen <|-- Gamemap
	Screen <|-- Scorecounter
	Screen <|-- Startmenuactions
	Gamemap <|-- Actions
	Gamemap <|-- Scorecounter
	Actions <|-- Snake
	Gamemap <|-- Snake
	Snake <|-- Apple
	Gamemap <|-- Apple
	Apple <|-- Scorecounter
	class Screen{
		+pygame
		+screen
		+clock
		+draw_screen()
		+loop()
		+wingame()
		+losegame()
		+startscreen()
		+draw_art()
	}
	class Gamemap{
		+List grid
		+List zeros
		+updateavailable()
		+update()
		+restart()
	}
	class Actions{
		+pygame
		+check_actions()
	}
	class Snake{
		+int x
		+int y
		+int direction
		+bool moving
		+bool changeddirections
		+List positions
		+moveup()
		+movedown()
		+moveleft()
		+moveright()
		+move_snake()
		+set_stationary()
	}
	class Apple{
		+int y
		+int x
		+List available
		+set_available()
		+spawn()
	}
	class Scorecounter{
		+int score
		+add_score()
	}
	class Startmenuactions{
		+pygame
		+check_actions()
	}

```


## Sekvenssikaavio:

Tilanteessa, jossa käyttäjä käynnistää pelin ja ohjaa snaken ensimmäiselle omenalle mahdollisimman pienellä määrällä käännöksiä, ohjelman toiminnallisuus näyttää seuraavalta:

```mermaid
 sequenceDiagram
	actor User
	participant game
	participant Screen
	participant Gamemap
	participant Actions
	participant pygame
	participant Snake
	participant Apple
	participant Scorecounter
	User->>game: poetry run invoke start
	game->>Screen: loop()
	User->>pygame: K_RIGHT
	loop Until screen updates when snake has x value of 7
	Screen->>Gamemap: update()
	Gamemap->>Actions: check_actions()
	Actions->>pygame: event.get()
	pygame-->>Actions: 
	Actions-->>Gamemap: 
	Gamemap->>Snake: move_snake()
	Snake-->>Gamemap: 
	Gamemap->>Gamemap: updateavailable()
	Gamemap->>Apple: set_available(zeros)
	Apple-->>Gamemap: 
	Gamemap-->>Screen: grid
	Screen->>Screen: draw_screen()
	end
	User->>pygame: K_DOWN
	Screen->>Gamemap: update()
	Gamemap->>Actions: check_actions()
	Actions->>pygame: event.get()
	pygame-->>Actions: pygame.K_DOWN
	Actions->>Snake: movedown()
	Snake-->>Actions: 
	Actions-->>Gamemap: 
	Gamemap->>Snake: move_snake()
	Snake-->>Gamemap: 
	Gamemap-->>Screen: grid
	Screen->>Screen: draw_screen()
	loop Until screen updates when snake has y value of 6
	Screen->>Gamemap: update()
	Gamemap->>Actions: check_actions()
	Actions->>pygame: event.get()
	pygame-->>Actions: 
	Actions-->>Gamemap: 
	Gamemap->>Snake: move_snake()
	Snake-->>Gamemap: 
	Gamemap->>Gamemap: updateavailable()
	Gamemap->>Apple: set_available(zeros)
	Apple-->>Gamemap: 
	Gamemap-->>Screen: grid
	Screen->>Screen: draw_screen()
	end
	Screen->>Gamemap: update()
	Gamemap->>Actions: check_actions()
	Actions->>pygame: event.get()
	pygame-->>Actions: 
	Actions-->>Gamemap: 
	Gamemap->>Snake: move_snake()
	Snake->>Apple: spawn()
	Apple->>Scorecounter: add_score()
	Apple-->>Snake: available[position]
	Snake-->>Gamemap: 
	Gamemap->>Gamemap: updateavailable()
	Gamemap->>Apple: set_available(zeros)
	Apple-->>Gamemap: 
	Gamemap-->>Screen: grid
	Screen->>Screen: draw_screen()

```


## Muut toiminnallisuudet

Ohjelma toimii samalla tavalla kunnes peli hävitään tai voitetaan. Näissä tilanteissa snakemap-luokan tila päivittyy ja screen-luokka näyttää pelin loppunäkymän. Jos peli aloitetaan alusta R-näppäimellä, snakemap-luokka huolehtii tarvittavien arvojen nollaamisesta.


## Rakenteen heikkoudet

Ohjelman koodi oltaisiin voitu jakaa useampaan pienempään luokkaan. Tämänhetkisessä tilanteessa ohjelmassa on luokkia, jotka huolehtivat turhan monesta eri asiasta. Lisäksi pylint-virheitä on melko paljon.
