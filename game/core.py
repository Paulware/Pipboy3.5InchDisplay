import pygame
import time
import os
os.environ["SDL_VIDEODRIVER"] = "DIRECTX"
class Engine(object):

	EVENTS_UPDATE = pygame.USEREVENT + 1
	EVENTS_RENDER = pygame.USEREVENT + 2

	def __init__(self, title, width, height, *args, **kwargs):
		super(Engine, self).__init__(*args, **kwargs)
		print ("pygame.display.set_mode (" + str(width) + "," + str(height) + ")" )
		self.window = pygame.display.set_mode((width, height))
		self.screen = pygame.display.get_surface()
		pygame.display.set_caption(title)
		pygame.mouse.set_visible(True)

		self.groups = []
		self.root_children = EntityGroup()
		self.background = pygame.surface.Surface(self.screen.get_size()).convert()
		self.background.fill((0, 0, 0))

		self.rescale = False
		self.last_render_time = 0

	def render(self):
		if self.last_render_time == 0:
			self.last_render_time = time.time()
			return
		else:
			interval = time.time() - self.last_render_time
			self.last_render_time = time.time()
		self.root_children.clear(self.screen, self.background)
		self.root_children.render(interval)
		self.root_children.draw(self.screen)
		for group in self.groups:
			group.render(interval)
			group.draw(self.screen)
		pygame.display.flip()
		return interval

	def update(self):
		self.root_children.update()
		for group in self.groups:
			group.update()

	def add(self, group):
		if group not in self.groups:
			self.groups.append(group)

	def remove(self, group):
		if group in self.groups:
			self.groups.remove(group)


class EntityGroup(pygame.sprite.LayeredDirty):
	def render(self, interval):
		for entity in self:
			entity.render(interval)

	def move(self, x, y):
		for child in self:
			child.rect.move(x, y)


class Entity(pygame.sprite.DirtySprite):
	def __init__(self, dimensions=(0, 0), layer=0, *args, **kwargs):
		super(Entity, self).__init__(*args, **kwargs)
		self.image = pygame.surface.Surface(dimensions)
		self.rect = self.image.get_rect()
		self.image = self.image.convert()
		self.groups = pygame.sprite.LayeredDirty()
		self.layer = layer
		self.dirty = 2
		self.blendmode = pygame.BLEND_RGBA_ADD

	def render(self, interval=0, *args, **kwargs):
		pass

	def update(self, *args, **kwargs):
		pass
