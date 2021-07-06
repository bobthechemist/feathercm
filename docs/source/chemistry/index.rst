The FeAtHEr-Cm Textbook
=======================

Roadmap for version 1.0
~~~~~~~~~~~~~~~~~~~~~~~

Initially, content is not going to be self-standing and will leverage other textbooks that adequately cover theory and pre-requisite material.  Texts such as Skoog's *Principles of Instrumental Analysis* and Harris' *Quantitative Chemical Analysis* are sufficiently ubiquitous that a student will likely have access to one or both of those texts.  Harvey's *Analytical Chemistry 2.1* provides adequate background material on chemical theory and is freely accessible.  These texts will be referenced when background material is necessary.  Rather than reinvent the wheel, there will be little attempt to cover material that is already available in Harvey's text, so once it becomes necessary to introduce content that is presented in one of the "closed" textbooks, the focus will be on expanding on where Harvey lets off.

Building and using a potentiostat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An instrumental approach to voltammetric measurements will center on the construction of a potentiostat, which requires a basic understanding of circuits involving resistors, capacitors and operational amplifiers.  Circuit analysis at the level of Kirchhoff's voltage/current laws is not necessary and will not be presented.  Coverage of operational amplifiers will be limited to the two ideal principles of op amps (no current draw from the inputs and the voltage difference between the inputs is zero).

The potentiostat used in this course is built with problem-based exploration as a foundational design principle.  Not only are we ignoring important electrical engineering design concepts (which are beyond the scope of this program), but the resulting potentiostat will allow individual components to be probed and analyzed.  For example, the components used to define a virtual ground are also used to introduce the concept of a voltage divider and explore why voltage dividers need to be buffered with an operational amplifer.

Lastly, there is an excellent circuit simulation package available on the internet that is incorporated into the text.  It allows for just-in-time exploration of concepts that are introduced and will allow students to compare actual results to theoretical results.

The expected student trajectory is as follows:

1. Electronics principles
  * Understand what a voltage divider is and how it is created using two resistors
  * Explore relationship between resistor magnitude, power consumed and output voltage
  * Analyze the effect of an external load on a voltage divider
  * Compare simulated and actual performance metrics with the bob173.
2. An overview of operational amplifiers and their utility
  * Understand that an operational amplifier can compare the relative values of the input voltages
  * Explore the role of op amps in buffering an input
  * Evaluate how performance of a real operation amplifier compares to the ideal behavior of drawing no current.
    - This section will likely be the first entry into (circuit) python programming.
  * Explore how operational amplifiers can add multiple inputs together.
  * Explore how operational amplifiers can magnify the intensity of a signal.
3. Combining the elements - a basic adder potentiostat
  * Learn how to read a schematic
  * Explore python programming needed to communicate with the bob173
  * Calibrate voltage and current scales of the bob173
  * Perform a cyclic voltammetry experiment and analyze results
4. Going further - improving the potentiostat
  * Reducing noise
  * Incorporating iR compensation
  * Exploring instrument limitations
  * Exploring a "new" chemical system.

Building a colorimeter
~~~~~~~~~~~~~~~~~~~~~~

One of the most prevalent instrument design activities is the construction of a rudimentary spectrometer.  Rather than provide yet another example, the proposed instrument design activities will focus on several under-represented concepts:

* Exploring how an instrument controls/operates a source and records information from a detector
* Analyze non-idealities due to instrument design (a primary example is stray light)
* Investigating signal transduction for novel data acquisition strategies (one example might be transducing detector response to an audio signal)

One design idea is to intentionally incorporate source flicker into the instrument.  Then create a system that provides dual-beam capabilities and explore how effective this approach is at reducing such noise.

Concepts covered in this module will include electronics (transimpedance amplifiers), programming (digital and analog IO), deviations from Beer's Law and signal transduction.  It may also be an interesting segue into 3D printing design.


Building a thermal conductivity detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to exploring chromatography instrumentation, we need to have a reasonable detector.  It is possible that one could use concepts in the previous sections (spectroscopy, voltammetry) to design a detector, and that could/should be part of a future direction.  Here we are interested in exploring a detector that is often described in instrumental analysis courses, the thermal conductivity detector.  Designing and testing the detector will provide an opportunity to further develop our electronics understanding through the development of a Wheatstone bridge.  The goal would be to develop an instrument that can, for example, analyze a binary gas sample.  The approach we are revisiting was first described in J. Chem Ed. 28, 576 (1951) and it is time we revisit this approach.

Creating a rudimentary Gas Chromatograph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The previous module presented an approach to analyzing gaseous mixtures, which suggests that by adding a means to separate mixtures prior to TCD analysis should result in a functioning GC.  There are DIY GC designs on the internet that use packed columns (one of them actually uses kitty litter) which might be sufficient to perform alcohol separations.
