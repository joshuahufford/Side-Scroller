import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout

class MainScreen(Screen):
	pass

class GameScreen(Screen):
	pass

class SettingsScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass


mainkv = Builder.load_file("main.kv")

class MainApp(App):
	def build(self):
		return mainkv

if __name__ == '__main__':
    MainApp().run()