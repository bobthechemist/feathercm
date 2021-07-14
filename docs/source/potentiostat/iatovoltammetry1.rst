The Voltage Divider
===================

In voltammetric measurements, one controls the potential of an electrode immersed in an electrolytic solution containing a redox-active species and observes the current.  In this exercise, you will develop an understanding of how to design an instrument that can perform this experiment.

Let's first look at one approach for setting a potential.  The circuit below is called a *voltage divider* and consists of a voltage source and two resistors.  Notice how the voltage measured in between the two resistors is exactly one half the input voltage of 5 V.

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/ygwgal3q' frameborder='0'></iframe>

  Explore this simulation by doing the following:

* Change the values of the resistors and observe how they impact the output voltage.  To make this exercise more manageable, limit your resistor choices so that the *sum* of the resistance remains 2k  (e.g. 500 and 1.5k, 250 and 1.75k).  Determine if the output potential is proportional to the top resistor or the bottom resistor.
* The simulator indicates the flow of current with yellow dots.  Placing the mouse over a component will reveal the current flowing through the object and may provide other information.  Mouse over the voltage source and note the power.  Power is calculated using the equation :math:`P = V \times I` with units of Watts (W).  Determine if the current and power change with changing the resistor values.
* Perform the same exploration but start with resistor values of 10k each.  When adjusting the resistor values, keep the total resistance equal to 20k.  Note similarities and differences in the output voltage, current and power.
