Voltage Divider Problems
========================

.. note::

  In the last section, you should have noticed that the output voltage varies proportionally with the lower resistor and that the current and power are dependent on the sum of the two resistors. The equation for determining the output voltage is :math:`V_{out}=V_{in}\frac{R_{lower}}{R_{lower}+R_{upper}}`

One way we could create a variable potential is by changing the resistance values.  A variable resistor, or *potentiometer* provides this functionality.  The circuit below is similar to the one on the previous page, with several important differences:

* The two resistors are replaced by a potentiometer, which makes it easy to adjust the resistances above and below the test point while keeping the total resistance the same.  You should see a slider on the right hand side of the simulator that will control the potentiometer position.
* A switch has been added, which can be opened and closed with a double click.
* A new resistor has been added, which is the *load* or the object that we want to apply the output voltage to.

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/yfeq6ato' frameborder='0'></iframe>

Explore this simulation by doing the following:

* Make sure the switch is open.  Adjust the potentiometer so that the resistances are roughly equal and the output voltage is about 2.5 V.
* Close the switch and note how the output voltage is affected.  Collect several data points with varying the resistance and noting the lower resistor value, the output potential with the switch open and the output potential with the switch closed.

.. note::

  Notice how the load is in parallel with the lower resistor.  Since resistors in parallel add as inverses (:math:`\frac{1}{R_{total}}=\frac{1}{R_a}+\frac{1}{R_b}`), the load strongly impacts the performance of the voltage divider.  The load resistance must be much higher than the resistors used in the voltage divider in order to minimize this impact.

  However, using too small of a resistor for the voltage divider will result in excessive power usage.  One cannot optimize both low power consumption and load resistance tolerance.

Problems
~~~~~~~~

#. For a voltage divider with a total resistance of 2 kOhm, what is the minimum load resistance that will have a small (< 5%) impact on the desired output voltage?  (Assume for this exercise that Vout is 1/2 Vmax.)
#. Perform the same calculation for a 20 kOhm voltage divider.
#. Does the R95 (my term) change with changing the desired output voltage?
