# Knobby
**_Knob control program for ex vivo fast-scan cyclic voltammetry (FSCV)_**

Ex vivo FSCV experiments in the España lab run like a well-oiled machine - everything is automated! Well, almost everything...

Once you have positioned your working and reference electrodes you can step away from the rig except for one thing. You'll have to come back every 20 minutes for the next few hours just to turn a knob. So, so close to full automation.

If we didnt have to worry about turning knobs, we would have much more freedom to read papers, do surgeries, or work on our github profiles without worrying about missing a timer or physically bumping into the rig and ruining our experiment (a rare but devastating event). I built Knobby to eliminate those issues and finally give us a fully automated FSCV setup.

Knobby consists of an array of 6 servos each attached to a knob via a custom 3D-printed adaptor. The servos are connected to an arduino running the standard firmata protocol which then connects to the computer via USB.  The GUI was made in Tkinter and allows manual control of the knobs with the pyfirmata library, but also includes an autorun function that, if selected, will automatically turn the knobs at user-defined time intervals. It's a simple solution, and it works!
