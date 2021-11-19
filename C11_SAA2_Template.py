# Import "pygame" module 
import pygame
# Import "time" module
import time
# Initialize "pygame"
pygame.init() 

# Create a screen of size (400, 500)
screen = pygame.display.set_mode((400,500))
# Set the "screen" title as "Student Additional Activity 2" 
pygame.display.set_caption("Student Additional Activity 2")

# RGB color combinations
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
YELLOW = (255,255,0)

# gdp stands for "Gross Domestic Product"
gdp = [7.862, 8.498, 5.241, 5.456, 6.386, 7.41, 7.996, 8.17, 7.168, 6.811]

# Create a variable 'yloc' and set it to 50. This varialbe helps to display gdp values one below the other.

# Create a variable 'year' and set it to 2009. 


carryOn = True
while carryOn:
    # Fill the screen with "DARKBLUE" color

    
    # Display the text "India's GDP for the years 2009-2018:" at loaction (20, 10)

    

    # Initiate a 'for' that iterates through the list "gdp"


        # Round off "i" value to 2 decimal places

        # Display the text in the form "Year: GDP value" at location (130, yloc)


        # Increment 'yloc' by 40, to display "i" values one below the other

        # Increment 'year' by 1

        
        # Check if user has clicked on close botton on the game window when the counter is running. 
        # If 'True' close the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                pygame.quit()
                
        # Update the contents of display

        # Wait for 1 seconds before displaying next counter value

    # After the all the "gdp" list values are displayed close the window by breaking out of 'while' loop.
    # Use 'break' keyword to exit the 'while' loop

# Wait for 5 seconds before closing the window
                   
# Close the window on the occurence of "pygame.QUIT".        
