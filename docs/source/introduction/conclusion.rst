.. _introduction_conclusion:

Wrapping up the Introduction
============================

*Each module will consist of some concluding remarks and self-check activities to help the learner demonstrate that material has been covered sufficiently.  It is strongly encouraged that the activities presented here be completed, even if they are not officially assigned.*

In order to understand how scientific instrumentation is designed, it is first necessary to learn about some strategies to discuss instrumentation.  In general, the purpose of a scientific instrument is to convert a chemical/physical phenomena into a quantity that can be visualized by the scientist. We used Enke's data domain concept to describe the variety of conversions or *signal transductions* that can occur in scientific instrumentation.\ [Enke1971]_  We then coupled that concept to block diagramming of scientific instruments.  As described by Rayson, virtually all instruments can be subdivided into 5 components: source, sample, detector, discriminator, and output.\ [Rayson2004]_

While this course may be your first introduction to microcontrollers, it is possible that you have had exposure to them in other areas of your life.  Many physics and computer science programs have introduced microcontrollers into their curricula, and hobbyist microcontrollers such as the Arduino are becoming widespread in home-made light shows, sensor and actuator applications.  Here, you have been introduced to the M4 Express, which has a set of features amenable to scientific instrument design.  We have relied quite heavily on `Adafruit's overview page <https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-pins-and-modules>`_ to explore how to update the microcontroller, explore the pinouts and program the device using `Circuit Python <https://circuitpython.org/>`_ and the `Mu editor <https://codewith.mu/>`_.

You have been introduced to some basic programming in Circuit Python (CP) and should be familiar with importing libraries, setting variables, defining functions, and creating loops and conditional statements.  You have also learned how to send and receive binary information from the digital pins as well as reading and interpreting an analog signal.

Lastly, you have learned how to solder and have followed instructions for building your very first instrument.  In the next section, you will explore that instrument further, learning what the components are in the instrument and how they function.

Self Check
~~~~~~~~~~

1. Draw the block diagram of two scientific instruments with which you are familiar (e.g. a pH meter and a visible spectrometer).
2. Identify what data domain conversions occur within or between the blocks in the instruments you diagramed in the previous question.
3. Confirm that your microcontroller is running the latest firmware and update it if necessary.
4. Write a program that will use the on-board red LED to display the Morse code for the chemical symbol of technetium when the user presses a tactile switch.

.. tip:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=conclusion.rst&labels=documentation>`_ and share your thoughts there.
