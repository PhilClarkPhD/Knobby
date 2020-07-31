TESTING PULL REQUEST

# Knobby
Knob control program for slice FSCV

Knobby was written to control the flow of drug solutions in slice FSCV via micro servos. The GUI was made to reflect the color and number of knobs that are available, with each knob color corresponding to a particular drug concentration. The servos (one per knob) receive commands from the computer via an Arduino Uno. The Arduino communicates with the computer via a USB. The servos receive power from 6V battery pack. 

Demon Voltammetry software used for FSCV can be set up to communicate with the Arduino at a user-defined pin (see comments in code) so that Knobby starts automatically when file collections start. Currently, the Autorun button does this. The labels for each knob can be changed in the GUI, and you can select which knobs will run in the Autorun function by selecting or de-selecting the "Run" checkbox for each knob. The default is set to 0.3-30uM cocaine on knobs 2-6 (green thru blue).

The Autorun function turns the first knob ON immediately. After that, it counts up to 7 files, each lasting 180s, before turning on the next knob.

***IMPORTANT*** The autorun function can only be started ONCE PER SESSION.  If you start and stop the autorun function, you must exit and re-open Knobby in order to start Autorun again.  Autorun can be stopped by pressing the STOP button or exiting the program. 
