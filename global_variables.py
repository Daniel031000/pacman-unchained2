  # duration of the eating animation in game ticks
screensize = (1000, 500)
keys_pressed = []
pacman = 0


def pixel_colour(playerPosition, pygame_):
    if direction ==0:#left
        stripStartingpoint=[playerPosition[0]-1,playerPosition[1]] #Startpunktfinden
        for i in range (25): #Alle 25 Pixel testen
            activePixel=[stripStartingpoint[0],stripStartingpoint[1]+i] #Den Pixel vor dem PacMan definieren
            if pygame.display.get_surface().get_at(activePixel)==(0,0,255,255): #testen, ob dieser gleicg blau ist
                stripistrevirsible=False
    elif direction==1: #right
            stripStartingpoint = [playerPosition[0] + 1, playerPosition[1]]  # Startpunktfinden
            for i in range(25):  # Alle 25 Pixel testen
                activePixel = [stripStartingpoint[0], stripStartingpoint[1] + i+ gV.Größe]  # Den Pixel vor dem PacMan definieren
                if pygame.display.get_surface().get_at(activePixel) == (0, 0, 255, 255):  # testen, ob dieser gleicg blau ist
                    stripistrevirsible = False
    elif direction==2: #Up
        stripStartingpoint = [playerPosition[0], playerPosition[1]-1]  # Startpunktfinden
        for i in range(25):  # Alle 25 Pixel testen
            activePixel = [stripStartingpoint[0]+ i,stripStartingpoint[1]]  # Den Pixel vor dem PacMan definieren
            if pygame.display.get_surface().get_at(activePixel) == (0, 0, 255, 255):  # testen, ob dieser gleicg blau ist
                stripistrevirsible = False

    elif direction==3: #Down
        stripStartingpoint = [playerPosition[0], playerPosition[1] +gV.Größe]  # Startpunktfinden
        for i in range(25):  # Alle 25 Pixel testen
            activePixel = [stripStartingpoint[0] + i, stripStartingpoint[1]]  # Den Pixel vor dem PacMan definieren
            if pygame.display.get_surface().get_at(activePixel) == (
            0, 0, 255, 255):  # testen, ob dieser gleicg blau ist
                stripistrevirsible = False

    return stripistrevirsible
