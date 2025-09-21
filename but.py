import pygame
from pygame_widgets.button import Button
import config as cf


def delay_button(time):
    global delay
    delay = time
    button.hide()
    button_1.hide()
    button_2.hide()

    # time_button()
    # global flag_2
    # flag_2 = True
    # #pygame.draw.circle(screen, (255,255,255), (x, y), radius)
    # screen.blit(aim_pic, (x_1, y_1))
    # pygame.display.flip()
    # # global flag
    print('click')
    return True
def press():
    global button
    global button_1
    global button_2
    button = Button(
            # Mandatory Parameters
            cf.screen,  # Surface to place button on
            100,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height

            # Optional Parameters
            text='easy',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: delay_button(1.5)  # Function to call when clicked on
        )
    button_1 = Button(
            # Mandatory Parameters
            cf.screen,  # Surface to place button on
            450,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height

            # Optional Parameters
            text='normal',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: delay_button(1)  # Function to call when clicked on
        )
    button_2 = Button(
            # Mandatory Parameters
            cf.screen,  # Surface to place button on
            800,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height

            # Optional Parameters
            text='hard',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: delay_button(0.5)  # Function to call when clicked on
        )