from pico2d import *
import math

def move_circle():
    x = -180;
    while (x <= 180):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + 300 * math.sin(x / 360 * 2 * math.pi), 300 + 210 * math.cos (x / 360 * 2 * math.pi))
        x = x + 2
        delay(0.01)
        
def move_triangle():
    x = 400;
    y = 90;
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while (x > 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y + 840/400
        delay(0.01)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y - 840/400
        delay(0.01)
    while (x <= 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

while(True):
    move_triangle()
    delay(0.1)
    move_circle()
    delay(0.1)
    
close_canvas()
