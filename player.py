import pygame


class player:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y
		self.xdirection = 0
		self.ydirection = 0
		self.currentImage = image
		self.xVelocity = 0
		self.yVelocity = 0

	def draw(self, screen):
		screen.blit(self.currentImage, (self.x, self.y))

	def move(self):
		if self.xdirection != 0:
			self.xVelocity += 1 * self.xdirection * 0.2
		if self.ydirection != 0:
			self.yVelocity += 1 * self.ydirection * 0.2

		if self.xVelocity > 2:
			self.xVelocity = 2
		if self.yVelocity > 2:
			self.yVelocity = 2

		if self.xVelocity < -2:
			self.xVelocity = -2
		if self.yVelocity < -2:
			self.yVelocity = -2

		self.x += self.xVelocity
		self.y += self.yVelocity

		self.xVelocity *= 0.99
		self.yVelocity *= 0.99

		if self.xVelocity < 0.1 and self.xVelocity > -0.1:
			self.xVelocity = 0
		if self.yVelocity < 0.1 and self.yVelocity > -0.1:
			self.yVelocity = 0

	def setDirection(self, x, y):
		self.xdirection = x
		self.ydirection = y
		if x < 0:
			self.currentImage = pygame.transform.flip(self.image, True, False)
		elif x > 0:
			self.currentImage = self.image
		elif y < 0:
			self.currentImage = pygame.transform.rotate(self.image, 90)
		elif y > 0:
			self.currentImage = pygame.transform.rotate(self.image, -90)
