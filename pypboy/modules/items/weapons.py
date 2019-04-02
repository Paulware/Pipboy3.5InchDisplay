import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		quests = Quests()
		quests.rect[0] = 4
		quests.rect[1] = 40
		self.add(quests)  

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "Quests Yo"
		super(Module, self).handle_resume()
  
class Quests(game.Entity):
	def __init__(self):
		super(Quests, self).__init__()
		self.image = pygame.image.load('images/plasmaCannon1.jpg')
		self.rect = self.image.get_rect()
		self.image = self.image.convert()
		text = config.FONTS[18].render("Grieve - Level 27", True, (105, 251, 187), (0, 0, 0))
		text_width = text.get_size()[0]
		self.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 250))