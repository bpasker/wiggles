#!python3

# Sleep
import time
from datetime import datetime

# clear Console
import console
import os

# Speech
import speech
import sound


def voiceUpdate(wiggle):

	# Turn on audio even if iPhone silence switch is one
	sound.set_honors_silent_switch(False)
	
	# Say wiggle
	speech.say("Addison now switch to %s" % (wiggle))
	time.sleep(.5)
	
	# Reminder of current wiggle
	speech.say("Please switch to %s" % (wiggle))
	
	# Sleep for while wiggle is done
	for x in range(0, 10):
		time.sleep(1)
		
	# Sound alarm that wiggle is done
	for x in range(0, 120):
		sound.play_effect('Ding_3', 10)
		time.sleep(.3)
		
	# Say wiggle is now done
	speech.say("Addison all done with %s" % (wiggle))
	time.sleep(2)
	
# Set wiggles list 
wiggleList = ["Point Toes", "Knees up", "Head", "windshield Wipers", "Frog Legs", "Full Frog Legs", "Left and Right", "Scoops", "Cross Overs", "Snow Angels", "Hands and Knees"]

# Test wiggle
#wiggleList = ["Point"]

console.clear()

for newWiggle in wiggleList:

	# Clear console from last run
	console.set_idle_timer_disabled(True)
	
	# Update console with wiggle and time started
	print(str(datetime.now().strftime("%H:%M:%S")) + " " + newWiggle)
	
	# Call voice update 
	voiceUpdate(newWiggle)

# Update that wiggles are done
speech.say("You did it! You are all done with wiggles!")
time.sleep(5)

# turn screen sleep back on
console.set_idle_timer_disabled(False)

# Close pythonista app
os.abort()

