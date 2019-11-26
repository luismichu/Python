import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
x = 300
y = 250

disp = pygame.display.set_mode((x, y))
pygame.display.set_caption('CountDown')

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Hey', True, black)
textRect = text.get_rect()
textRect.center = (x//2, y//2)

while True:
	disp.fill(white)
	disp.blit(text, textRect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()