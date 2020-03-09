# Adapted from PsychoPy demo
# Used to illustrate drifting grating stimuli in Murray et al. 2018

from psychopy import core, visual, event

# Parameters
duration_s = .2
grating_contrast = .5

# create a window to draw in
win = visual.Window([400, 400.0], allowGUI=False)

# INITIALISE SOME STIMULI
gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1', contrast=grating_contrast)
gabor.autoDraw = True
message = visual.TextStim(win, pos=(0.0, -0.9), text='Hit Q to quit')
trialClock = core.Clock()

# repeat drawing for each frame
while trialClock.getTime() < duration_s: 
    gabor.phase += 0.01
    message.draw()
    # handle key presses each frame
    if event.getKeys(keyList=['escape', 'q']):
        win.close()
        core.quit()

    win.flip()

win.close()
