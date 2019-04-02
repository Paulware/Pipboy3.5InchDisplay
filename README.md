pypboy
======

Remember that one Python Pip-Boy 3000 project? Neither do we!<br>
Python/Pygame interface, emulating that of the Pipboy-3000.<br> 
Uses OSM for map data and has been partially tailored to respond to physical switches over Raspberry Pi's GPIO<br>

## Features
Work with Screen TFT 3.5" Capacitive of Adafruit<br>
Works with real gps (TBD)

## Requirements
Latest 32 bit python 3.7.X
pygame installed from windows.msi  

## Vision
* Real role play to complete missions and quests.  Interact with other real players
* Network laser tag into game with raspberry pi server running connected to a wifi router (with sim card)
* Real gps is used to pull map from internet 
* Radiation area is configured somehow on raspberry pi server
* Use pipboy screens to choose weapon type to dictate damage dealt on raspberry pi server
* Use pipboy screens to adminster first aid
* Complete actual quests with other players (friendly/neutral/hostile)

## Authors

* By Sabas of The Inventor's House Hackerspace
* By grieve work original<br>
* Paul Richards conversion to 3.5 inch display and runs on pc 
*    Adding gps and real role-play functionality 

## Special Thanks
Ruiz Brothers for the mention in [Adafruit](https://learn.adafruit.com/raspberry-pi-pipboy-3000/overview) 

## License
MIT

##Contributions

Contribuyendo a este programa se da la bienvenida con gusto.<br>

Contributing to this software is warmly welcomed. You can do this basically by [forking](https://help.github.com/articles/fork-a-repo), committing modifications and then [pulling requests](https://help.github.com/articles/using-pull-requests) (follow the links above for operating guide). Adding change log and your contact into file header is encouraged.<br>

Thanks for your contribution.

Enjoy!

Rotary Switch
The rotary switch is connected to various pins on the PiTFT. The table below lists out the pin number and GPIO. The colors correspond with the wires in the diagram - these however, can be whatever color you want.

Pin 14 GND 
Other pins: 7, 11, 13, 15, 16

Notes: 
   Wifi connection is required to load the map
   For Testing you can enter a knob number 1-5 to simulate a knob selection.
   Press ESC to stop the program
   
   config.py has all the knob definitions 
   game/core.py 
      Engine class has the render which renders the active module
   pypboy/__init__.py has a SubModule class which is inherited by pypboy/modules/data/quests.py
   pypboy/core.py 
      looks for events and handles the actions and adds modules for data, items, and stats
   pypboy/data.py not sure what GRID_SIZE/SIG_PLACES 
   pypboy/modules/data/__init__ creates a list of modules that have functionality
   pypboy/modules/data/entities.py Map writes the emenity on the map
   pypboy/modules/data/local_map.py init has a call to fet_map with radius 
      This radius controls the size of the map, it would be nice to be able to zoom  
   pypboy/ui.py Menu.handle_action handles the dial_up and dial_down action 
