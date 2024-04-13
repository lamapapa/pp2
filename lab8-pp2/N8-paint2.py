import pygame
import random
import math

#drawing simple lines
def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1-x2)
    dy = abs(y1-y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx>dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x)/B
            pygame.draw.circle(screen, color, (x, y), width)

    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y)/A
            pygame.draw.circle(screen, color, (x, y), width)

#function to drow rectangle
def draw_rect(screen, pos, color, a):
    x1 = pos[0]
    y1 = pos[1]

    print(pos)
    pygame.draw.rect(screen, color, (x1, y1, a, a), 5)

#function to draw circles
def draw_c(screen, pos, color, radius):
    x = pos[0]
    y = pos[1]

    pygame.draw.circle(screen, color, pos, radius, 5)

#function to draw right triangle
def draw_rt(screen, pos, color, a):
    x = pos[0]
    y = pos[1]
    
    pygame.draw.lines(screen, color, True, [(x,y), (x, y+a), (x+a, y+a)], 5)
    
#function to draw equilateral triangle
def draw_qt(screen, pos, color, a):           
    x = pos[0]
    y = pos[1]
    
    #points of angles of equilateral triangle with 60 angle
    point1 = (x,y)
    point2 = (x-a*math.cos(math.pi/3), y+a*math.sin(math.pi/3))
    point3 = (x+a*math.cos(math.pi/3), y+a*math.sin(math.pi/3))
    
    pygame.draw.lines(screen, color, True, [point1, point2, point3], 5)
    
#function to draw rhombus
def draw_h(screen, pos, color, a):
    x = pos[0]
    y = pos[1]
    
    #points of angles of rhombus with 60 and 120 angles
    point1 = (x,y)
    point2 = (x-a*math.cos(math.pi/6), y+a*math.sin(math.pi/6))
    point3 = (x, y+a)
    point4 = (x+a*math.cos(math.pi/6), y+a*math.sin(math.pi/6))
    
    pygame.draw.lines(screen, color, True, [point1, point2, point3, point4], 5)

def main():
    screen = pygame.display.set_mode((1100, 600))
    mode = 'random'
    draw_on = False
    last_pos = {0, 0}
    color = (255, 128, 0)
    radius = 10

#setting up colors
    colors = {
        'red' : (255, 0, 0),
        'blue' : (0, 0, 255),
        'green' : (0, 255, 0),
        'eraser' : (255, 255, 255)
    }

    screen.fill((255, 255, 255))

    while True:

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(screen, "image.jpg")
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                #if press ctrl+r draw rectangle
                if event.key == pygame.K_r and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_rect(screen, mp, color, radius*10)

                #if press ctrl+c draw circles
                if event.key == pygame.K_c and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_c(screen, mp, color, radius*5)
                    
                #if press ctrl+t draw right triangle
                if event.key == pygame.K_t and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_rt(screen, mp, color, radius*10)
                
                #if press ctrl+q draw equilateral triangle
                if event.key == pygame.K_q and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_qt(screen, mp, color, radius*10)
                #if press ctrl+h draw rhombus 
                if event.key == pygame.K_h and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_h(screen, mp, color, radius*10)


                #if press ctrl + e eraser
                if event.key == pygame.K_e and ctrl_held:
                    mode = 'eraser'
                #press r get red
                if event.key == pygame.K_r:
                    mode = 'red'
                #press b get blue
                if event.key == pygame.K_b:
                    mode = 'blue'
                #press g get green
                if event.key == pygame.K_g:
                    mode = 'green'
                #press up line get wider
                if event.key == pygame.K_UP:
                    radius += 1
                #press down line gets shrinker
                if event.key == pygame.K_DOWN:
                    radius -= 1

                #pressing just a left click will cause random color lines
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    draw_line(screen, last_pos, event.pos, radius, color)

                last_pos = event.pos

        pygame.display.flip()

    pygame.quit()

main()