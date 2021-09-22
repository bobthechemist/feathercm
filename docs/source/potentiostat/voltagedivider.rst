.. _voltagedivider:

The Voltage Divider
===================

Introduction and prerequisite reading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A voltage divider is a simple-yet-important circuit that turns a large voltage into a smaller one.  It will appear in several parts of the potentiostat, most importantly in creating something called *virtual ground*\ [#]_.  Upon completing this activity, you should have a better understanding of what a voltage divider circuit is, the mathematics behind voltage dividers, how to select components for a desired voltage, and how voltage dividers are used in a few real-world applications.

Before starting this activity, read this `introductory tutorial from Sparkfun <https://learn.sparkfun.com/tutorials/voltage-dividers/all>`_.

Simulated voltage dividers
~~~~~~~~~~~~~~~~~~~~~~~~~~

The model below depicts a voltage divider with two 1 kOhm resistors and a 5 Volt power supply.  The desired output voltage is obtained from the point in between the two resistors.  The triangle-like shape is called *ground* and allows for all current paths to complete a loop.  (Not shown is that the power supply is also connected to ground.)

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/ygwgal3q' frameborder='0'></iframe>

Explore this simulation by doing the following:

* Change the values of the resistors and observe how they impact the output voltage.  To make this exercise more manageable, limit your resistor choices so that the *sum* of the resistance remains 2k  (e.g. 500 and 1.5k, 250 and 1.75k).  Determine if the output potential is proportional to the top resistor or the bottom resistor.
* The simulator indicates the flow of current with yellow dots.  Placing the mouse over a component will reveal the current flowing through the object and may provide other information.  Mouse over the voltage source and note the power.  Power is calculated using the equation :math:`P = V \times I` with units of Watts (W).  Determine if the current and power change with changing the resistor values.
* Perform the same exploration but start with resistor values of 10k each.  When adjusting the resistor values, keep the total resistance equal to 20k.  Note similarities and differences in the output voltage, current and power.

Create your own circuit:

You may erase the circuit in the on-line textbook (and recover it by refreshing the page) or open a new browser with the `circuit simulator <https://www.falstad.com/circuit/circuitjs.html>`_.  Create a voltage divider with a *potentiometer* instead of two resistors.  Make the input voltage 9 V and select a resistance value that results in a total power draw of less than 1 mW.  Adjust the potentiometer to achieve an output voltage of 3.3 V (approximate).  Some tips on using the simulator:

* The components needed for this circuit are a one-terminal voltage source, ground, potentiometer, and voltmeter.  These items can be found in the Draw menu (submenus Passive Components, Inputs and Sources, and Outputs and Labels).
* Note the shortcut keys (e.g. w for wire, r for resistor) as these come in handy.
* You can save/submit your circuit as a text file from the File menu (Export as Text...).

Real world applications
~~~~~~~~~~~~~~~~~~~~~~~

An important use of voltage dividers is in the measurement of resistive sensors, one example being photoresistors.  A photoresistor is a passive element that has a resistance that changes with the brightness of light shining on it.  The simulator software has a photoresistor element that you can incorporate into a voltage divider.  Create a circuit that can generate a response that is proportional to light brightness.  Consider the following in your design:

* Assume that you only have access to a limited supply of resistors (100 Ohm, 1 kOhm, 10 kOhm).  Which one is best suited for the photoresistor and why?
* Create a plot of output voltage vs light brightness.  For the latter, estimate the percent brightness from the slider (no need to be more precise than 0, 20%, 40%, 60%, 80%, 100%).
* Explore the impact of having the photoresistor in the "upper" vs. "lower" positions of the voltage divider.  Which would you choose and why?
* Identify the data domain conversions implemented in this circuit.  Refer to the data domain map (Figure 6 in Enke's paper)\ [#]_

Another real-world application is *level shifting*, which is important when one wants to communicate between two devices with different voltage levels.  For example, while many new sensors utilize 3.3 V in their communication protocols, the ubiquitous Arduino uses 5 V logic, which can damage the sensor.  A voltage divider (much like the one simulated in the *create your own circuit* section) can be used to facilitate uni-directional communication.  You do not need to create a logic shifting circuit, since it is similar to the one above; however, if you are so inclined, it would be useful to find the combination of resistors between 1 kOhm and 10 kOhm that shifts a 5 V signal to a 3.3 V signal.

.. note::

  Voltage dividers **cannot** be used in bi-directional communication because it can only shift a voltage *down*.  A 5 V source can be shifted down to 3.3 V, but a 3.3 V source cannot be shifted *down* to 5 V.


Using the FeAtHEr-Cm voltage divider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up the code
***************

Refer back to :ref:`circuitpython_2` for a refresher on how to read analog input.  Modify that code if necessary to read the analog input from the `PVG` potentiometer, which is connected to analog pin 4 (A4).  Convert the reading to a voltage and print that voltage to the serial console at a rate of 1 hz.  Round the result to 3 decimal places.

Data collection
***************

Adjust the knob of the PVG potentiometer so that the output reads in the neighborhood of 1.65 V.  Collect voltage readings as a function of the number of knob turns from this location.  Make note of the direction (clockwise or counterclockwise) but it is not necessary that you do both in this experiment.  Aim for 6 to 10 data points.

Do some math
************

* Estimate the :math:`\Delta R/turn` of the potentiometer (:math:`R_{total}=22\ k\Omega`) noting that the total number of turns is 25.
* Create an expression that relates the upper resistance (:math:`R_1`) to the input voltage (:math:`V_{in}=3.3\ V`), the output voltage (:math:`V_{out}`) and the total resistance of the potentiometer.
* Repeat the above process for the lower resistance (:math:`R_2`).

Plot and analyze
****************

* Create a spreadsheet with columns for the number of turns, output voltage and calculated upper/lower voltages.
* Create three plots with output voltage, or resistance plotted as a function of number of turns.
* Find the slopes of the three plots.  For the resistance plots, determine if there should be a relationship between the two slopes.
* Use the `LINEST()` function in Excel to find the error in slope of the upper resistor plot.  Find the percent relative error in the slope.  Compare the slope to the expected :math:`\Delta R/turn` value calculated earlier.

Before proceeding, adjust the potentiometer such that the output voltage is :math:`1.65\pm 0.01` V.

Exploring the impact of load
****************************

Until now, the voltage divider has been used to produce a voltage, but the produced voltage has not been used.  For example, one might want the produced voltage to turn on an LED or drive a motor.  The general term for these cases is *load*.  In the following activity, you will explore the impact of load on the ability of a voltage divider to supply the desired voltage.

* Identify the location of the resistor labeled RLD on the FeAtHEr-Cm potentiostat.
* Note the output voltage indicated by the Python script while no resistor is in the RLD slot.  Then insert a resistor (1 kOhm, 10 kOhm, 100 kOhm) and note the change in output voltage.
* Repeat the previous step with the remaining resistors and develop a relationship between the load and the *error* in the output voltage.
* Remove the RLD resistor and adjust the voltage divider to 2.5 V.  Repeat the above steps.  Do this one more time with the voltage divider set to 0.75 V and determine how the magnitude of the error changes with the desired output voltage.
* Identify any trend between the magnitude of the load resistance and the total resistance of the potentiometer.  Under what conditions is the output voltage error the smallest?
* Summarize the relationships between load resistance, desired output voltage and actual output voltage in several brief sentences.

Upon completion of this activity, you should have a better understanding of what a voltage divider is, some real-world applications as well as limitations.  Since the potentiostat we build depends on using a voltage divider to drive a load, the next section will discuss how to overcome the limitations presented here.

.. rubric:: Footnotes

.. [#] We will cover the concept of virtual ground later.
.. [#] C.G. Enke, *Anal. Chem.*, **1971**, *43*, 69A `link <https://dx.doi.org/10.1021/ac60296a764>`_

.. warning:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=voltagedivider.rst&labels=documentation>`_ and share your thoughts there.
