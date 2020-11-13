from space.planet import Planet
from space.calc import planet_mass, planet_vol

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')


hoth_mass = planet_mass(hoth.gravity, hoth.radius)
hoth_vol = planet_vol(hoth.radius)

print(f'{hoth.name} has a mass of {hoth_mass} and a volumn of {hoth_vol}')