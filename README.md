# ScissorLift
This is where you can find the code for the Great Mojave Rover Scissor Lift.


These files belong to an instructable that I created for The Great Mojave Rover Scissor lift.

Files:
SwitchTest.py - This is a Pyhton3 program to check the operations of the limit switches. 
  Run by typing python3 SwitchText.Py
  The program will respond with "going down"  after engaging the switch away from the servo the prompt will change to "going up". After engaging the switch closest to the server the program will stop.
  
MotorTest.py - this program builds on the SwitchTest.py adding servo commands. 
  You will need the https://www.ethanlipson.com/lx16a-library/ library for the Pi to talk to the servos.
  Running the program the scissor lift will start with an up motion then switch to down and stop.

