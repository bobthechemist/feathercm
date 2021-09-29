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

Op amps as amplifiers
*********************

As the name suggests, op amps can amplify voltage or current signals.  Let's explore the circuit below:

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/yjj4be2d' frameborder='0'></iframe>

First, notice the construction.  The non-inverting input is tied to ground and the inverting input has two connections, one is a *feedback resistor* that is connected to the output source and the other is the input signal, which in this case is a voltage source passed through a resistor.  The simulation indicates that current is flowing from source, through the feedback resistor and into the output pin of the op amp.  The output voltage is -100 mV (with some rounding errors).  How is the output voltage related to the source?

Notice that the source generates a current base upon Ohm's Law (:math:`V=IR`) of 100 :math:`\mu A`.  This current then flows through the feedback resistor to generate a voltage (again, through Ohm's Law) of 100 mV.  However, since we are tied to the inverting input of the op amp, the output voltage has a sign opposite of the input.

.. admonition:: you try

  1. Change one of the circuit elements to result in a positive output voltage.
  2. Convince yourself that the current flow is not impacted by the value of the feedback resistor.  Recall that you can view the current in a circuit by moving the mouse over a wire.
  3. Convince yourself that the circuit elements labeled as *source* do in fact control the current.  You should be able to change the current by altering either the voltage or the resistor.

In addition to viewing the above circuit as a current follower (or current to voltage converter), it is also possible to think of the circuit as a voltage scaler.  To do so, we revisit the two Ohm's Law equations that describe the circuit, and notice that they can be rearranged to eliminate :math:`i` from the equations:

.. math::

    \begin{aligned}
    V_{source} &= i\times R_{source} \\
    V_{output} &= -i\times R_{feedback} \\
    \frac{V_{source}}{V_{output}} &= -\frac{R_{source}}{R_{feedback}}\\
    V_{output} &= -V_{source}\frac{R_{feedback}}{R_{source}}
    \end{aligned}

There is an important point to remember when using an op amp in current-to-voltage (or voltage scaler) applications: the output voltage cannot exceed the power supply rails.  This limit has some hidden consequences for using op amps with microcontrollers because many instructional materials assume that the circuit employs a *bi-polar power supply*, which is not the case for the standard array of microcontrollers.

.. admonition:: you try

  To understand the problem, change the simulation to have a Minimum voltage of 0 and a maximum voltage of 3.3.  With a positive source voltage, is the output voltage the same as that predicted from the equations above?  Is it possible to scale a negative voltage source?

There are two approaches to addressing the lack of a bi-polar power supply (commonly referred to as single source).  One is to design the instrument such that the source will only be one polarity.  We will revisit this concept in the next instrument that uses the current from an illuminated LED.  The second approach is to use the concept of a *virtual ground* that effectively changes what the instrument considers as zero.  That is what is done in the potentiostat.  Before exploring how a virtual ground is made and used, we will look at the last op amp configuration important for this course.

Math with op amps
*****************

With operational amplifiers, it is possible to perform many mathematical operations.  The voltage scaler just described is an example of multiplying a voltage by a constant value.  There are also circuits for adding signals together and performing complex operations like differentiation, integration and even logarithms.  Nowadays, many of the complex operations can be performed sufficiently quickly through software (programming) that they are not done via hardware (circuit design).  Adding signals has a place in designing a potentiostat, so that is the only math-related circuit we will explore.

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/yk6d353w' frameborder='0'></iframe>

In exploring this circuit, you should notice that it has many similarities to the voltage scaler.  The non-inverting input is tied to ground and the inverting input has a feedback resistor tied to the output pin.  The most significant difference is the presence of a *summing point* that ties together multiple sources.  Each one of these sources can be viewed as a current (a combination of voltage and resistor), each of which is added together to generate the current that flows through the feedback resistor.

.. admonition:: you try

  1. Use the voltage/resistor values to determine the current from each of the three sources.
  2. Confirm that the sum of the currents *entering* the summing point equals the current *exiting* this point.

The equation that relates the sources to the output voltage can be expressed as:

.. math::

  \begin{aligned}
  V_{output} &= -R_{feedback} \sum{i_{sources}} \\[20pt]
  V_{output} &= -R_{feedback} \sum_{n=1}^{\infty}{\frac{V_n}{R_n}}
  \end{aligned}

Any number of sources can be added together, limited by physical and practical constraints.  In cases where voltages are to be simply added, all of the resistance values (including :math:`R_{feedback}`) are equal.  It is possible to *subtract* by changing the sign of a voltage source.

.. admonition:: you try

  1. Modify the circuit to generate the average of the three sources.
  2. Modify the circuit to generate a weighted average of the sources, where the 2nd source is weighted twice as much as the other two.
