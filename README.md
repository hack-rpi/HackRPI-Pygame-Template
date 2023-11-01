# Project Template: Getting Started with Pygame

## Setup and Installation:
1. Ensure you have Python on your machine:
[*Download Python*](https://www.python.org "Click to redirect!")

2. Install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. Verify the installation by running the following Python commands:
   ```python
   import pygame
   print("Pygame version:", pygame.__version__)
   ```

## Getting Started:
1. To get started, you will first want to initalize a Pygame window:
   ```python
   # https://www.pygame.org/docs/
   import pygame

   # Initialize the pygame library
   pygame.init()

   SCREEN_DIMENSIONS = (750, 750)

   # Creating the base pygame screen
   screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
   ```

2. You may notice that the window only appears briefly. This is because we have not established a render loop yet:
   ```python
   ...

   # Creating the base pygame screen
   screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

   # Creating the clock used to frame rate management
   clock = pygame.time.Clock()

   running = True
   while (running):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False

       # Updates the screen
       pygame.display.flip()

       clock.tick(60)
   ```

3. We now have a proper screen! But what if we want to change the color? We can do this by utilizing the `fill()` command:
   ```python
   # Creating the base pygame screen
   screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

   # Creating the clock used to frame rate management
   clock = pygame.time.Clock()

   running = True
   while (running):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False

       # Fills the screen in (r, g, b) format
       screen.fill((255, 0, 0))

       # Updates the screen
       pygame.display.flip()

       clock.tick(60)
   ```

4. Now, lets try adding an external image using the `pygame.image.load()` and `blit()` functions:
   ```python
   # Creating the base pygame screen
   screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

   # Creating the clock used to frame rate management
   clock = pygame.time.Clock()

   logo = pygame.image.load('logo.png')

   running = True
   while (running):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False

       # Fills the screen in (r, g, b) format
       screen.fill((255, 0, 0))

       # Displays the HackRPI logo in (x, y) format
       screen.blit(logo, (60, 60))

       # Updates the screen
       pygame.display.flip()

       clock.tick(60)
   ```

5. Now, it is up to you! There are many more features that Pygame presents and I recommend that you explore them! ***[Pygame Documentation](https://www.pygame.org/docs/ "Click to redirect!")***

## **Template Author:**
   - Name: Anthony Smith | *smitha28@rpi.edu*
