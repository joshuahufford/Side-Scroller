import random
import kivy
kivy.require('1.10.0')
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty)
from kivy.vector import Vector
from kivy.uix.floatlayout import FloatLayout

class ScrollerGame(Widget):
	player = ObjectProperty(None)

	toppipe1 = ObjectProperty(None)
	toppipe2 = ObjectProperty(None)
	toppipe3 = ObjectProperty(None)
	toppipe4 = ObjectProperty(None)
	toppipe5 = ObjectProperty(None)
	toppipe6 = ObjectProperty(None)
	topPipeNumber = 0

	bottompipe1 = ObjectProperty(None)
	bottompipe2 = ObjectProperty(None)
	bottompipe3 = ObjectProperty(None)
	bottompipe4 = ObjectProperty(None)
	bottompipe5 = ObjectProperty(None)
	bottompipe6 = ObjectProperty(None)
	bottomPipeNumber = 0

	star = ObjectProperty(None)

	scorebox = ObjectProperty(None)
	highscorebox = ObjectProperty(None)

	startbutton = ObjectProperty(None)
	replaybutton = ObjectProperty(None)

	running = False
	score = 0
	timer = 0

	def update(self, dt):
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down)

		self.toppipe1.Collision(self.player)
		self.toppipe2.Collision(self.player)
		self.toppipe3.Collision(self.player)
		self.toppipe4.Collision(self.player)
		self.toppipe5.Collision(self.player)
		self.toppipe6.Collision(self.player)

		self.bottompipe1.Collision(self.player)
		self.bottompipe2.Collision(self.player)
		self.bottompipe3.Collision(self.player)
		self.bottompipe4.Collision(self.player)
		self.bottompipe5.Collision(self.player)
		self.bottompipe6.Collision(self.player)

		self.star.Collision(self.player)

		if self.player.anim_delay == -1:
			self.replaybutton.pos = Vector(500-(self.replaybutton.width/2), 300-(self.replaybutton.height/2))
			self.toppipe1.pos = Vector(1000, self.height-50)
			self.toppipe2.pos = Vector(1000, self.height-100)
			self.toppipe3.pos = Vector(1000, self.height-150)
			self.toppipe4.pos = Vector(1000, self.height-200)
			self.toppipe5.pos = Vector(1000, self.height-250)
			self.toppipe6.pos = Vector(1000, self.height-300)

			self.bottompipe1.pos = Vector(1000, -250)
			self.bottompipe2.pos = Vector(1000, -200)
			self.bottompipe3.pos = Vector(1000, -150)
			self.bottompipe4.pos = Vector(1000, -100)
			self.bottompipe5.pos = Vector(1000, -50)
			self.bottompipe6.pos = Vector(1000, 0)

			self.star.pos = Vector(1000, 300)


		if self.player.velocity_x > 30:
			self.player.velocity_x = 0

			self.replaybutton.pos = Vector(500-(self.replaybutton.width/2), 300-(self.replaybutton.height/2))
			self.toppipe1.pos = Vector(1000, self.height-50)
			self.toppipe2.pos = Vector(1000, self.height-100)
			self.toppipe3.pos = Vector(1000, self.height-150)
			self.toppipe4.pos = Vector(1000, self.height-200)
			self.toppipe5.pos = Vector(1000, self.height-250)
			self.toppipe6.pos = Vector(1000, self.height-300)

			self.bottompipe1.pos = Vector(1000, -250)
			self.bottompipe2.pos = Vector(1000, -200)
			self.bottompipe3.pos = Vector(1000, -150)
			self.bottompipe4.pos = Vector(1000, -100)
			self.bottompipe5.pos = Vector(1000, -50)
			self.bottompipe6.pos = Vector(1000, 0)

			self.star.pos = Vector(1000, 300)

		self.player.Gravity(dt, self.height)

		if (self.running == False or 
			self.toppipe1.pos[0] <= 0 - self.toppipe1.size[0] or 
			self.toppipe2.pos[0] <= 0 - self.toppipe2.size[0] or 
			self.toppipe3.pos[0] <= 0 - self.toppipe3.size[0] or 
			self.toppipe4.pos[0] <= 0 - self.toppipe4.size[0] or 
			self.toppipe5.pos[0] <= 0 - self.toppipe5.size[0] or 
			self.toppipe6.pos[0] <= 0 - self.toppipe6.size[0]): 
				self.running = True
				self.toppipe1.pos = 1000, self.height-50
				self.toppipe2.pos = 1000, self.height-100
				self.toppipe3.pos = 1000, self.height-150
				self.toppipe4.pos = 1000, self.height-200
				self.toppipe5.pos = 1000, self.height-250
				self.toppipe6.pos = 1000, self.height-300
				self.bottompipe1.pos = 1000, -250
				self.bottompipe2.pos = 1000, -200
				self.bottompipe3.pos = 1000, -150
				self.bottompipe4.pos = 1000, -100
				self.bottompipe5.pos = 1000, -50
				self.bottompipe6.pos = 1000, 0

				self.topPipeNumber = random.randint(1,6)
				self.bottomPipeNumber = random.randint(1,6)
				self.player.velocity_x *= 1.1
		else:
			pass

		if self.topPipeNumber == 6 and self.bottomPipeNumber == 6:
			self.toppipe4.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 5 and self.bottomPipeNumber == 6:
			self.toppipe1.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 4 and self.bottomPipeNumber == 6:
			self.toppipe6.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 3 and self.bottomPipeNumber == 6:
			self.toppipe2.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 1:
			self.toppipe1.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 2:
			self.toppipe2.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 3:
			self.toppipe3.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 4:
			self.toppipe4.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 5:
			self.toppipe5.scroll(self.player.velocity_x)
		elif self.topPipeNumber == 6:
			self.toppipe6.scroll(self.player.velocity_x)
		else:
			pass

		if self.bottomPipeNumber == 6 and self.topPipeNumber == 6:
			self.bottompipe4.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 6 and self.topPipeNumber == 5:
			self.bottompipe3.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 6 and self.topPipeNumber == 4:
			self.bottompipe1.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 6 and self.topPipeNumber == 3:
			self.bottompipe5.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 1:
			self.bottompipe1.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 2:
			self.bottompipe2.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 3:
			self.bottompipe3.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 4:
			self.bottompipe4.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 5:
			self.bottompipe5.scroll(self.player.velocity_x)
		elif self.bottomPipeNumber == 6:
			self.bottompipe6.scroll(self.player.velocity_x)
		else:
			pass

		if (self.toppipe1.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe1.pos[0] <= self.player.pos[0] or
			self.toppipe2.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe2.pos[0] <= self.player.pos[0] or
			self.toppipe3.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe3.pos[0] <= self.player.pos[0] or
			self.toppipe4.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe4.pos[0] <= self.player.pos[0] or
			self.toppipe5.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe5.pos[0] <= self.player.pos[0] or
			self.toppipe6.pos[0] >= self.player.pos[0]-self.player.velocity_x and self.toppipe6.pos[0] <= self.player.pos[0]):
				self.score = self.score + 1

		if self.timer % 600 == 0:
			self.star.pos[0] = self.size[0] - self.player.velocity[0]
		if self.star.pos[0] > 0-self.star.size[0] and self.star.pos[0] < self.size[0]:
			self.star.scroll(self.player.velocity_x)
		else:
			self.star.scroll(0)
		
		if self.replaybutton.onpress(self.player) == True:
			self.score = 0
		self.startbutton.onpress(self.player)

		self.scorebox.change_text(self.score)
		highscore = HighScore().readHighScore()
		self.highscorebox.change_text(highscore)

		if self.score > int(highscore):
			HighScore().saveHighScore(self.score)

		self.timer = self.timer+1
	def _keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		if keycode[1] == 'spacebar':
			self.player.velocity_y = 7
		else:
			pass

