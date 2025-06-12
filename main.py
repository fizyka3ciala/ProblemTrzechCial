import pygame
import numpy as np

WIDTH, HEIGHT = 1200, 800
CENTER = np.array([WIDTH // 2, HEIGHT // 2])
SCALE = 100

G = 1.0
dt = 0.001
SUBSTEPS = 5
SUBSTEPS_MIN = 0
SUBSTEPS_MAX = 200
MAX_TRAIL = 50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Problem Trzech Ciał")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]

config_data = {
    "Broucke A1": {
        "bodies": [
            [np.array([-0.9892620043, 0.0]), np.array([0.0, 1.9169244185]), 1.0],
            [np.array([2.2096177241, 0.0]), np.array([0.0, 0.1910268738]), 1.0],
            [np.array([-1.2203557197, 0.0]), np.array([0.0, -2.1079512924]), 1.0],
        ],
        "period": 6.283213
    },
    "Broucke A2": {
        "bodies": [
            [np.array([0.336130095, 0.0]), np.array([0.0, 1.532431537]), 1.0],
            [np.array([0.7699893804, 0.0]), np.array([0.0, -0.6287350978]), 1.0],
            [np.array([-1.1061194753, 0.0]), np.array([0.0, -0.9036964391]), 1.0],
        ],
        "period": 7.702408
    },
    "Broucke A4": {
        "bodies": [
            [np.array([0.2843198916, 0.0]), np.array([0.0, 1.377417957]), 1.0],
            [np.array([0.8736097872, 0.0]), np.array([0.0,-0.4884226932]), 1.0],
            [np.array([-1.1579296788, 0.0]), np.array([0.0, -0.8889952638]), 1.0],
        ],
        "period": 8.211617
    },
    "Broucke A5": {
        "bodies": [
            [np.array([0.2355245585, 0.0]), np.array([0.0, 1.2795329643]), 1.0],
            [np.array([0.9712004534, 0.0]), np.array([0.0, -0.4021329019]), 1.0],
            [np.array([-1.2067250118, 0.0]), np.array([0.0, -0.8774000623]), 1.0],
        ],
        "period": 8.689105
    },

    "Broucke A6": {
        "bodies": [
            [np.array([0.1432778606, 0.0]), np.array([0.0, 1.1577475241]), 1.0],
            [np.array([1.1556938491, 0.0]), np.array([0.0, -0.2974667752]), 1.0],
            [np.array([-1.2989717097, 0.0]), np.array([0.0, -0.8602807489]), 1.0]
        ],
        "period": 9.593323
    },

    "Broucke A7": {
        "bodies": [
            [np.array([-0.1095519101, 0.0]), np.array([0.0, 0.9913358338]), 1.0],
            [np.array([1.6613533905, 0.0]), np.array([0.0, -0.1569959746]), 1.0],
            [np.array([-1.5518014804, 0.0]), np.array([0.0, -0.8343398592]), 1.0]
        ],
        "period": 12.055859
    },
    "Broucke A8": {
        "bodies": [
            [np.array([0.1979259967, 0.0]), np.array([0.0 ,1.2224733132]), 1.0],
            [np.array([1.0463975768, 0.0]), np.array([0.0, -0.3527351133]), 1.0],
            [np.array([-1.2443235736, 0.0]), np.array([0.0, -0.8697381999]), 1.0]
        ],
        "period": 18.118189
    },
    "Broucke A9": {
        "bodies": [
            [np.array([0.0557808334, 0.0]), np.array([0.0, 1.0824099428]), 1.0],
            [np.array([1.3308335036, 0.0]), np.array([0.0, -0.2339059386]), 1.0],
            [np.array([-1.3865415370, 0.0]), np.array([0.0, -0.8485040042]), 1.0]
        ],
        "period": 20.897689
    },
    "Broucke A10": {
        "bodies": [
            [np.array([-0.5426216182, 0.0]), np.array([0.0, 0.8750200467]), 1.0],
            [np.array([2.5274928067, 0.0]), np.array([0.0, -0.0526955841]), 1.0],
            [np.array([-1.9848711885, 0.0]), np.array([0.0, -0.8223244626]), 1.0]
        ],
        "period": 32.610953
    },
    "Broucke A11": {
        "bodies": [
            [np.array([0.0132604844, 0.0]), np.array([0.0, 1.054151921]), 1.0],
            [np.array([1.4157286016, 0.0]), np.array([0.0, -0.2101466639]), 1.0],
            [np.array([-1.4289890859, 0.0]), np.array([0.0, -0.8440052572]), 1.0]
        ],
        "period": 32.584945
    },
    "Broucke A12": {
        "bodies": [
            [np.array([-0.337076702, 0.0]), np.array([0.0 ,0.9174260238]), 1.0],
            [np.array([2.1164029743, 0.0]), np.array([0.0, -0.0922665014]), 1.0],
            [np.array([-1.7793262723, 0.0]), np.array([0.0 ,-0.8251595224]), 1.0]
        ],
        "period": 42.823219
    },
    "Broucke A13": {
        "bodies": [
            [np.array([-0.8965015243, 0.0]), np.array([0.0, 0.8285556923]), 1.0],
            [np.array([3.2352526189, 0.0]), np.array([0.0, -0.0056478094]), 1.0],
            [np.array([-2.3387510946, 0.0]), np.array([0.0, -0.8229078829]), 1.0]
        ],
        "period": 59.716075
    },
    "Broucke A14": {
        "bodies": [
            [np.array([-0.2637815221, 0.0]), np.array([0.0, 0.9371630895]), 1.0],
            [np.array([1.9698126146, 0.0]), np.array([0.0, -0.1099503287]), 1.0],
            [np.array([-1.7060310924, 0.0]), np.array([0.0, -0.8272127608]), 1.0]
        ],
        "period": 54.230811
    },
    "Broucke R2": {
    "bodies": [
        [np.array([0.9060893715, 0.0]), np.array([0.0, 0.9658548899]), 1.0],
        [np.array([-0.6909723536, 0.0]), np.array([0.0, -1.6223214842]), 1.0],
        [np.array([-0.2151170179, 0.0]), np.array([0.0, 0.6564665942]), 1.0]
    ],
    "period": 99.0
    },

    "Figure Eight": {
        "bodies": [
            [np.array([-1.0, 0.0]), np.array([0.3471168881, 0.5327249454]), 1.0],
            [np.array([1.0, 0.0]), np.array([0.3471168881, 0.5327249454]), 1.0],
            [np.array([0.0, 0.0]), np.array([-0.6942337762, -1.0654498908]), 1.0]
        ],
        "period": 6.3259139829
    },
    "Clover": {
        "bodies": [
            [np.array([1.0, 0.0]), np.array([0.0, 0.5]), 1.0],
            [np.array([-0.5, np.sqrt(3)/2]), np.array([-np.sqrt(3)/4, -0.25]), 1.0],
            [np.array([-0.5, -np.sqrt(3)/2]), np.array([np.sqrt(3)/4, -0.25]), 1.0]
        ],
        "period": 2 * np.pi  # jedna pełna orbita
    },
    "Circle": {
        "bodies": [
            [np.array([1.0, 0.0]), np.array([0.0, 1.52*0.5]), 1.0],
            [np.array([-0.5, np.sqrt(3)/2]), np.array([-np.sqrt(3)*1.52/4, -0.25*1.52]), 1.0],
            [np.array([-0.5, -np.sqrt(3)/2]), np.array([np.sqrt(3)*1.52/4, -0.25*1.52]), 1.0]
        ],
        "period": 2 * np.pi
    },
    "Chaos 1": {
    "bodies": [
        [np.array([-0.5, 0.0]), np.array([0.0, 0.5]), 1.0],
        [np.array([0.5, 0.0]), np.array([0.0, -0.5]), 1.0],
        [np.array([2, -10.0]), np.array([0.0, 0.5]), 1.0]
    ],
    "period": 0
    },
    "Chaos 2": {
    "bodies": [
        [np.array([-1.0, 0.0]), np.array([0.0, 0.5]), 1.0],
        [np.array([1.0, 0.0]), np.array([0.0, -0.5]), 1.0],
        [np.array([10.0, -2.0]), np.array([-0.7, 0.0]), 1.0]
    ],
    "period": 0
    }
}

config_names = list(config_data.keys())
current_config = config_names[0]
dropdown_open = False
show_controls = False
show_com = False

def reset_bodies():
    return [[p.copy(), v.copy(), m] for p, v, m in config_data[current_config]["bodies"]]

bodies = reset_bodies()
path_history = [[] for _ in range(3)]

trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_colorkey((0, 0, 0))
trail_surface.set_alpha(255)
paused = False

def compute_acceleration(i):
    r_i = bodies[i][0]
    a_i = np.zeros(2)
    for j, (r_j, _, m_j) in enumerate(bodies):
        if i != j:
            diff = r_j - r_i
            dist = np.linalg.norm(diff)
            a_i += G * m_j * diff / dist**3
    return a_i

def to_screen(pos):
    return (CENTER + SCALE * pos).astype(int)

def update():
    accelerations = [compute_acceleration(i) for i in range(3)]
    for i in range(3):
        bodies[i][1] += accelerations[i] * dt
        bodies[i][0] += bodies[i][1] * dt
        path_history[i].append(bodies[i][0].copy())
        if len(path_history[i]) > MAX_TRAIL:
            path_history[i].pop(0)

def reset_simulation():
    global bodies, path_history, trail_surface
    bodies = reset_bodies()
    path_history = [[] for _ in range(3)]
    trail_surface.fill((0, 0, 0))

# --- GUI ---
def draw_dropdown(x, y, w, h, open, selected_name):
    main_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (80, 80, 80), main_rect)
    pygame.draw.rect(screen, (200, 200, 200), main_rect, 2)
    label = font.render(selected_name, True, (255, 255, 255))
    screen.blit(label, (x + 10, y + 5))

    if open:
        for i, name in enumerate(config_names):
            item_rect = pygame.Rect(x, y + (i + 1) * h, w, h)
            pygame.draw.rect(screen, (60, 60, 60), item_rect)
            pygame.draw.rect(screen, (200, 200, 200), item_rect, 1)
            label = font.render(name, True, (255, 255, 255))
            screen.blit(label, (x + 10, y + (i + 1) * h + 5))

    return main_rect, [pygame.Rect(x, y + (i + 1) * h, w, h) for i in range(len(config_names))]

def draw_controls_panel(x, y):
    lines = [
        "[Q] Pokaż środek ciężkości układu",
        "[↑] Przyśpiesz symulację",
        "[↓] Zwolnij symulację",
        "[Spacja] Zatrzymaj symulację",
        "[S] Ukryj ten panel"
    ]
    for i, text in enumerate(lines):
        label = font.render(text, True, (180, 180, 180))
        screen.blit(label, (x, y + i * 25))

def draw_center_of_mass():
    positions = [body[0] for body in bodies]
    masses = [body[2] for body in bodies]
    com = sum(p * m for p, m in zip(positions, masses)) / sum(masses)

    for i in range(3):
        for j in range(i + 1, 3):
            pygame.draw.line(screen, (180, 180, 180), to_screen(positions[i]), to_screen(positions[j]), 1)
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        midpoint = (positions[j] + positions[k]) / 2
        pygame.draw.line(screen, (255, 255, 0), to_screen(midpoint), to_screen(positions[i]), 1)

    pygame.draw.circle(screen, (255, 255, 0), to_screen(com), 5)

def draw():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(0)
    fade.fill((0, 0, 0))
    trail_surface.blit(fade, (0, 0))

    for i in range(3):
        points = [to_screen(p) for p in path_history[i]]
        for j in range(1, len(points)):
            pygame.draw.line(trail_surface, colors[i], points[j - 1], points[j], 2)

    screen.fill((0, 0, 0))
    screen.blit(trail_surface, (0, 0))
    for i, (r, _, _) in enumerate(bodies):
        pygame.draw.circle(screen, colors[i], to_screen(r), 6)

    screen.blit(font.render(f"Status symulacji: {'zatrzymana' if paused else 'uruchomiona'}", True, (200, 200, 200)), (WIDTH - 300, 10))
    screen.blit(font.render(f"Prędkość: {SUBSTEPS} kroków/klatkę", True, (200, 200, 200)), (WIDTH - 300, 30))
    screen.blit(font.render(f"Okres: {config_data[current_config]['period']:.6f}", True, (200, 200, 200)), (WIDTH - 300, 50))

    control_label = font.render("[S] Sterowanie", True, (200, 200, 200))
    control_rect = pygame.Rect(WIDTH - 300, 75, 220, 25)
    pygame.draw.rect(screen, (40, 40, 40), control_rect)
    screen.blit(control_label, (WIDTH - 295, 80))

    if show_controls:
        draw_controls_panel(WIDTH - 295, 110)

    if show_com:
        draw_center_of_mass()

    dropdown_rect, item_rects = draw_dropdown(10, 10, 180, 30, dropdown_open, current_config)

    return dropdown_rect, item_rects, control_rect

running = True
while running:
    clock.tick(60)
    dropdown_rect, item_rects, control_rect = draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_UP:
                SUBSTEPS = min(SUBSTEPS + 5, SUBSTEPS_MAX)
            elif event.key == pygame.K_DOWN:
                SUBSTEPS = max(SUBSTEPS - 5, SUBSTEPS_MIN)
            elif event.key == pygame.K_q:
                show_com = not show_com
            elif event.key == pygame.K_s:
                show_controls = not show_controls

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if dropdown_rect.collidepoint(mx, my):
                dropdown_open = not dropdown_open
            elif dropdown_open:
                for i, rect in enumerate(item_rects):
                    if rect.collidepoint(mx, my):
                        selected = config_names[i]
                        if selected != current_config:
                            current_config = selected
                            reset_simulation()
                        dropdown_open = False
                        break
                else:
                    dropdown_open = False
            elif control_rect.collidepoint(mx, my):
                show_controls = not show_controls

    if not paused:
        for _ in range(SUBSTEPS):
            update()

    pygame.display.flip()

pygame.quit()
