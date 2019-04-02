import os
import game
import config
import pygame
import threading
import pypboy.data

from random import choice


class Map(game.Entity):

	_mapper = None
	_transposed = None
	_size = 0
	_fetching = None
	_map_surface = None
	_loading_size = 0
	_render_rect = None

	def __init__(self, width, render_rect=None, *args, **kwargs):
		self._mapper = pypboy.data.Maps()
		self._size = width
		self._map_surface = pygame.Surface((width, width))
		self._render_rect = render_rect
		super(Map, self).__init__((width, width), *args, **kwargs)
		text = config.FONTS[14].render("Loading map...", True, (95, 255, 177), (0, 0, 0))
		self.image.blit(text, (10, 10))

	def fetch_map(self, position, radius):
		#(-5.9234923, 54.5899493)
		self._fetching = threading.Thread(target=self._internal_fetch_map, args=(position, radius))
		self._fetching.start()

	def _internal_fetch_map(self, position, radius):
		self._mapper.fetch_by_coordinate(position, radius)
		self.redraw_map()

	def update(self, *args, **kwargs):
		super(Map, self).update(*args, **kwargs)

	def move_map(self, x, y):
		self._render_rect.move_ip(x, y)

	def redraw_map(self, coef=1):
		self._map_surface.fill((0, 0, 0))
		for way in self._mapper.transpose_ways((self._size / coef, self._size / coef), (self._size / 2, self._size / 2)):
			pygame.draw.lines(
					self._map_surface,
					(85, 251, 167),
					False,
					way,
					2
			)
		count = 0 
		for tag in self._mapper.transpose_tags((self._size / coef, self._size / coef), (self._size / 2, self._size / 2)):
			count = count + 1
			if tag[3] in config.AMENITIES:
				image = config.AMENITIES[tag[3]]
				pygame.transform.scale(image, (10, 10))
				self._map_surface.blit(image, (tag[1], tag[2]))
				text = config.FONTS[12].render(tag[0], True, (95, 255, 177), (0, 0, 0))
				self._map_surface.blit(text, (tag[1] + 17, tag[2] + 4))		
				self.image.blit(self._map_surface, (0, 0), area=self._render_rect)
			else:
				print ("Unknown amenity: " + tag[3] + " " + str(count))
				image = config.MAP_ICONS['misc']
    
		print ("done in Map redraw_map")

class MapSquare(game.Entity):
	_mapper = None
	_size = 0
	_fetching = None
	_map_surface = None
	map_position = (0, 0)

	def __init__(self, size, map_position, parent, *args, **kwargs):
		self._mapper = pypboy.data.Maps()
		self._size = size
		self.parent = parent
		self._map_surface = pygame.Surface((size * 2, size * 2))
		self.map_position = map_position
		self.tags = {}
		super(MapSquare, self).__init__((size, size), *args, **kwargs)

	def fetch_map(self):
		self._fetching = threading.Thread(target=self._internal_fetch_map)
		self._fetching.start()

	def _internal_fetch_map(self):
		self._mapper.fetch_grid(self.map_position)
		self.redraw_map()
		self.parent.redraw_map()

	def redraw_map(self, coef=1):
		self._map_surface.fill((0, 0, 0))
		for way in self._mapper.transpose_ways((self._size, self._size), (self._size / 2, self._size / 2)):
			pygame.draw.lines(
					self._map_surface,
					(85, 251, 167),
					False,
					way,
					1
			)
		for tag in self._mapper.transpose_tags((self._size, self._size), (self._size / 2, self._size / 2)):
			self.tags[tag[0]] = (tag[1] + self.position[0], tag[2] + self.position[1], tag[3])
		self.image.fill((0, 0, 0))
		self.image.blit(self._map_surface, (-self._size / 2, -self._size / 2))
		print ("Done in MapSquare redraw_map")

