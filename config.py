import pygame

WIDTH = 480
HEIGHT = 320

# OUTPUT_WIDTH = 320
# OUTPUT_HEIGHT = 240

MAP_FOCUS = (-102.3016145, 21.8841274) # NYC
MAP_FOCUS = (-93.636860, 42.025030) # Ames
MAP_FOCUS = (-93.777325, 41.592103) # Grimes cloverleaf
MAP_FOCUS = (-93.734934, 41.6082) # Park

EVENTS = {
	'SONG_END': pygame.USEREVENT + 1
}

ACTIONS = {
	pygame.K_F1: "module_stats",
	pygame.K_F2: "module_items",
	pygame.K_F3: "module_data",
	pygame.K_1:	"knob_1",
	pygame.K_2: "knob_2",
	pygame.K_3: "knob_3",
	pygame.K_4: "knob_4",
	pygame.K_5: "knob_5",
	pygame.K_UP: "dial_up",
	pygame.K_DOWN: "dial_down"
}

#Pin 14 GND 
#Other pins: 7, 11, 13, 15, 16
# Currently connected: 17, 22, 4, 27

# Using GPIO.BCM as mode
GPIO_ACTIONS = {
  17: "module_stats", #GPIO 4
	22: "module_items", #GPIO 14
	4: "module_data", #GPIO 15 Map? 
	#17:	"knob_1", #GPIO 17 AKA pin 11
	#22: "knob_2", #GPIO 22 AKA pin 15 
 #	4: "knob_3", #GPIO  4 AKA pin  7
	#27: "knob_4", #GPIO 27 AKA pin 13
27: "knob_5", #GPIO 23 AKA pin 16 (NC) 
#31: "dial_up", #GPIO 31
	18: "dial_down" #GPIO 18
}


MAP_ICONS = {
	"camp": 		pygame.image.load('images/map_icons/camp.png'),
	"factory": 		pygame.image.load('images/map_icons/factory.png'),
	"metro": 		pygame.image.load('images/map_icons/metro.png'),
	"misc": 		pygame.image.load('images/map_icons/misc.png'),
	"monument": 	pygame.image.load('images/map_icons/monument.png'),
	"vault": 		pygame.image.load('images/map_icons/vault.png'),
	"settlement": 	pygame.image.load('images/map_icons/settlement.png'),
	"ruin": 		pygame.image.load('images/map_icons/ruin.png'),
	"cave": 		pygame.image.load('images/map_icons/cave.png'),
	"landmark": 	pygame.image.load('images/map_icons/landmark.png'),
	"city": 		pygame.image.load('images/map_icons/city.png'),
	"office": 		pygame.image.load('images/map_icons/office.png'),
	"sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
	'pub': 				MAP_ICONS['vault'],
	'nightclub': 		MAP_ICONS['vault'],
	'bar': 				MAP_ICONS['vault'],
	'fast_food': 		MAP_ICONS['sewer'],
	'cafe': 			MAP_ICONS['sewer'],
	'drinking_water': 	MAP_ICONS['sewer'],
	'restaurant': 		MAP_ICONS['settlement'],
	'cinema': 			MAP_ICONS['office'],
	'pharmacy': 		MAP_ICONS['office'],
	'school': 			MAP_ICONS['office'],
	'bank': 			MAP_ICONS['monument'],
	'townhall': 		MAP_ICONS['monument'],
	'bicycle_parking': 	MAP_ICONS['misc'],
	'place_of_worship': MAP_ICONS['misc'],
	'theatre': 			MAP_ICONS['misc'],
	'bus_station': 		MAP_ICONS['misc'],
	'parking': 			MAP_ICONS['misc'],
	'fountain': 		MAP_ICONS['misc'],
	'marketplace': 		MAP_ICONS['misc'],
 'grave_yard':  MAP_ICONS['misc'],
	'atm': 				MAP_ICONS['misc'],
}

pygame.font.init()
FONTS = {}
for x in range(10, 28):
	FONTS[x] = pygame.font.Font('monofonto.ttf', x)