import pygame
import random


class missiles:
	def __init__(self, image, x, y):
		print("yo")
		self.image = image
		self.x = x
		self.y = y
		ypos = random.randint(0, 720)
		print(self.y)
		move = True


	def istouching(self, x, y, w, h,player):
		missilesSize = self.image.get_size()
		myx = self.x - missilesSize[0] / 2
		myy = self.y - missilesSize[1] / 2

		if (myx >= x and myx <= x + w) or x >= myx and x <= myx + missilesSize[0]:
			if (myy >= y and myy <= y + h) or y >= myy and y <= myy + missilesSize[1]:
				player.x = 640
				player.y = 360
				print("boom")





	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
