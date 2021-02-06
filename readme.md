# Ship Simulator:

## About
The main idea behind this project was to better get to know Python. More specificly, how to use classes and threads within the laguage. Software designpatterns aren't yet in place correctly, but are expected to be in order in the future as my knowledge expands. 

Now to what I've actually built. What I've built is an simple ship simulator. It's a ship that sails around a two dimensional XY-plane representing the ocean. The ship is controlled by the user via manual or autopilot. Depending on the user input the wessle will change position and state as seen on a chart and data feed, resp. As we can see in the Block Diagram bellow the ship is built-up by two parts. More on them you'll find in the following parts. 

## Physics and Instruments:
Contains the barebone of the simulator. Interaction with the modules is made easy with 3 outputs to get the state of the simulation. To change the state, two inputs are used. The I/Os are:
- Output: Position, Speed and direction.
- Input: Angle and throttle.

(For more details, check the Wiki.)

## Control panel:
Contains the user interactions with the simulation together with some additional services. Controls and states of the simulation are displayed in a GUI. Additional services are the database and Autopilot.

(For more details, check the Wiki.)

## Block Diagram:

![overview.png](overview.png)
