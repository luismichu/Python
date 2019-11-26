def run():
	from kivy import Config
	Config.set('graphics', 'multisamples', '0')
	import os
	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'