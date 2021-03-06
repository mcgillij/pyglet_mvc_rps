'''
Created on Jul 25, 2012

@author: mcgillij
'''
from cocos.layer import Layer, ColorLayer
from cocos.director import director
from pyglet.gl import glPushMatrix, glPopMatrix
from gameover import GameOver
from cocos.actions import StopGrid

class View(Layer):
    def __init__(self, model, hud):
        super(View, self).__init__()
        width, height = director.get_window_size()
        #setup the view stuff here
        color_layer = ColorLayer( 112, 66, 20, 50, width = width, height=height )
        self.add(color_layer, z=-1)
        self.model = model
        self.hud = hud
        self.model.push_handlers( # win / gameover / various in game effects
                                  self.on_level_complete,
                                  self.on_new_level,
                                  self.on_game_over,
                                  self.on_win,
                                  self.on_tie,
                                  )
        self.hud.show_message( ' Get ready', self.model.start())

    def on_enter(self):
        super(View, self).on_enter()
        #do sound stuff
        
    def on_exit(self):
        super(View, self).on_exit()
        #stop sound

    def on_level_complete(self):
        #sound stuffs can be done here.
        self.hud.show_message('Level complete', self.model.set_next_level)
        return True

    def on_new_level(self):
        #play new level sound
        self.stop()
        self.do(StopGrid())
        self.rotation = 0
        self.scale = 1
        return True

    def on_game_over(self):
        #director.replace(GameOver(win='win'))
        self.parent.add(GameOver(win='win'), z=10)
        return True

    def on_win(self):
        self.parent.add(GameOver(win='lose'), z=10)
        return True

    def on_tie(self):
        self.parent.add(GameOver(win='tie'), z=10)

    def draw(self):
        glPushMatrix()
        self.transform()

        for c in self.model.player_choices:
            c.draw()

        if self.model.choice:
            self.model.choice.draw()
        if self.model.cpu_choice:
            self.model.cpu_choice.draw()
            #self.model.gameobject.draw()
        glPopMatrix()

if __name__ == '__main__':
    pass