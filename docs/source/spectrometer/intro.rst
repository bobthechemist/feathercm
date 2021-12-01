.. _turbidimetry_intro:

Spectroscopy
============

Designing turbidimetry/nephelometry instrument

Many instrument design labs explore colorimetry or spectrophotometry, and the intention here is not to reinvent the wheel but to add to it.  We will explore some aspects of instrument design such as signal amplification, non-chemical deviations from Beer's Law, signal transduction and task-specific design.

Outcomes

* A spectroscopic instrument that uses an LED as a source and detector
* Circuit design for signal amplification, passive and active filtering
* 3D printing of a sample holder
* Comparison of home-built vs commercial instrument performance
* Exploring a relevant project idea.

Project timeline

1. Intro to turbidimetry/nephelometry - building an instrument that can measure the clarity of water

   * Watch intro videos and read paper

2. Setting goals for instrument design and introduction to CAD with OpenSCAD

   * Become familiar with OpenSCAD; develop idea for instrument
   * Download from `their website <https://openscad.org/>`_
   * Which filter will be used (on board active does additional gain)
   * Source color (EPA uses White, we'll use red or green)
   * Sample holder design
   * Phone wire for easy wiring

3. New circuit components: LEDs, transistors and filters

   * Do integrated simulation activities

4. Building the instrument

   * Solder instrument

5. Creating 3D printed prototypes of the instrument

   * 3D printing
   * Create a device that can hold two LEDs at a fixed angle and incorporate the sample cell.

6. Modifying the prototype

   * 3D printing

7. Measurements 1: Instrument setup
8. Measurements 2: Initial data acquisition
9. Measurements 3: Fixing mistakes, testing reproducibility and robustness
10. Presentation

http://www.mdpi.com/1424-8220/14/4/7142 might be interesting to model

.. toctree::
  :maxdepth: 2
  :hidden:
  :numbered:

  theory
  design
  cad
  projects

.. tip:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=intro.rst&labels=documentation>`_ and share your thoughts there.
