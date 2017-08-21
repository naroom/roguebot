# move / attack keys
KEY_WAIT = "."
KEY_LEFT = "h"
KEY_RIGHT = "l"
KEY_UP = "k"
KEY_DOWN = "j"
KEY_THROW = "t"
KEY_ZAP = "z"

# equipment
KEY_EQUIP = "W"
KEY_TAKE_OFF = "T"
KEY_WIELD = "w"



def do_weapon(state):
	"""
	Manage the player's inventory by trying on
	new weapons.

	Knows about: 
	- Numbers for current weapons
	- Distance to nearby monsters
	"""
	best_action = KEY_WAIT
	priority = 0
	return (best_action, priority)


def do_armor(state):
	"""
	Manage the player's inventory by trying on
	new armors

	Knows about: 
	- Numbers for current weapons
	- Distance to nearby monsters
	"""
	best_action = KEY_WAIT
	priority = 0
	return (best_action, priority)


def do_food(state):
	"""
	Keep the player fed.

	Knows about:
	- Hunger status
	- Steps since last food
	- Food in inventory
	- Fullness of inventory
	"""
	best_action = KEY_WAIT
	priority = 0
	return (best_action, priority)


def do_potions(state):
	"""
	Uses potions, or not.
	
	Knows about: 
	- Health, strength, level, depth
	- Distance to nearby monsters
	- Fullness of inventory
	"""
	best_action = KEY_WAIT
	priority = 0
	return (best_action, priority)

	
def do_scrolls(state):
	"""
	Uses scrolls, or not.
	
	Knows about: 
	- Numbers for current weapons / armor
	- Distance to nearby monsters
	- Fullness of inventory
	"""
	best_action = KEY_WAIT
	priority = 0
	return (best_action, priority)


def do_rings(state):
	"""
	Just ignore the goddamn rings.
	"""
	return (KEY_WAIT, 0)


def get_next_action():
	flist = [do_rings, do_scrolls, do_potions, do_food, do_armor, do_weapon]
	for f in flist:
		(action, priority) = f(state)
		

