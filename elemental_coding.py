import pygame
import sys
import math

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Periodic Table")

background = (44,44,47)
white = (255,255,255)
black = (0,0,0)
red = (255, 100, 100)
element_font_color = (82,87,93)

alkali_metals = (255,204,204)
alkaline_earth_metals = (255,229,204)
transition_metals = (255,255,204)
post_transition_metals = (229,255,204)
metalloids = (204,255,205)
non_metals = (204,255,229)
halogens = (204, 229, 255)
noble_gasses = (229,204,255)
lanthanides = (255,204,229)
actinides = (255,229,204)

font = pygame.font.Font(None,29)
large_font = pygame.font.Font(None, 36)
bold_font = pygame.font.Font(None, 33)
bold_font.set_bold(True)

element_font = pygame.font.Font("NewAmsterdam-Regular.ttf", 28)
popup_font = pygame.font.Font(None, 46)

cell_size = 53
grid_paddiing = 4
table_offset_x = 80

elements = {
    'H': {
        'name': 'Hydrogen', 
        'color': 'non_metals', 
        'atomic_number': 1, 
        'mass': 1.008, 
        'electron_config': '1s1', 
        'shells': [1]
    },
    'He': {
        'name': 'Helium', 
        'color': 'noble_gases', 
        'atomic_number': 2, 
        'mass': 4.003, 
        'electron_config': '1s2', 
        'shells': [2]
    },
    'Li': {
        'name': 'Lithium', 
        'color': 'alkali_metals', 
        'atomic_number': 3, 
        'mass': 6.94, 
        'electron_config': '1s2 2s1', 
        'shells': [2, 1]
    },
    'Be': {
        'name': 'Beryllium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 4, 
        'mass': 9.0122, 
        'electron_config': '1s2 2s2', 
        'shells': [2, 2]
    },
    'B': {
        'name': 'Boron', 
        'color': 'metalloids', 
        'atomic_number': 5, 
        'mass': 10.81, 
        'electron_config': '1s2 2s2 2p1', 
        'shells': [2, 3]
    },
    'C': {
        'name': 'Carbon', 
        'color': 'non_metals', 
        'atomic_number': 6, 
        'mass': 12.011, 
        'electron_config': '1s2 2s2 2p2', 
        'shells': [2, 4]
    },
    'N': {
        'name': 'Nitrogen', 
        'color': 'non_metals', 
        'atomic_number': 7, 
        'mass': 14.007, 
        'electron_config': '1s2 2s2 2p3', 
        'shells': [2, 5]
    },
    'O': {
        'name': 'Oxygen', 
        'color': 'non_metals', 
        'atomic_number': 8, 
        'mass': 15.999, 
        'electron_config': '1s2 2s2 2p4', 
        'shells': [2, 6]
    },
    'F': {
        'name': 'Fluorine', 
        'color': 'halogens', 
        'atomic_number': 9, 
        'mass': 18.998, 
        'electron_config': '1s2 2s2 2p5', 
        'shells': [2, 7]
    },
    'Ne': {
        'name': 'Neon', 
        'color': 'noble_gases', 
        'atomic_number': 10, 
        'mass': 20.180, 
        'electron_config': '1s2 2s2 2p6', 
        'shells': [2, 8]
    },
    'Na': {
        'name': 'Sodium', 
        'color': 'alkali_metals', 
        'atomic_number': 11, 
        'mass': 22.990, 
        'electron_config': '1s2 2s2 2p6 3s1', 
        'shells': [2, 8, 1]
    },
    'Mg': {
        'name': 'Magnesium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 12, 
        'mass': 24.305, 
        'electron_config': '1s2 2s2 2p6 3s2', 
        'shells': [2, 8, 2]
    },
    'Al': {
        'name': 'Aluminum', 
        'color': 'post_transition_metals', 
        'atomic_number': 13, 
        'mass': 26.982, 
        'electron_config': '1s2 2s2 2p6 3s2 3p1', 
        'shells': [2, 8, 3]
    },
    'Si': {
        'name': 'Silicon', 
        'color': 'metalloids', 
        'atomic_number': 14, 
        'mass': 28.085, 
        'electron_config': '1s2 2s2 2p6 3s2 3p2', 
        'shells': [2, 8, 4]
    },
    'P': {
        'name': 'Phosphorus', 
        'color': 'non_metals', 
        'atomic_number': 15, 
        'mass': 30.974, 
        'electron_config': '1s2 2s2 2p6 3s2 3p3', 
        'shells': [2, 8, 5]
    },
    'S': {
        'name': 'Sulfur', 
        'color': 'non_metals', 
        'atomic_number': 16, 
        'mass': 32.06, 
        'electron_config': '1s2 2s2 2p6 3s2 3p4', 
        'shells': [2, 8, 6]
    },
    'Cl': {
        'name': 'Chlorine', 
        'color': 'halogens', 
        'atomic_number': 17, 
        'mass': 35.45, 
        'electron_config': '1s2 2s2 2p6 3s2 3p5', 
        'shells': [2, 8, 7]
    },
    'Ar': {
        'name': 'Argon', 
        'color': 'noble_gases', 
        'atomic_number': 18, 
        'mass': 39.948, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6', 
        'shells': [2, 8, 8]
    },
    'K': {
        'name': 'Potassium', 
        'color': 'alkali_metals', 
        'atomic_number': 19, 
        'mass': 39.098, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1', 
        'shells': [2, 8, 8, 1]
    },
    'Ca': {
        'name': 'Calcium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 20, 
        'mass': 40.078, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2', 
        'shells': [2, 8, 8, 2]
    },
    'Sc': {
        'name': 'Scandium', 
        'color': 'transition_metals', 
        'atomic_number': 21, 
        'mass': 44.956, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d1 4s2', 
        'shells': [2, 8, 9, 2]
    },
    'Ti': {
        'name': 'Titanium', 
        'color': 'transition_metals', 
        'atomic_number': 22, 
        'mass': 47.867, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d2 4s2', 
        'shells': [2, 8, 10, 2]
    },
    'V': {
        'name': 'Vanadium', 
        'color': 'transition_metals', 
        'atomic_number': 23, 
        'mass': 50.942, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d3 4s2', 
        'shells': [2, 8, 11, 2]
    },
    'Cr': {
        'name': 'Chromium', 
        'color': 'transition_metals', 
        'atomic_number': 24, 
        'mass': 51.996, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d5 4s1', 
        'shells': [2, 8, 13, 1]
    },
    'Mn': {
        'name': 'Manganese', 
        'color': 'transition_metals', 
        'atomic_number': 25, 
        'mass': 54.938, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d5 4s2', 
        'shells': [2, 8, 13, 2]
    },
    'Fe': {
        'name': 'Iron', 
        'color': 'transition_metals', 
        'atomic_number': 26, 
        'mass': 55.845, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d6 4s2', 
        'shells': [2, 8, 14, 2]
    },
    'Co': {
        'name': 'Cobalt', 
        'color': 'transition_metals', 
        'atomic_number': 27, 
        'mass': 58.933, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d7 4s2', 
        'shells': [2, 8, 15, 2]
    },
    'Ni': {
        'name': 'Nickel', 
        'color': 'transition_metals', 
        'atomic_number': 28, 
        'mass': 58.693, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d8 4s2', 
        'shells': [2, 8, 16, 2]
    },
    'Cu': {
        'name': 'Copper', 
        'color': 'transition_metals', 
        'atomic_number': 29, 
        'mass': 63.546, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s1', 
        'shells': [2, 8, 18, 1]
    },
    'Zn': {
        'name': 'Zinc', 
        'color': 'transition_metals', 
        'atomic_number': 30, 
        'mass': 65.38, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2', 
        'shells': [2, 8, 18, 2]
    },
    'Ga': {
        'name': 'Gallium', 
        'color': 'post_transition_metals', 
        'atomic_number': 31, 
        'mass': 69.723, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p1', 
        'shells': [2, 8, 18, 3]
    },
    'Ge': {
        'name': 'Germanium', 
        'color': 'metalloids', 
        'atomic_number': 32, 
        'mass': 72.63, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2', 
        'shells': [2, 8, 18, 4]
    },
    'As': {
        'name': 'Arsenic', 
        'color': 'metalloids', 
        'atomic_number': 33, 
        'mass': 74.922, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3', 
        'shells': [2, 8, 18, 5]
    },
    'Se': {
        'name': 'Selenium', 
        'color': 'non_metals', 
        'atomic_number': 34, 
        'mass': 78.96, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p4', 
        'shells': [2, 8, 18, 6]
    },
    'Br': {
        'name': 'Bromine', 
        'color': 'halogens', 
        'atomic_number': 35, 
        'mass': 79.904, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5', 
        'shells': [2, 8, 18, 7]
    },
    'Kr': {
        'name': 'Krypton', 
        'color': 'noble_gases', 
        'atomic_number': 36, 
        'mass': 83.798, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6', 
        'shells': [2, 8, 18, 8]
    },
    'Rb': {
        'name': 'Rubidium', 
        'color': 'alkali_metals', 
        'atomic_number': 37, 
        'mass': 85.468, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1', 
        'shells': [2, 8, 18, 8, 1]
    },
    'Sr': {
        'name': 'Strontium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 38, 
        'mass': 87.62, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2', 
        'shells': [2, 8, 18, 8, 2]
    },
    'Y': {
        'name': 'Yttrium', 
        'color': 'transition_metals', 
        'atomic_number': 39, 
        'mass': 88.906, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2', 
        'shells': [2, 8, 18, 9, 2]
    },
    'Zr': {
        'name': 'Zirconium', 
        'color': 'transition_metals', 
        'atomic_number': 40, 
        'mass': 91.224, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2', 
        'shells': [2, 8, 18, 10, 2]
    },
    'Nb': {
        'name': 'Niobium', 
        'color': 'transition_metals', 
        'atomic_number': 41, 
        'mass': 92.906, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1', 
        'shells': [2, 8, 18, 12, 1]
    },
    'Mo': {
        'name': 'Molybdenum', 
        'color': 'transition_metals', 
        'atomic_number': 42, 
        'mass': 95.95, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1', 
        'shells': [2, 8, 18, 13, 1]
    },
    'Tc': {
        'name': 'Technetium', 
        'color': 'transition_metals', 
        'atomic_number': 43, 
        'mass': 98, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2', 
        'shells': [2, 8, 18, 13, 2]
    },
    'Ru': {
        'name': 'Ruthenium', 
        'color': 'transition_metals', 
        'atomic_number': 44, 
        'mass': 101.07, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1', 
        'shells': [2, 8, 18, 15, 1]
    },
    'Rh': {
        'name': 'Rhodium', 
        'color': 'transition_metals', 
        'atomic_number': 45, 
        'mass': 102.91, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1', 
        'shells': [2, 8, 18, 16, 1]
    },
    'Pd': {
        'name': 'Palladium', 
        'color': 'transition_metals', 
        'atomic_number': 46, 
        'mass': 106.42, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10', 
        'shells': [2, 8, 18, 18]
    },
    'Ag': {
        'name': 'Silver', 
        'color': 'transition_metals', 
        'atomic_number': 47, 
        'mass': 107.87, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1', 
        'shells': [2, 8, 18, 18, 1]
    },
    'Cd': {
        'name': 'Cadmium', 
        'color': 'transition_metals', 
        'atomic_number': 48, 
        'mass': 112.41, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2', 
        'shells': [2, 8, 18, 18, 2]
    },
    'In': {
        'name': 'Indium', 
        'color': 'post_transition_metals', 
        'atomic_number': 49, 
        'mass': 114.82, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1', 
        'shells': [2, 8, 18, 18, 3]
    },
    'Sn': {
        'name': 'Tin', 
        'color': 'post_transition_metals', 
        'atomic_number': 50, 
        'mass': 118.71, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2', 
        'shells': [2, 8, 18, 18, 4]
    },
    'Sb': {
        'name': 'Antimony', 
        'color': 'metalloids', 
        'atomic_number': 51, 
        'mass': 121.76, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p3', 
        'shells': [2, 8, 18, 18, 5]
    },
    'Te': {
        'name': 'Tellurium', 
        'color': 'metalloids', 
        'atomic_number': 52, 
        'mass': 127.60, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p4', 
        'shells': [2, 8, 18, 18, 6]
    },
    'I': {
        'name': 'Iodine', 
        'color': 'halogens', 
        'atomic_number': 53, 
        'mass': 126.90, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p5', 
        'shells': [2, 8, 18, 18, 7]
    },
    'Xe': {
        'name': 'Xenon', 
        'color': 'noble_gases', 
        'atomic_number': 54, 
        'mass': 131.29, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6', 
        'shells': [2, 8, 18, 18, 8]
    },
    'Cs': {
        'name': 'Cesium', 
        'color': 'alkali_metals', 
        'atomic_number': 55, 
        'mass': 132.91, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s1', 
        'shells': [2, 8, 18, 18, 8, 1]
    },
    'Ba': {
        'name': 'Barium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 56, 
        'mass': 137.33, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 18, 8, 2]
    },
    'La': {
        'name': 'Lanthanum', 
        'color': 'lanthanides', 
        'atomic_number': 57, 
        'mass': 138.91, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 5d1 6s2', 
        'shells': [2, 8, 18, 18, 9, 2]
    },
    'Ce': {
        'name': 'Cerium', 
        'color': 'lanthanides', 
        'atomic_number': 58, 
        'mass': 140.12, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f1 5s2 5p6 5d1 6s2', 
        'shells': [2, 8, 18, 19, 9, 2]
    },
    'Pr': {
        'name': 'Praseodymium', 
        'color': 'lanthanides', 
        'atomic_number': 59, 
        'mass': 140.91, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f3 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 21, 8, 2]
    },
    'Nd': {
        'name': 'Neodymium', 
        'color': 'lanthanides', 
        'atomic_number': 60, 
        'mass': 144.24, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f4 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 22, 8, 2]
    },
    'Pm': {
        'name': 'Promethium', 
        'color': 'lanthanides', 
        'atomic_number': 61, 
        'mass': 145, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f5 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 23, 8, 2]
    },
    'Sm': {
        'name': 'Samarium', 
        'color': 'lanthanides', 
        'atomic_number': 62, 
        'mass': 150.36, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f6 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 24, 8, 2]
    },
    'Eu': {
        'name': 'Europium', 
        'color': 'lanthanides', 
        'atomic_number': 63, 
        'mass': 151.96, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 25, 8, 2]
    },
    'Gd': {
        'name': 'Gadolinium', 
        'color': 'lanthanides', 
        'atomic_number': 64, 
        'mass': 157.25, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 25, 9, 2]
    },
    'Tb': {
        'name': 'Terbium', 
        'color': 'lanthanides', 
        'atomic_number': 65, 
        'mass': 158.93, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f9 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 27, 8, 2]
    },
    'Dy': {
        'name': 'Dysprosium', 
        'color': 'lanthanides', 
        'atomic_number': 66, 
        'mass': 162.50, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f10 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 28, 8, 2]
    },
    'Ho': {
        'name': 'Holmium', 
        'color': 'lanthanides', 
        'atomic_number': 67, 
        'mass': 164.93, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f11 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 29, 8, 2]
    },
    'Er': {
        'name': 'Erbium', 
        'color': 'lanthanides', 
        'atomic_number': 68, 
        'mass': 167.26, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f12 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 30, 8, 2]
    },
    'Tm': {
        'name': 'Thulium', 
        'color': 'lanthanides', 
        'atomic_number': 69, 
        'mass': 168.93, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f13 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 31, 8, 2]
    },
    'Yb': {
        'name': 'Ytterbium', 
        'color': 'lanthanides', 
        'atomic_number': 70, 
        'mass': 173.05, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 6s2', 
        'shells': [2, 8, 18, 32, 8, 2]
    },
    'Lu': {
        'name': 'Lutetium', 
        'color': 'lanthanides', 
        'atomic_number': 71, 
        'mass': 174.97, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d1 6s2', 
        'shells': [2, 8, 18, 32, 9, 2]
    },
    'Hf': {
        'name': 'Hafnium', 
        'color': 'transition_metals', 
        'atomic_number': 72, 
        'mass': 178.49, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d2 6s2', 
        'shells': [2, 8, 18, 32, 10, 2]
    },
    'Ta': {
        'name': 'Tantalum', 
        'color': 'transition_metals', 
        'atomic_number': 73, 
        'mass': 180.95, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d3 6s2', 
        'shells': [2, 8, 18, 32, 11, 2]
    },
    'W': {
        'name': 'Tungsten', 
        'color': 'transition_metals', 
        'atomic_number': 74, 
        'mass': 183.84, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d4 6s2', 
        'shells': [2, 8, 18, 32, 12, 2]
    },
    'Re': {
        'name': 'Rhenium', 
        'color': 'transition_metals', 
        'atomic_number': 75, 
        'mass': 186.21, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d5 6s2', 
        'shells': [2, 8, 18, 32, 13, 2]
    },
    'Os': {
        'name': 'Osmium', 
        'color': 'transition_metals', 
        'atomic_number': 76, 
        'mass': 190.23, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d6 6s2', 
        'shells': [2, 8, 18, 32, 14, 2]
    },
    'Ir': {
        'name': 'Iridium', 
        'color': 'transition_metals', 
        'atomic_number': 77, 
        'mass': 192.22, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d7 6s2', 
        'shells': [2, 8, 18, 32, 15, 2]
    },
    'Pt': {
        'name': 'Platinum', 
        'color': 'transition_metals', 
        'atomic_number': 78, 
        'mass': 195.08, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d9 6s1', 
        'shells': [2, 8, 18, 32, 17, 1]
    },
    'Au': {
        'name': 'Gold', 
        'color': 'transition_metals', 
        'atomic_number': 79, 
        'mass': 196.97, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s1', 
        'shells': [2, 8, 18, 32, 18, 1]
    },
    'Hg': {
        'name': 'Mercury', 
        'color': 'transition_metals', 
        'atomic_number': 80, 
        'mass': 200.59, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2', 
        'shells': [2, 8, 18, 32, 18, 2]
    },
    'Tl': {
        'name': 'Thallium', 
        'color': 'post_transition_metals', 
        'atomic_number': 81, 
        'mass': 204.38, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p1', 
        'shells': [2, 8, 18, 32, 18, 3]
    },
    'Pb': {
        'name': 'Lead', 
        'color': 'post_transition_metals', 
        'atomic_number': 82, 
        'mass': 207.2, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p2', 
        'shells': [2, 8, 18, 32, 18, 4]
    },
    'Bi': {
        'name': 'Bismuth', 
        'color': 'post_transition_metals', 
        'atomic_number': 83, 
        'mass': 208.98, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p3', 
        'shells': [2, 8, 18, 32, 18, 5]
    },
    'Po': {
        'name': 'Polonium', 
        'color': 'metalloids', 
        'atomic_number': 84, 
        'mass': 209, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p4', 
        'shells': [2, 8, 18, 32, 18, 6]
    },
    'At': {
        'name': 'Astatine', 
        'color': 'metalloids', 
        'atomic_number': 85, 
        'mass': 210, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p5', 
        'shells': [2, 8, 18, 32, 18, 7]
    },
    'Rn': {
        'name': 'Radon', 
        'color': 'noble_gases', 
        'atomic_number': 86, 
        'mass': 222, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6', 
        'shells': [2, 8, 18, 32, 18, 8]
    },
    'Fr': {
        'name': 'Francium', 
        'color': 'alkali_metals', 
        'atomic_number': 87, 
        'mass': 223, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s1', 
        'shells': [2, 8, 18, 32, 18, 8, 1]
    },
    'Ra': {
        'name': 'Radium', 
        'color': 'alkaline_earth_metals', 
        'atomic_number': 88, 
        'mass': 226, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s2', 
        'shells': [2, 8, 18, 32, 18, 8, 2]
    },
    'Ac': {
        'name': 'Actinium', 
        'color': 'actinides', 
        'atomic_number': 89, 
        'mass': 227, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d1 7s2', 
        'shells': [2, 8, 18, 32, 18, 9, 2]
    },
    'Th': {
        'name': 'Thorium', 
        'color': 'actinides', 
        'atomic_number': 90, 
        'mass': 232.04, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d2 7s2', 
        'shells': [2, 8, 18, 32, 18, 10, 2]
    },
    'Pa': {
        'name': 'Protactinium', 
        'color': 'actinides', 
        'atomic_number': 91, 
        'mass': 231.04, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f2 6d1 7s2', 
        'shells': [2, 8, 18, 32, 20, 9, 2]
    },
    'U': {
        'name': 'Uranium', 
        'color': 'actinides', 
        'atomic_number': 92, 
        'mass': 238.03, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f3 6d1 7s2', 
        'shells': [2, 8, 18, 32, 21, 9, 2]
    },
    'Np': {
        'name': 'Neptunium', 
        'color': 'actinides', 
        'atomic_number': 93, 
        'mass': 237, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f4 6d1 7s2', 
        'shells': [2, 8, 18, 32, 22, 9, 2]
    },
    'Pu': {
        'name': 'Plutonium', 
        'color': 'actinides', 
        'atomic_number': 94, 
        'mass': 244, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f6 6d1 7s2', 
        'shells': [2, 8, 18, 32, 24, 8, 2]
    },
    'Am': {
        'name': 'Americium', 
        'color': 'actinides', 
        'atomic_number': 95, 
        'mass': 243, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f7 6d1 7s2', 
        'shells': [2, 8, 18, 32, 25, 8, 2]
    },
    'Cm': {
        'name': 'Curium', 
        'color': 'actinides', 
        'atomic_number': 96, 
        'mass': 247, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f7 6d1 7s2', 
        'shells': [2, 8, 18, 32, 25, 9, 2]
    },
    'Bk': {
        'name': 'Berkelium', 
        'color': 'actinides', 
        'atomic_number': 97, 
        'mass': 247, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f9 6d1 7s2', 
        'shells': [2, 8, 18, 32, 27, 8, 2]
    },
    'Cf': {
        'name': 'Californium', 
        'color': 'actinides', 
        'atomic_number': 98, 
        'mass': 251, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f10 6d1 7s2', 
        'shells': [2, 8, 18, 32, 28, 8, 2]
    },
    'Es': {
        'name': 'Einsteinium', 
        'color': 'actinides', 
        'atomic_number': 99, 
        'mass': 252, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f11 6d1 7s2', 
        'shells': [2, 8, 18, 32, 29, 8, 2]
    },
    'Fm': {
        'name': 'Fermium', 
        'color': 'actinides', 
        'atomic_number': 100, 
        'mass': 257, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f12 6d1 7s2', 
        'shells': [2, 8, 18, 32, 30, 8, 2]
    },
    'Md': {
        'name': 'Mendelevium', 
        'color': 'actinides', 
        'atomic_number': 101, 
        'mass': 258, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f13 6d1 7s2', 
        'shells': [2, 8, 18, 32, 31, 8, 2]
    },
    'No': {
        'name': 'Nobelium', 
        'color': 'actinides', 
        'atomic_number': 102, 
        'mass': 259, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d1 7s2', 
        'shells': [2, 8, 18, 32, 32, 8, 2]
    },
    'Lr': {
        'name': 'Lawrencium', 
        'color': 'actinides', 
        'atomic_number': 103, 
        'mass': 262, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d1 7s2', 
        'shells': [2, 8, 18, 32, 32, 8, 3]
    },
    'Rf': {
        'name': 'Rutherfordium', 
        'color': 'transition_metals', 
        'atomic_number': 104, 
        'mass': 267, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d2 7s2', 
        'shells': [2, 8, 18, 32, 32, 10, 2]
    },
    'Db': {
        'name': 'Dubnium', 
        'color': 'transition_metals', 
        'atomic_number': 105, 
        'mass': 270, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d3 7s2', 
        'shells': [2, 8, 18, 32, 32, 11, 2]
    },
    'Sg': {
        'name': 'Seaborgium', 
        'color': 'transition_metals', 
        'atomic_number': 106, 
        'mass': 271, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d4 7s2', 
        'shells': [2, 8, 18, 32, 32, 12, 2]
    },
    'Bh': {
        'name': 'Bohrium', 
        'color': 'transition_metals', 
        'atomic_number': 107, 
        'mass': 270, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d5 7s2', 
        'shells': [2, 8, 18, 32, 32, 13, 2]
    },
    'Hs': {
        'name': 'Hassium', 
        'color': 'transition_metals', 
        'atomic_number': 108, 
        'mass': 277, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d6 7s2', 
        'shells': [2, 8, 18, 32, 32, 14, 2]
    },
    'Mt': {
        'name': 'Meitnerium', 
        'color': 'unknown', 
        'atomic_number': 109, 
        'mass': 276, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d7 7s2', 
        'shells': [2, 8, 18, 32, 32, 15, 2]
    },
    'Ds': {
        'name': 'Darmstadtium', 
        'color': 'unknown', 
        'atomic_number': 110, 
        'mass': 281, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d9 7s1', 
        'shells': [2, 8, 18, 32, 32, 17, 1]
    },
    'Rg': {
        'name': 'Roentgenium', 
        'color': 'unknown', 
        'atomic_number': 111, 
        'mass': 280, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d10 7s1', 
        'shells': [2, 8, 18, 32, 32, 18, 1]
    },
    'Cn': {
        'name': 'Copernicium', 
        'color': 'unknown', 
        'atomic_number': 112, 
        'mass': 285, 
        'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 5f14 6d10 7s2', 
        'shells': [2, 8, 18, 32, 32, 18, 2]
    }
}

