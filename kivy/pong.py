import OpenGLfix
OpenGLfix.run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class Pelota(Widget):
	vel_x, vel_y, pos_x, pos_y = 0, 0, 0, 0

	def mover(self):
		self.pos_x = self.vel_x + self.pos[0]
		self.pos_y = self.vel_y + self.pos[1]

class Pala(Widget):
	puntuacion = 0

	def golpe(self, pelota):
		if self.collide_widget(pelota):
			vel_x, vel_y = pelota.vel_x, pelota.vel_y
			desplazamiento = (pelota.center_y - self.center_y)
			pelota.vel_x, pelota.vel_y = -vel_x, vel_y + desplazamiento

class Juego(Widget):
	pelota = ObjectProperty(None)
	jugador1 = ObjectProperty(None)
	jugador2 = ObjectProperty(None)

	def servicio(self, vel = 5):
		self.pelota.center = self.center
		self.pelota.vel_x = vel
	def actualizar(self, dt):
		self.pelota.mover()
		self.jugador1.golpe(self.pelota)
		self.jugador2.golpe(self.pelota)

		if (self.pelota.y < self.y) or (self.pelota.top > self.top):
			self.pelota.velocity_y *= -1
		if self.pelota.x < self.x:
			self.jugador2.puntuacion += 1
			self.serve_pelota(vel = 5)
		if self.pelota.x > self.width:
			self.jugador1.puntuacion += 1
			self.serve_pelota(vel = -5)

		def on_touch_move(self, touch):
			if touch.x < self.width / 3:
				self.jugador1.center_y = touch.y
			if touch.x > self.width - self.width / 3:
				self.jugador2.center_y = touch.y

class Pong(App):
	def build(self):
		juego = Juego()
		juego.servicio()
		Clock.schedule_interval(juego.actualizar, 1.0 / 60.0)
		return juego

if __name__ == '__main__':
	Pong().run()