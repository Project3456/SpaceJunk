# Space Junk Collector

## About the Project
Space Junk Collector is a Python project where you control a spaceship that collects junk in space. It’s a simple game to practice object-oriented programming (OOP) in Python. You manage the spaceship’s fuel and inventory while collecting space junk. This project is great for beginners learning Python classes and methods.

## Features
- Create a spaceship with a name and fuel level.
- Collect junk if the spaceship has enough fuel (uses 5 fuel units per junk).
- Check the spaceship’s status (name, fuel, and inventory).
- Easy-to-understand code for learning purposes.

## How It Works
The Space class represents a spaceship with these attributes:
- name: The spaceship’s name.
- fuel: Fuel level (0–100, defaults to 50 if invalid).
- inventory: A list to store collected junk.

### Methods
- show_status(): Shows the spaceship’s name, fuel, and inventory.
- collect_junk(): Adds "junk" to the inventory if there’s enough fuel (at least 10 units).

## Example Code
`python
ship = Space("Star", 50)
print(ship.collect_junk())  # Output: Junk collected!
print(ship.show_status())   # Output: Ship: Star, Fuel: 45, Inventory: ['junk']

How to RunClone the repository:
git clone https://github.com/Project3456/SpaceJunk.gitMake
sure you have Python 3.x installed.
Run the script:
python space_junk_collector.pyRequirementsPython 3.xFuture IdeasAdd new actions like repairing the ship or trading junk.Create a graphical version using Pygame or Arcade.Include random events like finding rare items or losing fuel.AuthorCreated by Project
a 12-year-old coder learning Python and aiming to work at Google!
