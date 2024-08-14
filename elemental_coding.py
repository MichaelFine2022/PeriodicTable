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
    'H':{'name': 'Hydrogen', 'color':non_metals,\
        'atomic_number':1, 'mass':1.008, \
        'electron_config':'1s1','shells':[1]},
    'He':{'name': 'Helium', 'color':noble_gasses,\
        'atomic_number':2, 'mass':4.003, \
        'electron_config':'1s2','shells':[2]},
}
compounds = {
    'H2O':{'elements':['H','H','O'],\
           'name': 'Water', 'uses': \
            'Essential for life, solvent',\
                'properties':'Colorless,odorless liquid'},
    'CO2':{'elements':['C','O','O'],\
           'name':'Carbon Dioxide', 'uses':\
            'Carbonated drinks, plant photosynthesis',\
                'properties':'Colorless gas, soluble in water'},
}
periodic_table_layout = [
    ['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'He'],
    ['Li', 'Be', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    ['Na', 'Mg', '', '', '', '', '', '', '', '', '', '', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
    ['K', 'Ca', 'Se', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
    ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
    ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
    ['Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
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
