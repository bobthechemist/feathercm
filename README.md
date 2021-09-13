# What is FeAtHEr-Cm?

FeAtHEr-Cm is a platform for building a better understanding of scientific instrumentation. It is my attempt at developing what I call an *Instrumental Approach to Chemical Analysis*. Traditionally, the second semester of analytical chemistry covers instrumentation used in the discipline. Recent advances in technology, electronics and programming allow us to explore how scientific measurements are made by designing our own instruments and using them to explore chemical systems. FeAtHEr-Cm helps us do that.

# Why FeAtHEr-Cm?

When exploring platforms that could be useful for introducing chemists it scientific instrumentation design, I wanted something that was relatively inexpensive, easy to operate, established, and supported by a larger community.  The [feather platform](https://learn.adafruit.com/adafruit-feather) by Adafruit Industries checks all of those boxes *plus* provides a cross-compatible platform with a vast array of tools already available.  The flexibility comes at a cost, however, and that is the array of choices that can be made is a bit overwhelming.  To bring some focus to the project, I have made two design decisions:

* The microcontroller board that will serve as the brains of any FeAtHEr-Cm instrument is the M4 Express and there is no intention to make activities compatible with other microcontrollers.
* All programming will be done in [Circuit Python](circuitpython.org)

The primary reason for selecting the M4 is that this microcontroller contains two 12-bit digital-to-analog outputs, which simplifies many designs (not least of which is the potentiostat).  The analog inputs are also 12 bit which is a very nice feature in education-based instrumentation.  By limiting software design to circuit python we not only decrease the programming learning curve (only one language is needed to control and communicate with the instrument) but it increases the accessibility of the instrument by being a plug and play option.  Note that a big downside to the M4 is that the analog to digital converter (ADC) isn't as good as it needs to be, which is why *the instrument you build is not suitable for research applications*.  There are tweaks made (and being made) to address the problems so that the potentiostat remains easy to build and configure while still serving as a meaningful learning platform.

As for that odd capitalization, it is something I've done for a long time.  I'm not alone and there are [many chemists](https://www.ionicviper.org/) who do this.

# What is the status?

The electronics activities, code and instructional materials are still a work in progress.  Presently, the introductory materials (concepts of instrumental design and introductions to microcontrollers, circuit python and soldering) are complete and building a potentiostat is in a draft form.  The second instrument (building a turbidity meter) is in the design stage.  The remaining two projects (a thermal conductivity detector and rudimentary chromatograph) are merely conceptual.

# Can I contribute?

Yes!  I suspect most participants will want to propose suggestions, raise questions and identify errors in the material.  We can do that through the issues tab.  If you are comfortable with Github, don't hesitate to fork the project so you can make pull requests.

The textbook (activities and background) is written using [restructured text](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#headings) which makes creating web and PDF documents straightforward while using a minimal amount of formatting.  It also allows for fairly easy integration of math and chemical formulas.  All programming needs to be done in circuit python and the *official* microcontroller for the project is the M4 express.

# Where is the material stored?

I'm currently using [readthedocs](https://www.readthedocs.io) to host the "textbook".  The primary advantage is that changes made to the github source get built at RTD within a few minutes.  In addition, RTD can create alternate formats (such as PDF) without any additional work on our part.


[![Documentation Status](https://readthedocs.org/projects/feathercm/badge/?version=latest)](https://feathercm.readthedocs.io/en/latest/?badge=latest)
