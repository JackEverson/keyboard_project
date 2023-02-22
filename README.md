# Keyboard Project 

This is the Redox keyboard I have made from scratch. The frame is made from 3d printed, PLA plastic parts. Wiring and soldering was done by hand (no PCB). The Microcontroller is a Raspberry Pi Pico running with Circuit Python and utilising the KMK keyboard libray. This repo contains a directory labeled 'redox_code' which is stable working code. To copy my code it should be as simple as installing Circuit Python on your desired microcontroller and then copy and pasting the contents of the redox_code folder into your device (you may have to re-number the pins in the code depending on your wiring).

This is the current keyboard:



Things I am looking to implement in the future are:

-A new layer that gives access to better motions <br />
-Setting up some macros that can automate repetive tasks <br />
-A gaming layer that allows for on the go macros or key swapping <br />
-~~buying new keycaps (filament 3d printed keycaps have turned out to be quite scratchy)~~ <br />
-~~upgrading joining cable to be detachable~~ <br /> 

I suspect I will never truly be done with this project as I will always want to be making adjustments, implementing new design choices, or even making new keyboards. I have therefore created a timeline so that what improvements have been made can be appreciated more fully. 

## Making of Redox keyboard
03JAN2023

I have 3d printed the frame of this keyboard using the STL files provided by MattDB on Thingiverse (https://www.thingiverse.com/thing:2704567/files). I have 3d printed the keycaps using STL files also provided on Thingiverse. I used transparent PLA filament for the frame and grey PLA filament for the keycaps. In hindsight, the transparent PLA would have been more suitable if I was introducing lighting effects into the keyboard (potentially later this can happen) and PLA for keycaps is not a great experience. 

I chose to use the Raspberry Pi Pico due to its power, ease of use, and price point. I acquired mine from Core-Electronics (https://core-electronics.com.au/raspberry-pi-pico.html?gclid=CjwKCAiA9NGfBhBvEiwAq5vSyzyWNIwh7zqMT8yNNUex2AOg3EC2hyN4nSSwGvXdT2K5udIXR_YyjBoC3oAQAvD_BwE). I then set the Pico up with CircuitPython (more information can be found at https://circuitpython.org/) so I could utilize KMK firmware (More information can be found at http://kmkfw.io/). This means that the keyboards programming is written out in Python ('MicroPython' technically). I appreciate CircuitPython and KMK as it has allowed me to make adjustments to my keyboard's code on the fly. The keyboard appears as a storage device and code.py can be adjusted at will and when saved the board will update in real time. This avoids the hassle of needing to compile and then flash the code to the Pico everytime. It does come with it's faults however. Being able to adjust the code on any computer also means I can break the code on any computer if I start to adjust the code.py script and introduce an error. I have also had issues with some computers trying to format and 'fix errors' on the board as they recognise it as a storage device. Overall, I have a positive view of the KMK library but would like to try out QMK at a later point (this uses C and needs to be compiled and flashed to the board giving (in my opinion) a more stable and less code breakable keyboard).

My actual code is quite simple and is laid out in a 14x5 grid utilising a QWERTY layout (this can be seen in the redox_code directory in the code.py file). I have had to make some movements to typical placements (for example backspace is now under the right thumb and `/~ and =/+ are now accessed on the right side of the left keyboard) but I am getting used to these oddities. I am experimenting with layers to give me access to arrow keys similar to that found in Vim, and access to the function keys. 

The wiring of the keyboard is achieved using a hand wired 'matrix'. This consists of 5 rows leading into 14 columns via diodes (pictures can be seen bellow). The joining cable is both just a continuing join for the 5 rows and directly connects all 7 of the columns directly into the Pico microcontroller. I'm not sure I am happy with this arrangement as if the joining cable is caught or pulled on by something it is directly attached to the fragile keyboard matrix and the Pico microcontroller. 

## Buying commercially available keycaps
14JAN2023

While it was nice to say that I had made all the plastic components of the keyboard myself, filament 3d printed keycaps had a tendency of getting stuck while trying to push keys, they felt quite scratchy and cheap to use, and I couldn't deny that they didn't look amazing. I therefore ordered some new low profile keycaps online (core electronics https://core-electronics.com.au/keycaps-for-mx-mechanical-keyboard-switches-pack-of-16-kit18-black.html?gclid=CjwKCAiA0cyfBhBREiwAAtStHAHOeJdRYrlzAaPDVHhf5ekOtMIlCpGAmhNHuppfY-7PPkSdw9rEuxoCn1gQAvD_BwE) which felt amazing in combination with the Gateron Brown switches and gave the keyboard a more finished and professional look. 

![20230114_123416](https://user-images.githubusercontent.com/111256162/212447383-ab533fd3-095f-4bb4-a475-d8b823ab701c.jpg)

## Upgraded to HDMI cable ports to connect the two halves of the Redox keyboard 
21FEB2023 

I have Upgraded my redox keyboard to use HDMI ports rather than having the two halves hard wired together. I was worried that having the two halves directly wired to the keyboard matrix would eventually lead to the cord getting caught on something and ripping something important out. Now the cord is able to be disconnected easily, the makes it much easier for movement around a work space and travel. Initially the plan was to use internal computer power connectors, but I believe this would have looked unprofessional and replacement would have required me to wire together a new cable each time. I did look into using VGA cables, but I needed 12 conductors in the cable, and while VGA does have 15 pins, a number of these are common ground which made it unsuitable. I settled on HDMI, as the cables are common and cheap, they have 19 separate conductors inside of the cable, and they would be relatively easy to solder the way I needed them.
