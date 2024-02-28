import pyglet
from pyglet.window import key

class Player:
    def __init__(self,x_pos,y_pos):
        self.up=False
        self.left=False
        self.down=False
        self.right=False
        self.x=x_pos
        self.y=y_pos
        self.n=8

    def check_bounds(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()
game_window = pyglet.window.Window(1280, 800)
image=pyglet.resource.image("character_sheet.png") # 12 rows 8 columns
image_seq=pyglet.image.ImageGrid(image, 12, 8) #Sprite Sheet
image_sprite=[]

for  i in range (24):
    image_sprite.append(pyglet.sprite.Sprite(img=image_seq[i]))
    image_sprite[i].update(scale=3)
x_pos=0
y_pos=0

add_sprite=[]
for  i in range (48,64):
    image_sprite.append(pyglet.sprite.Sprite(img=image_seq[i]))
    image_sprite[i-48].update(scale=3)


score_label = pyglet.text.Label(text="Score: 0", x=1280//2, y=50)

p1=Player(x_pos,y_pos)

@game_window.event
def on_draw():
    game_window.clear()
    score_label.draw()
    image_sprite[p1.n].draw()

@game_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        p1.up=True
    if symbol == key.A:
        p1.left=True
    if symbol == key.S:
        p1.down=True
    if symbol == key.D:
        p1.right=True

@game_window.event
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        p1.up=False
    if symbol == key.A:
        p1.left=False
    if symbol == key.S:
        p1.down=False
    if symbol == key.D:
        p1.right=False

speed=200
def update(dt):
    if p1.up:
        y_pos=p1.y+dt*speed
        image_sprite[p1.n].y=y_pos
        p1.y=y_pos
    if p1.down:
        y_pos=p1.y-dt*speed
        image_sprite[p1.n].y=y_pos
        p1.y=y_pos
    if p1.right:
        x_pos=p1.x+dt*speed
        image_sprite[p1.n].x=x_pos
        p1.x=x_pos
    if p1.left:
        x_pos=p1.x-dt*speed
        image_sprite[p1.n].x=x_pos
        p1.x=x_pos
pyglet.clock.schedule_interval(update, 1/60)

if __name__ == '__main__':
    pyglet.app.run()
