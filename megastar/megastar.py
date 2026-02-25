# MegaStar Application

## Description
MegaStar is a simple application that demonstrates how to manage a collection of stars. It allows users to add, view, and delete stars from their collection. 

## Features
- Add a new star
- View all stars
- Delete a star

## Installation
To install MegaStar, clone the repository and run the following command:

```bash
pip install -r requirements.txt
```

## Usage
To run the application, execute:

```bash
python megastar.py
```

## Code
```python
class Star:
    def __init__(self, name, type, magnitude):
        self.name = name
        self.type = type
        self.magnitude = magnitude

class MegaStar:
    def __init__(self):
        self.stars = []

    def add_star(self, star):
        self.stars.append(star)
        print(f'Star {star.name} added!')

    def view_stars(self):
        for star in self.stars:
            print(f'{star.name} - Type: {star.type}, Magnitude: {star.magnitude}')

    def delete_star(self, name):
        for star in self.stars:
            if star.name == name:
                self.stars.remove(star)
                print(f'Star {name} deleted!')
                return
        print(f'Star {name} not found!')

if __name__ == '__main__':
    app = MegaStar()

    # Example Usage
    star1 = Star('Sirius', 'Main Sequence', -1.46)
    app.add_star(star1)
    star2 = Star('Betelgeuse', 'Red Supergiant', 0.42)
    app.add_star(star2)
    
    print('\nStar Collection:')
    app.view_stars()
    
    app.delete_star('Sirius')
    print('\nAfter Deletion:')
    app.view_stars()
```