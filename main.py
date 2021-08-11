# importing files etc
import pygame
from player import player

# set python window
pygame.display.set_caption('jets n missiles')
screen = pygame.display.set_mode([1280, 720])

# initiating files
pygame.init()

# variables
running = True
playerLeft = pygame.K_a
playerRight = pygame.K_d
playerUp = pygame.K_w
playerDown = pygame.K_s

# load the sprites and world also resizing things
Worldimage = pygame.image.load('FSKY.PNG')
Worldimage = pygame.transform.scale(Worldimage, (1280, 720))
pjet = pygame.image.load('jet.png')
pjet = pygame.transform.scale(pjet, (100, 56))

player = player(pjet, 20, 60)
def IsKeyDown(event, key):
	return event.type == pygame.KEYDOWN and event.key == key
def IsKeyUp(event, key):
	return event.type == pygame.KEYUP and event.key == key
# main game loop
while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False
		if not running:
			break
		if IsKeyDown(event, playerRight):
			player.setDirection(1, player.ydirection)
		if IsKeyUp(event, playerRight):
			player.setDirection(0, player.ydirection)
		if IsKeyDown(event, playerLeft):
			player.setDirection(-1, player.ydirection)
		if IsKeyUp(event, playerLeft):
			player.setDirection(0, player.ydirection)
		if IsKeyDown(event, playerDown):
			player.setDirection(player.xdirection, 1)
		if IsKeyUp(event, playerDown):
			player.setDirection(player.xdirection, 0)
		if IsKeyDown(event, playerUp):
			player.setDirection(player.xdirection, -1)
		if IsKeyUp(event, playerUp):
			player.setDirection(player.xdirection, 0)



	screen.blit(Worldimage, (0, 0))
	player.draw(screen)
	player.move()
	pygame.display.flip()
