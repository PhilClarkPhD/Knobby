# Knobby
Knob control program for ex vivo fast-scan cyclic voltammetry (FSCV)

Ex vivo FSCV experiments in the España lab run like a well-oiled machine - everything is automated! Well, almost everything...

Once you have placed your working and reference electrodes you can step away from the rig except for one thing. You'll have to come back every 20 minutes for the next 2 hours just to turn a knob! So, so close to full automation.

If we didnt have to worry about this step we would have much more freedom to read, do surgeries, or work on our github profiles without worrying about missing a timer or physically bumping into the rig and ruining our experiment (a rare but devastating event). I built Knobby to eliminate those issues and finally give us a fully automated FSCV setup.

Knobby consists of an array of 6 servos each attached to a knob via a custom 3D-printed adaptor. The servos are connected to an arduino running the standard firmata protocol which then connects to the computer via USB.  The GUI was made in Tkinter and allows manual control of the knobs, but also includes an autorun function that, if selected, will automatically turn the knobs at user-defined intervals. 

It's simple and it works!