class MapGrid(game.Entity):

	_grid = None
	_delta = 0.002
	_starting_position = (0, 0)

	def __init__(self, starting_position, dimensions, *args, **kwargs):
		self._grid = []
		self._starting_position = starting_position
		self.dimensions = dimensions
		self._tag_surface = pygame.Surface(dimensions)
		super(MapGrid, self).__init__(dimensions, *args, **kwargs)
		self.tags = {}
		self.fetch_outwards()

	def test_fetch(self):
		for x in range(10):
			for y in range(5):
				square = MapSquare(
					100,
					(
						self._starting_position[0] + (self._delta * x),
						self._starting_position[1] - (self._delta * y)
					)
				)
				square.fetch_map()
				square.position = (100 * x, 100 * y)
				self._grid.append(square)

	def fetch_outwards(self):
		for x in range(-4, 4):
			for y in range(-2, 2):
				square = MapSquare(
					86,
					(
						self._starting_position[0] + (self._delta * x),
						self._starting_position[1] - (self._delta * y)
					),
					self
				)
				square.fetch_map()
				square.position = ((86 * x) + (self.dimensions[0] / 2) - 43, (86 * y) + (self.dimensions[1] / 2) - 43)
				self._grid.append(square)


	def draw_tags(self):
		self.tags = {}
		for square in self._grid:
			self.tags.update(square.tags)
		self._tag_surface.fill((0, 0, 0))
		print ("Process " + str(len(self.tags)) + " tags" )
		count = 0
		for name in self.tags:
			count = count + 1
			if self.tags[name][2] in config.AMENITIES:
				image = config.AMENITIES[self.tags[name][2]]
			else:
				print ("Unknown amenity: " + self.tags[name][2] + " " + str(count) + " of " + str(len(self.tags)))
				image = config.MAP_ICONS['misc']
			pygame.transform.scale(image, (10, 10))
			self.image.blit(image, (self.tags[name][0], self.tags[name][1]))
			# try:
			text = config.FONTS[12].render(name, True, (95, 255, 177), (0, 0, 0))
			# text_width = text.get_size()[0]
			# 	pygame.draw.rect(
			# 		self,
			# 		(0, 0, 0),
			# 		(self.tags[name][0], self.tags[name][1], text_width + 4, 15),
			# 		0
			# 	)
			self.image.blit(text, (self.tags[name][0] + 17, self.tags[name][1] + 4))
			# 	pygame.draw.rect(
			# 		self,
			# 		(95, 255, 177),
			# 		(self.tags[name][0], self.tags[name][1], text_width + 4, 15),
			# 		1
			# 	)
			# except Exception, e:
			# 	print(e)
			# 	pass
		print ("Done in MapGrid draw tags")

	def redraw_map(self, *args, **kwargs):
		self.image.fill((0, 0, 0))
		for square in self._grid:
			self.image.blit(square._map_surface, square.position)
		self.draw_tags()
		print ( "Done in MapGrid redraw_map")

class RadioStation(game.Entity):

	STATES = {
		'stopped': 0,
		'playing': 1,
		'paused': 2
	}

	def __init__(self, *args, **kwargs):
		super(RadioStation, self).__init__((10, 10), *args, **kwargs)
		self.state = self.STATES['stopped']
		self.files = self.load_files()
		pygame.mixer.music.set_endevent(config.EVENTS['SONG_END'])


	def play_random(self):
		f = choice(self.files)
		self.filename = f
		pygame.mixer.music.load(f)
		pygame.mixer.music.play()
		self.state = self.STATES['playing']
		
	def play(self):
		if self.state == self.STATES['paused']:
			pygame.mixer.music.unpause()
			self.state = self.STATES['playing']
		else:
			self.play_random()
		
	def pause(self):
		self.state = self.STATES['paused']
		pygame.mixer.music.pause()
		
	def stop(self):
		self.state = self.STATES['stopped']
		pygame.mixer.music.stop()

	def load_files(self):
		files = []
		for f in os.listdir(self.directory):
			if f.endswith(".mp3") or f.endswith(".ogg") or f.endswith(".wav"):
				files.append(self.directory + f)
		print (files)
		return files


class GalaxyNewsRadio(RadioStation):

	def __init__(self, *args, **kwargs):
		self.directory = 'sounds/radio/gnr/'
		super(GalaxyNewsRadio, self).__init__(self, *args, **kwargs)
