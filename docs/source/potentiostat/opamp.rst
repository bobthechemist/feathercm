Important Op Amp Circuits
=========================

Operational amplifiers have many uses in scientific instrumentation, and they play a central role in the design of a modern potentiostat.  We will see shortly that the four op amps in the potentiostat we build perform one of three different roles: buffering an input signal; adding input signals together; amplifying a current while converting it to a voltage.  We will take a closer look at these three op amp uses.

Op amps as buffers
******************

A major problem with using a voltage divider to drive a load is that any resistive load applied to a voltage divider *becomes part of the voltage divider*.  A careful inspection of the voltage divider circuit highlighted that one way to circumvent the influence of load on a voltage divider is to prevent current flowing through the divider from also flowing into the load.  In other words, if it is possible to block (or buffer) the voltage divider from the rest of the circuit, it should function as intended. An operational amplifier can perform this function, and an example is shown in the simulation below.

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/ygje45bd' frameborder='0'></iframe>

The 22 kOhm potentiometer is set up to divide the 3.3 V input voltage in half, resulting in an output of 1.65 V.  A 1 kOhm load resistance greatly attenuates the output voltage (you should be able to determine this value of ~ 253 mV); however, the op amp keeps the output voltage at the desired value.

First, let's emphasize that an op-amp buffer configuration has the output pin tied to the inverting input pin and the non-inverting pin is connected to the voltage divider.  Recall that an op amp tries to keep the difference between the two input pins equal to zero, which means that it will try to set the inverting input to 1.65 V.  Since this pin is also connected to the output, the output will remain at 1.65 V.

Notice in the simulation that no current is flowing into the non-inverting pin of the op amp.  As far as the voltage divider is concerned, the op amp looks like a huge resistor.  This characteristic of an op amp is called *input impedance* and an ideal op amp has such a high input impedance that *no current flows into the inputs*.  In reality, op amps have a finite input impedance, meaning that they will draw a small amount of current.

.. admonition:: You try

  Now would be a good time to start exploring datasheets of operational amplifiers.  Perform a websearch on "MCP6004 datasheet" to find the specifications of the op amp used in your potentiostat.  Look through the table to find the value of *input impedance*.  Use this value to estimate the amount of current flowing into the non-inverting input if the input voltage is 1.65 V.

One may ask where the current is coming from that exits the op amp.  The answer is the *power supply*.  Not shown in the schematic is that the op amp is connected to the ground and +3.3 V rails of the instrument.  If you pay close attention to the schematic for the bob173, you'll note that one of the four op amps has two extra pins to indicate connections to the power supply.  Circuit components that require power to function properly are referred to as *active components*.  Those we have used earlier (resistors, photoresistors, potentiometers) are examples of *passive components* that do their job without the use of a power supply.

.. admonition:: You try

  There is one more buffer located in the bob173 schematic.  Can you find it?
