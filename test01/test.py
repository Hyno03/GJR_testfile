from pico2d import*
open_canvas()

cha = load_image('character.png')
grass = load_image('grass.png')

x = 0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    cha.draw_now(x,90)
    x = x+2
    delay(0.01)

close_canvas()
