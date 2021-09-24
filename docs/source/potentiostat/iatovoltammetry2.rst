Voltage Divider Problems
========================

.. note::

  In the last section, you should have noticed that the output voltage varies proportionally with the lower resistor and that the current and power are dependent on the sum of the two resistors. The equation for determining the output voltage is :math:`V_{out}=V_{in}\frac{R_{lower}}{R_{lower}+R_{upper}}`

  In addition, you finished that section by exploring how a resistive load applied to the voltage divider on the bob173 potentiostat impacts the output voltage.  Here, we will use the circuit simulator to explore this phenomenon more systematically.

Setup
~~~~~

One way we could create a variable potential is by changing the resistance values.  A variable resistor, or *potentiometer* provides this functionality.  The circuit below is similar to the one on the previous page, with several important differences:

.. only:: latex

  .. note:: Visit `<https://tinyurl.com/yfeq6ato>`_ to perform the activity described below.

* The two resistors are replaced by a potentiometer, which makes it easy to adjust the resistances above and below the test point while keeping the total resistance the same.  You should see a slider on the right hand side of the simulator that will control the potentiometer position.
* A switch has been added, which can be opened and closed with a double click.
* A new resistor has been added, which is the *load* or the object that we want to apply the output voltage to.

.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/yfeq6ato' frameborder='0'></iframe>



Explore this simulation by doing the following:

* Make sure the switch is open.  Adjust the potentiometer so that the resistances are roughly equal and the output voltage is about 2.5 V.
* Close the switch and note how the output voltage is affected.
* Explore how the voltage difference between open and closed states is affected by the position of the potentiometer.  Where do you see the maximum difference and where is the difference negligible?
* Perform a more systematic analysis by collecting voltage readings (with switch closed) as a function of lower resistance value.  You will need to collect about 11 points: 1 with the potentiometer at its middle setting and one at each of the extremes, then four above and below the middle setting.
* Plot these results along with the expected value, which you can calculate using the voltage divider equation.

Investigation
~~~~~~~~~~~~~

To understand why the load resistor is causing the output of the voltage divider to decrease, we must first recall (or learn) that resistors in a circuit can be mathematically combined, and the math depends on whether the resistors are in series or parallel.  In series, the resistors add as you would expect: two 1-kOhm resistors in series results in a total resistance of 2 kOhm.  If those resistors are in parallel, then the *inverses* of the resistances are added:

.. math::

  \begin{aligned}
  \frac{1}{R_{parallel}}&=\frac{1}{R_1}+\frac{1}{R_2}
  \\[15pt]
  R_{parallel} &= \frac{R_1\times R_2}{R_1+R_2}
  \end{aligned}

Take a closer look at the voltage divider with a resistive load, and you will note that the lower resistor is in parallel with the load.  Because these two resistors can be added together, we are in effect *changing the voltage divider*.  The new voltage divider has the same resistance for :math:`R_{upper}` but :math:`R_{lower}` is now the parallel summed value of the original :math:`R_{lower}` and :math:`R_{load}`.  Incorporating this change into the voltage divider equation, we get:

.. math::
  :label: eq_a

  V_{loaded} = V_{in}\times \frac{R_{lower}R_{load}}{R_{upper}(R_{lower}+R_{load})+R_{lower} R_{load}}


We can further "simplify" this equation by noting that the upper and lower resistances are related to one another, given that we are using a potentiometer.  Substituting :math:`R_{pot}=R_{upper}+R_{lower}` into the above equation, it is possible to remove the upper resistance from the equation, yielding:

.. math::

  V_{loaded} = V_{in}\times \frac{R_{lower}R_{load}}{R_{load}R_{pot}+R_{lower}R_{pot}-R_{lower}^2}

.. admonition:: You try

  Use the above equation to calculate the simulated voltage of a loaded voltage divider to determine if the "experimental" data you obtained from the simulator matches the results expected from the math.

Digging deeper
**************

It is possible to analyze the resistive load error a bit further.  To do so will require a bit of calculus.  If you have a good handle on derivatives, then you should be able to see how the equations presented are connected to one another.  If you have no experience with calculus, then simply follow along and do not be bothered by how one equation leads to the other.

Our goal is twofold: first, we seek to determine quantitative where along the potentiometer will the greatest error due to resistive load occur; and second, we wish to explore how the magnitude of the resistive load influences the voltage divider performance.

We can define the voltage divider error as the ratio of the loaded output to the non-loaded output.  The non-loaded output voltage is equal to :math:`\frac{V_{in}R_{lower}}{R_{pot}}` and the loaded voltage is given above.  The error is then:

.. math::

  \text{error} = \frac{V_{loaded}}{V_{out}} = \frac{R_{load}R_{pot}}{R_{lower}R_{pot}+R_{load}R_{pot}-R_{lower}^2}

Plotting the error as a function of :math:`R_{lower}` you will find that the largest amount of error occurs around the point where the potentiometer is in its central position, :math:`R_{lower}=\frac{R_{pot}}{2}`.  Substituting this equality into the error equation, we obtain an expression for the maximum amount of error that is a function of just the potentiometer and the load resistances.

.. math::

  \text{error}_{max} = \frac{R_{load}R_{pot}}{\frac{R_{pot}^2}{4}+R_{load}R_{pot}}

.. note:: If you know calculus, you should attempt to take the derivative of the error expression (remember tha chain rule) and set the result equal to zero.  Upon simplifying, you should get the above answer.

With an expression for :math:`\text{error}_{max}`, it is now possible to explore how the relationship between the load and potentiometer resistances impact the performance of the voltage divider.  We will consider three conditions, when the two resistances are equal and with the load resistance is considerably larger or smaller than the potentiometer resistance.

.. math::

  \begin{aligned}
  R_{load} &= R_{pot} \\
  R_{load} &= 10 R_{pot} \\
  R_{load} &= 0.1 R_{pot}
  \end{aligned}

When the resistances are equal, :math:`\text{error}_{max}=0.8`, so the voltage divider output is attenuated by 20%.  As the load resistance becomes much larger than the potentiometer resistance, the impact decreases.  At 10 times the resistance of the potentiometer, the load attenuates the voltage divider output by 2.5 percent.  The opposite effect is seen when the load is very small relative to the potentiometer, and when :math:`R_{load} = 0.1 R_{pot}`, the output has been attenuated by over 70% and the voltage divider is clearly not functioning properly.

The end result of this analysis is that a voltage divider can only work properly when the load resistance is much greater than the potentiometer resistance.  This result might suggest that the solution to using voltage dividers is to use the smallest potentiometer resistance possible.  However, one must also keep in mind the power consumption of the potentiometer.  As the potentiometer resistance decreases, the current (and therefore the power) will increase, resulting in a poor use of the power supply.


.. tip:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=iatovoltammetry2.rst&labels=documentation>`_ and share your thoughts there.
