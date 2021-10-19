.. _turbidimetry_design:

Turbidimetry instrument design
==============================

* active/passive filters
* LEDs
* transistor switches
* schematic

Exploring active/passive filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ideally, one should design an instrument such that data are collected in the absence of noise.  Unfortunately, this situation can rarely - if ever - be realized.  Therefore, it is necessary to filter noise from an instrument's signal.  The theory, design and application of filters can become very complex, and our treatment here is design to introduce the concept and focus on one aspect of filtering that is relevant to the turbidimetry project.

The most rudimentary filter can be formed with a capacitor and resistor in series.  Since these components do not require power in order to operate, an RC filter is referred to as passive.  A more sophisticated, yet accessible filter involves the use of an operational amplifier, and is therefore referred to as an active filter.  In the simulation below, you will find both of these filters, along with an operational amplifier in an adder configuration that combines three sources: a DC signal; an AC signal; and white noise.

By the conclusion of this activity, you should have an understanding of what type of filter is being explore (high versus low pas filter) and be able to compare/contrast the two filter designs.  You will also learn some terminology (dB, Bode Plot) that are used in evaluating filters.

.. only:: latex

  .. note:: Visit `<https://tinyurl.com/yfbh53l2>`_ to perform the activity described below.


.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/yfbh53l2' frameborder='0'></iframe>


* Values can be adjusted using the sliders or by right clicking on the source and selecting properties
* Adjust sliders to see what happens to the signal
  * Note that at 40 hz, the passive filter output becomes distorted with max noise
  * Notice the change in peak height before/after filtering
* Adjust switch to see what happens to the two possible outputs
  * which filter attenuates 40 hz signal more?  Is this true for other frequencies?
* Set noise and offset to zero, manually set frequency to 1 hz and its max voltage to 1 V
* Collect data (1,2,5,7,10,12,15,17,20,50,70,100 hz) and record the max voltage for active and passive filter
* Plot Vmax vs Log frequency for each filter.
* Calculate the cutoff frequency using 1/(2 Pi r c)
* Calculate Vmax for -3 dB and -20 dB  (which we will define as the transition band)
* Find the frequency and delta frequency for the two filters
* How much does the passive filter attenuate the cutoff frequency?  Compare to active filter.
