import pygame
import imgui

from pygame.locals import DOUBLEBUF, OPENGL
from imgui.integrations.pygame import PygameRenderer
from resources import *

def executePrimaryProgram():
    init()
    start()

def init():
    global running
    global impl
    global screen
    global CENTER

    pygame.init()

    screen = pygame.display.set_mode((RESX, RESY), OPENGL | DOUBLEBUF)

    imgui.create_context()

    impl = PygameRenderer()

    CENTER = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    imgui.get_io().display_size = (RESX, RESY)

    # Clear screen
    screen.fill(BASECOLOR)

    running = True


def start():
    global running
    global deltaTime
    global keys
    global impl
    global screen

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            impl.process_event(event)

        imgui.new_frame()

        createBaseWnd()

        # ImGui rendering
        imgui.render()
        impl.render(imgui.get_draw_data())

        # Draw anything else
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pass

        pygame.display.flip()

        deltaTime = clock.tick(60) / 1000

    impl.shutdown()
    pygame.quit()

def createParticle(name, idop, stype, base_quantum_pos, color, size_in_radius):
    # name: Particle Name
    # idop: id of Particle
    # stype: science Type
    # base_quantum_pos: pos of quantum type
    # color: color of particle
    # size_in_radius: size of particle

    idop += 1
    if stype == STYPE_CHEMISTRY:
        # Draw Atom
        pygame.draw.circle(screen, color, base_quantum_pos, size_in_radius)
    elif stype == STYPE_PHYSICS:
        # Draw Atom/smaller Particle with Physical Rules applied
        pygame.draw.circle(screen, color, base_quantum_pos, size_in_radius)
    else:
        # Default is always Quantum Physics
        pygame.draw.circle(screen, color, base_quantum_pos, size_in_radius)

def createBaseWnd():
    ioA = 0

    imgui.set_next_window_size(400,400)
    imgui.begin("Main Menu")

    if imgui.button("Create"):
        createParticle("Hydrogen", ioA, STYPE_CHEMISTRY, CENTER, "red", 20)
        ioA += 1

    imgui.end()