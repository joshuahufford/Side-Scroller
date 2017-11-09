import random
import kivy
from kivy.clock import Clock
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty)
from kivy.vector import Vector


class ScrollerGame(Widget):
	player = ObjectProperty(None)
	obstical1 = ObjectProperty(None)
	counter = 0

	def update(self, dt):
		self.player.Collision(self.obstical1)
		self.player.Move(dt, self.width)
		self.player.Gravity(dt, self.height)
		self.obstical1.scroll(self.player.velocity_x)
		print(self.player.pos)

	def on_touch_down(self, touch):
		if self.counter == 0:
			self.player.velocity_x = 2
			self.counter += 1
		else:
			self.player.velocity_y = 10
			self.counter += 1

	# def on_touch_up(self, touch):
	# 	self.player.initial_velocity_y = 0

class Player(Widget):
	MAX_VELOCITY_X = 10
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	gravity = -20 # Pixels per second

	def Move(self, dt, screen_width):
		if self.velocity_x > self.MAX_VELOCITY_X:
			self.velocity_x = self.MAX_VELOCITY_X

		self.pos = Vector(0, self.velocity_y) + self.pos

	def Gravity(self, dt, screen_height):

		self.velocity_y = self.velocity_y+(self.gravity*dt)

		self.pos = Vector(0, self.velocity_y) + self.pos

		if self.pos[1] > screen_height or self.pos[1] <0:
			self.pos[1] = 0

	def Collision(self, obstical):
		if self.collide_widget(obstical):
			self.velocity_x = 0


class Obstical(Widget):
	LEFT_OFFSET = 10
	
	def scroll(self, scroll_dist):
		if self.pos[0] > 0 - self.LEFT_OFFSET:
			self.pos = Vector(-1 * scroll_dist, 0) + self.pos
		else:
			self.pos = Vector(
				self.parent.width + random.randint(0, self.parent.width), 0)


class ScrollerApp(App):
	def build(self):
		game = ScrollerGame()
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game

if __name__ == '__main__':
	ScrollerApp().run()