compounds = {
    'H2O': {
        'elements': ['H', 'H', 'O'],
        'name': 'Water',
        'uses': 'Essential for life, solvent',
        'properties': 'Colorless, odorless liquid'
    },
    'CO2': {
        'elements': ['C', 'O', 'O'],
        'name': 'Carbon Dioxide',
        'uses': 'Carbonated drinks, plant photosynthesis',
        'properties': 'Colorless gas, soluble in water'
    },
    'NaCl': {
        'elements': ['Na', 'Cl'],
        'name': 'Sodium Chloride',
        'uses': 'Common salt, food preservation',
        'properties': 'White crystalline solid, soluble in water'
    },
    'C6H12O6': {
        'elements': ['C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'O', 'O', 'O', 'O', 'O', 'O'],
        'name': 'Glucose',
        'uses': 'Energy source for living organisms',
        'properties': 'Sweet, colorless, crystalline solid'
    },
    'O2': {
        'elements': ['O', 'O'],
        'name': 'Oxygen',
        'uses': 'Respiration, combustion',
        'properties': 'Colorless, odorless gas'
    },
    'CH4': {
        'elements': ['C', 'H', 'H', 'H', 'H'],
        'name': 'Methane',
        'uses': 'Fuel, natural gas',
        'properties': 'Colorless, odorless gas, highly flammable'
    },
    'HCl': {
        'elements': ['H', 'Cl'],
        'name': 'Hydrochloric Acid',
        'uses': 'Stomach acid, industrial cleaning',
        'properties': 'Colorless to slightly yellow liquid, corrosive'
    },
    'NH3': {
        'elements': ['N', 'H', 'H', 'H'],
        'name': 'Ammonia',
        'uses': 'Fertilizer, cleaning agent',
        'properties': 'Colorless gas, pungent odor, highly soluble in water'
    },
    'C2H5OH': {
        'elements': ['C', 'C', 'H', 'H', 'H', 'H', 'H', 'O', 'H'],
        'name': 'Ethanol',
        'uses': 'Alcoholic beverages, fuel, solvent',
        'properties': 'Colorless, volatile liquid, flammable'
    },
    'N2': {
        'elements': ['N', 'N'],
        'name': 'Nitrogen',
        'uses': 'Inert atmosphere for chemical reactions, food preservation',
        'properties': 'Colorless, odorless gas, makes up 78% of Earth\'s atmosphere'
    }
}

periodic_table_layout = [
    ['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Be'],
    ['Li', 'Be', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    ['Na', 'Mg', '', '', '', '', '', '', '', '', '', '', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
    ['K', 'Ca', 'Se', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
    ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
    ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
    ['Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', '', '', '', '', '', ''],
    ['', '', '*', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '#', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '*La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', ''],
    ['', '', '#Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', ''],
]

def draw_element(element, x, y, angle = 0):
    if angle == 0:
        if element and element in elements:
            rect = pygame.Rect(x,y, cell_size,cell_size)
            pygame.draw.rect(screen,elements[element]['color'], rect)
            pygame.draw.rect(screen, black, rect,1)

            symbol = element_font.render(element, True, element_font_color)
            symbol_rect = symbol.get_rect(center=(x+cell_size//2, y+cell_size//2))
            screen.blit(symbol, symbol_rect)

def draw_table():
    for row, elements in enumerate(periodic_table_layout):
        for col, element in enumerate(elements):
            #x position calculation
            x = col * (cell_size + grid_paddiing) + grid_paddiing + table_offset_x 
            #y position calculation
            y = row * (cell_size + grid_paddiing) + grid_paddiing
            #draw the element
            draw_element(element,x,y)

def draw_electron_shells(element, x, y, width, height):
    #electron shell function
    shells = elements[element]['shells']
    #get drawing position
    centerx, centery = x + width // 2, y + height // 2
    for i, electrons in enumerate(shells):
        #find the radius
        radius = (i + 1) * (min(width, height) // (2 * len(shells)))
        pygame.draw.circle(screen, white, (centerx,centery), radius, 1)
        angle_step = 360 / electrons
        for j in range(electrons):
            #electron angle calculation
            angle = math.radians(j * angle_step)
            #electron x position
            ex = centerx + int(radius * math.cos(angle))
            #electron y position
            ey = centery + int(radius * math.sin(angle))
            #draw the circle
            pygame.draw.circle(screen, white, (ex, ey), 2)
def create_tooltip(element):
    #get element info
    information = elements[element]
    #create tooltip text
    tooltipt = f"{information['name']}"
    tooltip = font.render(tooltipt, True,(44,44,47), (229,229,229))
    return tooltip
def draw_tooltip(screen, tooltip, pos):
    #draw the tooltip
    #15px right and 15px down
    screen.blit(tooltip, (pos[0] + 15, pos[1]+15))
def show_element_info(element):
    #get the info
    information =  elements[element]
    lines = [
        f"Name: {information['name']}",
        f"Atomic Number: {information['atomic_number']}",
        f"Mass: {information['mass']}",
        f"Electron Config: {information['electron_config']}"
    ]
    #return the list
    return lines

def show_compound_info(compound):
    #get the information
    info = compounds[compound]
    #make a list of fstrings
    lines = [
        f"Name: {info['name']}",
        f"Formula: {compound}",
        f"Properties: {info['properties']}"
    ]
    #return the fstring list
    return lines

def check_compound(elements):
    #sort the elements into the correct order
    elements.sort()
    #iterate through all compounds
    for compound, data in compounds.items():
        #compare the input elements with each compound
        if elements == sorted(data['elements']):
            return compound, data['name']
    return None, None

def show_popup(message, color):
    #render the popup
    popup = popup_font.render(message,True,color)
    popup_rect = popup.get_rect(center = (width//2,height-260))
    screen.blit(popup, popup_rect)
    pygame.display.flip()
    pygame.time.wait(1500)

def get_element(pos):
    #function based on position
    x,y = pos
    col = (x-table_offset_x) // (cell_size + grid_paddiing)
    row = y // (cell_size+grid_paddiing)
    #validity check
    if row >= 0 and row < len(periodic_table_layout) and col >= 0 and col < len(periodic_table_layout[0]):
        return periodic_table_layout[row][col]
    else:
        return None

def main():
    clock = pygame.time.clock()
    dragging = False
    dragged_element = None
    #merged area for elements
    merge = []
    merge_rect = pygame.Rect(width-200, height-150,180,100)
    #electron shell drawing
    electron_shell_rect = pygame.Rect(width-200, height-260,180,100)
    merge_button = pygame.Rect(width-200,height-40,180,30)
    info_area = []
    hover_element = None
    tooltip = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if merge_button.collidepoint(event.pos):
                    compound, name = check_compound(merge)
                    if compound:
                        #show popup
                        show_popup(f"Created {name} ({compound})",white)   
                    else:
                        show_popup("No compoound formed", red)
                    merge = []
                else:
                    element = get_element(event.pos)
                    if element and element in elements:
                        dragging = True
                        dragged_element = element
                        info_area = show_element_info(element)
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    if merge_rect.collidepoint(event.pos) and dragged_element:
                        merge.append(dragged_element)
                    else:
                        show_popup(f"{elements[dragged_element]['name']}", white)
                dragged_element = None
        screen.fill(background)
        draw_table()
        pygame.draw.rect(screen, white, merge_rect,2)
        for i, elem in enumerate(merge):
            draw_element(elem, merge_rect.x+10 + i*40, merge_rect.y+10)
        pygame.draw.rect(screen,white, electron_shell_rect,2)
        if merge:
            draw_electron_shells(merge[-1], electron_shell_rect.x, electron_shell_rect.y, electron_shell_rect.width, electron_shell_rect.height)
        pygame.draw.rect(screen, white, merge_button)
        merge_text = font.render("Merge", True, black)
        screen.blit(merge_text, (merge_button.x+70, merge_button.y+8))
        info_Rect = pygame.Rect(10, height-150, 300, 140)
        for i, line in enumerate(info_area):
            info_text = font.render(line, True, white)
            screen.blit(info_text, (info_Rect.x, info_Rect.y + i*30))
        mouse_pos = pygame.mouse.get_pos()
        hover_element = get_element(mouse_pos)
        if hover_element and hover_element in elements:
            tooltip = create_tooltip(hover_element)
        else:
            tooltip = None
        if tooltip:
            draw_tooltip(screen, tooltip, mouse_pos)
        if dragging and dragged_element:
            x,y = pygame.mouse.get_pos()
            draw_element(dragged_element, x - cell_size // 2, y - cell_size // 2)
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    #if needed
    main()
