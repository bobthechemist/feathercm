Spectroscopy
==============

Designing turbidity/nephelometry instrument

Outcomes
* A spectroscopic instrument that uses an LED as a source and detector
* Circuit design for signal amplification, passive and active filtering
* 3D printing of a sample holder
* Comparison of home-built vs commercial instrument performance
* Exploring a relevant project idea.


Outcomes in detail
* Electronics
  * What is an LED; how does it make light; how can it be used as a sensor
  * Signal amplification (which is a duplicate of pstat)
  * Using a transistor switch
    * When using microcontrollers, we have to be careful with how much current is drawn from a pin (https://tinyurl.com/ye4uay78) use of transistor helps us turn a device on and off which little current drawn from the switch itself.
  * Explore a passive filter, then compare performance to an active filter.  Benefits of complexity
    * Use Falstad to explore how a low pass filter attenuates an AC signal.  Make the Bode plot?
    * Compare above plot to the active filter.
* 3D printing, designing with OpenSCAD, review of geometry and introduction to arithmetic with shapes
  * Download from `their website <https://openscad.org/>`_
  * Create a device that can hold two LEDs at a fixed angle and incorporate the sample cell.
* Turbidity background
  * `Video from Cleveland water department <https://www.youtube.com/watch?v=aY4xeg6QOtE>`_
  * `Video from Endress-Hauser <https://www.youtube.com/watch?v=qz8xHQJw6qY>`_
  * Discussion of attenuation vs. scattering
* Student design decisions
  * Which filter will be used (on board active does additional gain)
  * Source color (EPA uses White, we'll use red or green)
  * Attenuation vs. scattering
  * Sample holder design
  * Phone wire for easy wiring

Many instrument design labs explore colorimetry or spectrophotometry, and the intention here is not to reinvent the wheel but to add to it.  We will explore some aspects of instrument design such as signal amplification, non-chemical deviations from Beer's Law, signal transduction and task-specific design.

* Review of spectroscopy fundamentals
* Design and implementation of a turbidity meter
* Possibly building an endpoint detector for `this <https://pubs-acs-org.brockport.idm.oclc.org/doi/10.1021/acs.jchemed.0c01165>`_
