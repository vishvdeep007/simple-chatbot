#<!-- vishvdeep dasadiya , vishvdeep.dasadiya.vd@gmail.com -->
#<!-- 03 nov 2016 -->

import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "stf-startup.xml" , commands = "load aiml b")
    kernel.saveBrain("bit_brain.brn")

# kernel now ready for use
while Ture:
    print kernel.respond(raw_input("Enter your message >> "))