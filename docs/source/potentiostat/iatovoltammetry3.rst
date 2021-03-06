An operational amplifier primer
===============================

.. note::

  We saw in the last section that the load we are trying to work with impacts the performance of a resistor-based voltage divider.  Ideally, we need to isolate the voltage divider from the load.  In this section we will learn how a component called an *operational amplifier* can perform that task.

Just the facts
~~~~~~~~~~~~~~

As this material is designed for chemists who need to know (or want to know) some useful electronics, we will skip a lot of the theory behind operational amplifiers and focus on the two important features that make them useful and then move on to several basic configurations that are found frequently in scientific instrumentation.

An operational amplifier is an active component that amplifies weak signals.  It has two inputs (a non-inverting input designated **+** and an inverting input designated **-**) and one output.  The symbol used for operational amplifiers in schematics is a triangle.

.. raw:: html

  <iframe width='100%' height='500' src='https://tinyurl.com/ydptekz5' frameborder='0'></iframe>

Note that in the diagram above, a square wave pulse with amplitude +/- 5 V is applied to the inverting input and the non-inverting input is tied to ground.  Try the following explorations:

* Describe the output in relation to the input
* Mouse over the oscilloscope trace to find the amplitude of the output signal.  Where does this value come from? (Hint: right click on the op amp and select properties.)
* Reconfigure the inputs so that the output signal is in phase with the input signal.

In this circuit, the op amp is behaving as a *comparator*.  It is comparing the two inputs and responding with the following result

* If the inverting input is greater than the non-inverting input (which is tied to ground) then set the output as negative as possible.
* If the inverting input is less than the non-inverting input, then set the output as positive as possible.

Note that the comparator is also amplifying the signal.  Look at the properties of the input signal and note that the voltage of the square wave is :math:`\pm 5\ V` while the output is :math:`\pm 15\ V` for an effective gain of 3.  Notice what happens when the input square wave voltage is decreased further.  For square waves as small as 5 mV, the comparator still provides a crisp output with the voltage limits defined by the input voltages supplied to the operational amplifier.  This behavior is what is expected in an *ideal* situation, however.

The simulation software allows for using a more realistic op amp model.  Swapping out the ideal op amp for a real one (under active building blocks) and note that the output no longer has a crisp switch from low to high and vice versa.  Increasing the voltage of the input square wave restores the behavior to that of the ideal... almost.  Mouse over the output scope and note that the output square wave is not actually cycling between :math:`\pm 15\ V`.  Many real operational amplifiers are not able to set their outputs to the supply voltages.  Those that can are referred to as *rail to rail output*.  Although not demonstrated in this simulation, it is difficult for some op amps to accept input voltages as the rails as well.  Those that can do both (accept and deliver voltage at the power supply limits) are referred to as *rail to rail input/output* or RRIO.

A comparator does one more thing, which isn't readily apparent in the simulation: if the inputs are equal, set the output to zero.

.. note::

  You should be able to give this a try by deleting the ground and adding a wire from the square wave source to the non-inverting input.

Two important points
~~~~~~~~~~~~~~~~~~~~

We'll quickly see that op amps can do much more than just compare the values of their inputs.  As we explore some other configurations, there are two important rules that we must keep in mind:

1. An operational amplifier does everything in its power to make the *difference* between voltages at the inverting and non-inverting inputs be zero.
2. In an ideal operational amplifier, the inputs do not draw any current.

.. warning:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=iatovoltammetry3.rst&labels=documentation>`_ and share your thoughts there.
