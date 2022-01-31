import pygame

size = WIDTH, HEIGHT = 800, 600
FPS = 60

pygame.init()

speed = [3, 4]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load("logo/red-logo (1).png")
r = logo.get_rect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if r.left < 0:
        speed[0] = -speed[0]
        logo = pygame.image.load("logo/green-logo (1).png")

    if r.right > WIDTH:
        speed[0] = -speed[0]
        logo = pygame.image.load("logo/orange-logo (1).png")

    if r.top < 0:
        speed[1] = -speed[1]
        logo = pygame.image.load("logo/purple-logo (1).png")

    if r.bottom > HEIGHT:
        speed[1] = -speed[1]
        logo = pygame.image.load("logo/blue-logo (1).png")

    r.left += speed[0]
    r.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, r)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
