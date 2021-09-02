Programming microcontrollers
============================

The M4 Express
~~~~~~~~~~~~~~

The Adafruit Feather M4 Express is a microcontroller that provides sufficient resources and computing power to create pedagogically meaningful scientific instrumentation.  It can be programmed using either C++ or Python, and this text will use the latter - specifically CircuitPython - for all projects.

.. figure:: img/m4thumb.jpg
  :align: center
  :alt: Figure of M4 Express Microcontroller

  The Adafruit Feather M4 Express (courtesy of Adafruit)

For more extensive details on how to use CircuitPython with M4 express, `visit Adafruit's web page <https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-pins-and-modules>`_.  Here you will find a summary of information that is necessary to get up and running.

The Bootloader
**************

All computer and computer-like devices require an operating system, and the software that loads this operating system into memory is called the *bootloader*.  For microcontrollers such as the M4 Express, the bootloader controls what type of programming language can be used for the device.  Due to the ease and accessibility, we use the UF2 bootloader, which allows the microcontroller to understand CircuitPython instructions and also makes updating the code extremely simple.

To install the latest bootloader, you must first `download the most recent stable version <https://circuitpython.org/board/featuer_m4_express>`_.  Next, with the M4 Express connected to your computer with a USB cable, you will double-click the resent button.  At that point, a new drive (FEATHERBOOT) will appear on your computer.  Drag the `.uf2` file you downloaded previously to this drive, which will case the red LED on the board to flicker and the FEATHERBOOT drive will disappear.  A new drive, CIRCUITPY should appear, indicating that you have successfully updated the bootloader.

Programming with Mu
*******************

CircuitPython programs can be generated with any software that can generate text files; however, it is convenient to use a program designed for writing such code.  `Mu <https://codewith.mu/en/download>`_ is a simple program that provides everything needed for this course and is available for Windows, MacOS and Linux.  One of the advantages of Mu is that updating the software on the microcontroller is as simple as pressing the save button in the Mu software.  No additional task is needed.  Additionally, Mu (as well as other IDEs or Integrated Develop Environments) provides a tool for viewing output from the microcontroller using a *serial console*.

Circuit Python
~~~~~~~~~~~~~~

With the latest version of CircuitPython installed on the M4 Express and Mu up and running, it is time to start programming the microcontroller.  Type the following code into the Mu editor:

.. code:: python

  import board
  import digitalio
  import time

  led = digitalio.DigitalInOut(board.LED)
  led.direction = digitalio.Direction.OUTPUT

  while True:
      led.value = True
      time.sleep(0.5)
      led.value = False
      time.sleep(0.5)

Some things to note about python code:

* commands are *case sensitive* which means `True` and `true` are two different things.
* spacing is important.  Note that the code under the `while True:` line has been indented.  The size of the indent isn't important; however the fact that all subsequent lines are indented the same amount is important.

Once the above code is saved in a file named `code.py`, you will notice that a red LED begins to blink regularly on the M4.  Let's break down the code to see what was done.

.. code:: python

  import board
  import digitalio
  import time

These three lines import *modules* into memory.  Modules contain pre-written code that is intended to be reused.  In this case, `board` contains useful information like the location of the red LED.  `digitalio` contains information about controlling the digital inputs and outputs and `time` contains the sleep function, which allows a programmer to insert delays in the code.

.. note:: Look at the remaining code and identify where these modules are used.  You can tell they are used because the module names will precede a period.

.. code:: python

  led = digitalio.DigitalInOut(board.LED)
  led.direction = digitalio.Direction.OUTPUT

The first line highlighted here creates a *variable* called `led` that instructs the program communicate with the output connected to the red LED using digital signaling.  The second line indicates that digital signaling will be output from the microcontroller.

.. code:: python

  while True:
      led.value = True
      time.sleep(0.5)
      led.value = False
      time.sleep(0.5)

The remaining 5 lines contain the bulk of the program.  First a loop is established; the command `while True:` is one way to tell python to keep performing the subsequent tasks indefinitely.  The indentation identifies which commands should be performed during this loop.  The next line, `led.value = True` turns on the LED.  The subsequent lines tell python to do nothing for 0.5 seconds, turn off the LED, and wait another half second before repeating the loop.

Some things to try:

* Adjust the delays so that the LED is on for twice as long as it is off.
* Why are there two delays?  What happens if you remove one of the delays?
* What happens if you start by turning the led off before turning it on?

Before continuing, it is useful to get into the habit of including documentation in the code.  Comments can be included by prepending a line with a `#` symbol.  Any text following that symbol, up until the end of the line, will not be viewed as an instruction.  Excluding the `import` lines, add a comment before each line to describe what the code is doing.
