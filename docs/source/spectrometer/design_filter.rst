.. _turbidity_design_filter:

Exploring active/passive filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ideally, one should design an instrument such that data are collected in the absence of noise.  Unfortunately, this situation can rarely - if ever - be realized.  Therefore, it is necessary to filter noise from an instrument's signal.  The theory, design and application of filters can become very complex, and our treatment here is design to introduce the concept and focus on one aspect of filtering that is relevant to the turbidimetry project.

The most rudimentary filter can be formed with a capacitor and resistor in series.  Since these components do not require power in order to operate, an RC filter is referred to as passive.

.. only:: latex

  .. note:: Visit `<https://tinyurl.com/yh478el3>`_ to view this interactive image

.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/yh478el3' frameborder='0'></iframe>

In this figure, The voltage source consists of an AC component with an amplitude of 0.5 V and a DC component with a magnitude of 0.5 V.  The signal is passed through a resistor then capacitor.  The output signal is measured at the point *in between* the two components.  It is important that the components are in the designated order.

At a frequency of 10 hz, the output signal nearly mimics the input signal.  The peak voltage should be around 1 V.  Increase the frequency to 100 hz and you'll notice that the output no longer looks like the input.  The peak voltage is around 579 mV.  Increasing the frequency further to 1000 hz and the output loses nearly all of the AC component and what remains is the 0.5 V DC signal.  The high frequency component has effectively been removed while the DC component remains; hence, the name of this circuit is a *passive low pass filter*.

A more sophisticated, yet accessible filter involves the use of an operational amplifier, and is therefore referred to as an active filter.  The operational amplifier looks to be in a buffer-like configuration with the inverting input tied to the output.  A capacitor is in a feedback loop with the non-inverting input.  The two pairs of resistors and capacitors share the same values and the resulting output has a slightly better performance than the passive filter.  As we will explore more fully, the added complexity of the active filter results in overall better performance.

.. only:: latex

  .. note:: Visit `<https://tinyurl.com/yfnc3kgh>`_ to view this interactive image

.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/yfnc3kgh' frameborder='0'></iframe>

In the simulation below, you will find both of these filters, along with an operational amplifier in an adder configuration that combines three sources: a DC signal; an AC signal; and white noise.  Perform the tasks noted below the simulation.  By the conclusion of this activity, you should be able to compare and contrast the two types of filters and understand their performance limitations.  You will also learn some terminology (dB, transition band) that are used in evaluating filters.

.. only:: latex

  .. note:: Visit `<https://tinyurl.com/yfbh53l2>`_ to perform the activity described below.


.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/yfbh53l2' frameborder='0'></iframe>


* [Do] Identify the three parts of this circuit: the source adder; the passive filter; and the active filter.  The three components are separated by a switch, which can be clicked to direct the source to either of the filters.
* [DO] Note the resistor and capacitor values in the *filter* parts of the circuit.  Are they the same or different?
* [Do] Determine how to change the input by using the sliders for noise and DC signal.  The frequency is set by right clicking on that source component and selecting edit.
* [Do] When finished with introducing yourself to the simulation, refresh the page to reset the simulation to its default values.
* [DO] Note the different in maximum voltage between the passive filter output and the source.
* [PREDICT] Based on what you have learned earlier in this section, what do you expect will happen to these values when the frequency is increased to 400 hz?
* [Explore] Investigate qualitatively how the maximum voltage of the output compares to the maximum voltage of the input as the frequency is changed from 40 to 400 to 4000 hz.  Compare the responses of both filters.
* [REPORT] What is the ratio of output voltage to input voltage for each filter at each of the three frequencies?  Which filter does a better job at eliminating the AC signal?
* [REPORT] Was the prediction you made correct?  If not, identify what was incorrect about it and what misconceptions you may have had.
* [EXCEL] Perform a more quantitative exploration of the output voltage by creating a spreadsheet with the maximum output voltage of each filter at the following frequencies: 1, 2, 5, 7, 10, 12, 15, 17, 20, 50, 70 and 100 Hz.  Insert a column that calculates the log of the frequency
* [PLOT] Create a single plot with the Voltage as a function of the log of frequency.  Include both markers and connected lines in this plot.

The plot you have created describes the performance of the filter as a function of frequency.  It has three regions: one where the signal is essentially unaffected; one where the signal is completely attenuated and a transition region referred to as the *transition band*.  Many applications require that the transition band be as narrow as possible in order to avoid some undesired noise from leaking through the filter.

Filter performance is typically reported using the unit decibels (dB), which is calculated using :math`dB=20 \log(\frac{V_{out}}{V_{in}})`.  We will use this value to define the transition band of each filter and define this region (somewhat arbitrarily) as the region between -3 dB and -20 dB.

* [CALCULATE] Determine the output voltage at -3 dB and -20 dB.
* [CALCULATE] the *percent* of the AC signal that is filtered out at -3 dB and -20 dB.
* [DO] Find the frequency at which the output is -3 dB and -20 dB for each of the filters.  The difference between these values is the width of the transition band.
* [REPORT] Report the width of the transition bands for each of the filters and comment on which filter performs better.

One other characteristic of a filter is its *cutoff frequency* which is equal to :math:`\frac{1}{2 \pi R C}`.

* [CALCULATE] Calculate the cutoff frequency :math:`\frac{1}{2 \pi R C}` for the filter.  Note that since the same values of R and C are used, this characteristic is the same for both the active and passive filters.
* [DO] Find the maximum voltage at the cutoff frequency for each of the filters.
* [CALCULATE] Determine the filter magnitude (in dB) of each filter at the cutoff frequency.

.. tip:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=design_filter.rst&labels=documentation>`_ and share your thoughts there.
