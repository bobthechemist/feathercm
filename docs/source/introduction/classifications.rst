Instrument description strategies
=================================

Before building instrumentation, it is useful to have some general approaches to describing instrumentation.  In doing so, we will have an additional tool for breaking down instrumentation into individual components, allowing us to better understand the role of these components and how they contribute to the accuracy and precision of a measurement.  Upon completing this section, you should have a better understanding of

* Block diagrams of scientific instruments
* The concept of data domains
* What a scientific instrument is
* What a measurement is

Block Diagrams
~~~~~~~~~~~~~~

More details to come.  This section covers the concepts presented in Rayson's article. [Rayson2004]_ Learning objectives are:

* Describe the five components of a scientific instrument
* Draw a block diagram of an instrument
* Compare and contrast different scientific instruments using a block diagram
* Evaluate potential impact of component changes in the modification of a scientific instrument

**Implementation notes.** Assuming students are familiar with a spectrometer, it is useful to use this instrument to introduce block diagrams.  After this introduction, students can be asked to draw a block diagram of the papercraft spectroscope that they recently designed.  Comparing the two instruments, students can often identify that the spectroscope combines the source and sample components.

Because the first instrument students design is the potentiostat, it is useful to look at Rayson's block diagram of this instrument (Figure 2 in his article).

Data Domains
~~~~~~~~~~~~

More details to come.  This section covers the concepts presented in Enke's article. [Enke1971]_  Learning objectives are:

* Define data domains
* Understand that a transducer convers data from a non-electrical to electrical domain (and vice versa)
* Evaluate the argument that a scientific instrument performs (at least) two data domain conversions
* Describe a scientific instrument in terms of a sequence of data domain conversions
* Understand that a measurement involves both a difference detector and a reference standard quantity
* Assess the accuracy of a measurement

**Implementation notes.** Data domains build upon block diagrams by first focusing on the last three blocks (discriminator -> detector -> display) of a visible spectrometer.  Data are initially in non-electronic domain (light intensity of a particular wavelength) that is transduced by a photodetector into a voltage or current.  This electrical signal is then further transduced into a number for visual display by the end user.  While the process can occur in two steps in principle, a more realistic path involves data amplification and filtering (both of which involve data domain conversions within the electrical domain) as well as multiple data domain conversions in the non-electrical domain (a good example is the discriminator, which converts light intensity into wavelength-dependent light intensity).  A number of the examples provided in the paper are outdated (unsurprising given that the paper is 50 years old at the time of this writing); however, the strategies proposed remain relevant.