class Player(Widget):
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	anim_delay = NumericProperty(0.25)
	anim_loop = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	gravity = -20 # Pixels per second

	def Gravity(self, dt, screen_height):

		self.velocity_y = self.velocity_y + (self.gravity*dt)

		self.pos = Vector(0, self.velocity_y) + self.pos

		if self.pos[1] < 0:
			self.pos[1] = 0
			self.velocity_y *= -1 * 0.5

		if self.pos[1] >= screen_height:
			self.velocity_y *= -1

		if self.velocity_y > 0:
			self.anim_delay = 0.05
			self.anim_loop = 1
		else:
			self.anim_delay = 1
			self.anim_loop = 0

class Pipe(Widget):
	LEFT_OFFSET = 100
	def scroll(self, scroll_dist):
		if self.pos[0] > 0 - self.LEFT_OFFSET:
			self.pos = Vector(-1 * scroll_dist, 0) + self.pos
		else:
			pass


	def Collision(self, player):
		if self.collide_widget(player):
			player.velocity_x = 0
			player.velocity_y = 0
			player.anim_delay = -1

class Star(Widget):
	LEFT_OFFSET = 100
	def scroll(self, scroll_dist):
		if self.pos[0] > 0 - self.LEFT_OFFSET:
			self.pos = Vector(-1 * scroll_dist, 0) + self.pos
		else:
			pass

	def Collision(self, player):
		if self.collide_widget(player):
			player.velocity_x = 5
			self.pos[0] = 1000
		if self.pos[0] < (0 - self.size[0]):
			self.pos[0] = 1000

class ScoreBox(Widget):
	text = StringProperty()

	def __init__(self, **kwargs):
		super(ScoreBox, self).__init__(**kwargs)
		self.text = str(0)

	def change_text(self, score):
		self.text = "Score: "+str(score)

class HighScoreBox(Widget):
	text = StringProperty()

	def __init__(self, **kwargs):
		super(HighScoreBox, self).__init__(**kwargs)
		self.text = str(0)

	def change_text(self, highscore):
		self.text = "High Score: "+str(highscore)

class StartButton(Button):
	text = StringProperty("Start")
	def __init__(self, **kwargs):
		super(StartButton, self).__init__(**kwargs)

	def onpress(self, player):
		if self.state == 'down':
			player.velocity_x = 5
			self.pos = Vector(1000, 600)
			self.text = ""

class ReplayButton(Button):
	text = StringProperty("Try Again?")
	def __init__(self, **kwargs):
		super(ReplayButton, self).__init__(**kwargs)

	def onpress(self, player):
		if self.state == 'down':
			player.velocity_x = 5
			player.velocity_y = 7
			player.pos = Vector(100, 100)
			self.pos = Vector(1000, 600)
			return True
		else:
			return False

class ScrollerApp(App):
	def build(self):
		game = ScrollerGame()
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game

class HighScore():
	def readHighScore(self):
		with open("saves/auto_save.txt",'r') as readfile:
			highscore = readfile.readline()
		return highscore
	
	def saveHighScore(self, score):
		with open("saves/auto_save.txt",'w') as writefile:
			writefile.write(str(score))


if __name__ == '__main__':
	ScrollerApp().run()