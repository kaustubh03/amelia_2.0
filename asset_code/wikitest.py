import pyglet
animation = pyglet.image.load_animation("robo.gif")
# Create a sprite object as an instance of this animation.
animSprite = pyglet.sprite.Sprite(animation)
# The main pyglet window with OpenGL context
w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)

# r,g b, color values and transparency for the background
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
# OpenGL method for setting the background.
pyglet.gl.glClearColor(r, g, b, alpha)

# Draw the sprite in the API method on_draw of
# pyglet.Window
@win.event
def on_draw():
    win.clear()
    animSprite.draw()

pyglet.app.run()
