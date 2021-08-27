Start Here
==========

**Welcome**. If you are here, you were either invited or spend an awful lot of time randomly clicking links on the internet...

``FeAtHEr-Cm`` is a platform for building a better understanding of scientific instrumentation.  It is my attempt at developing what I call an *Instrumental Approach to Chemical Analysis.*\ [*]_  Traditionally, the second semester of analytical chemistry covers instrumentation used in the discipline.  Recent advances in technology, electronics and programming allow us to explore how scientific measurements are made by *designing our own instruments* and using them to explore chemical systems.  FeAtHEr-Cm helps us do that.

Why FeAtHEr-Cm?
~~~~~~~~~~~~~~~

When exploring platforms that could be useful for introducing chemists it scientific instrumentation design, I wanted something that was relatively inexpensive, easy to operate, established, and supported by a larger community.  The `feather platform <https://learn.adafruit.com/adafruit-feather>`_ by Adafruit Industries checks all of those boxes *plus* provides a cross-compatible platform with a vast array of tools already available.  The flexibility comes at a cost, however, and that is the array of choices that can be made is a bit overwhelming.  To bring some focus to the project, I have made two design decisions:

* The microcontroller board that will serve as the brains of any FeAtHEr-Cm instrument is the M4 Express and there is no intention to make activities compatible with other microcontrollers.
* All programming will be done in `Circuit Python <circuitpython.org>`_

The primary reason for selecting the M4 is that this microcontroller contains two 12-bit digital-to-analog outputs, which simplifies many designs (not least of which is the potentiostat).  The analog inputs are also 12 bit which is a very nice feature in education-based instrumentation.  By limiting software design to circuit python we not only decrease the programming learning curve (only one language is needed to control and communicate with the instrument) but it increases the accessibility of the instrument by being a plug and play option.  Note that a big downside to the M4 is that the analog to digital converter (ADC) isn't as good as it needs to be, which is why *the instrument you build is not suitable for research applications*.  There are tweaks made (and being made) to address the problems so that the potentiostat remains easy to build and configure while still serving as a meaningful learning platform.

As for that odd capitalization, it is something I've done for a long time.  I'm not alone and there are `many chemists <https://www.ionicviper.org/>`_ who do this.

What about *Mathematica*?
*************************

You'll note that while I mentioned above that all programming will be done using Python, there is a fair amount of Mathematica code floating around these pages.  I've been using Mathematica for many years now, and it is a language with which I'm comfortable.  Therefore, when I need to do something quickly, I'll do it using that language.  Additionally, there's a very good chance that students at an American college or university have access to Mathematica, and even if you don't, you can gain access by running the program on a Raspberry Pi (which includes a free for educational use license).  Despite being a closed source package, Mathematica is fairly accessible and serves as a useful tool for some high-order programming, data manipulation and visualization.  This project will not rely on Mathematica, but examples written in this language will be used to demonstrate how one might integrate these projects into a larger system.

Want to dive in?
****************

If you are excited about this project and want to start exploring right away, then I suggest purchasing an `M4 Feather <https://www.adafruit.com/product/3857>`_  along with Adafruit's `parts pal <https://www.adafruit.com/product/2975>`_.  That will give you nearly all the parts you need, and many that you'll find fun to play with.  The only additional components I suggest would be alligator clips and a quad op amp - the MCP6004 - which isn't sold by Adafruit but you can find it at other vendors.  I purchase from `Newark <newark.com>`_ but you might want to try `Digikey <digikey.com>`_ as they are also a reseller for Adafruit products and you might be able to get all of the components from one vendor.

A work in progress
~~~~~~~~~~~~~~~~~~

This project is in the early stages of development.  If you are visiting, you will likely find links that do not work, documentation that seems to require a significant amount of prerequisite knowledge, and many outlines and placeholders.  My intention for a *version 1.0* of this project is an instrument with activities for each of the three main areas of chemical instrumentation (spectroscopy, electrochemistry and chromatography).  I am currently working on the electrochemistry modules.

An open, collaborative effort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I am building this project using `github <github.com>`_ and `read the docs <readthedocs.com>`_ for a few important reasons.

* Both platforms provide open access to the content, so that others may view, use and modify what is presented here
* Both platforms work nicely together, allowing me to generate both software and instructional content in one location and have it display in a pretty format without much input on my part.
* This approach allows community members to contribute to the project either as content generators or content reviewers.

I imagine that users of the content will find typographical and content errors and wish to propose corrections; others may have suggestions on how to better present content.  With Github, those users should be able to make those requests in a documented, public fashion.  If the changes are accepted, they get pushed immediately to the project.

What to explore right now
~~~~~~~~~~~~~~~~~~~~~~~~~

The current area of activity is building the potentiostat, creating software for controlling it and developing activities for exploring how a potentiostat is built and operated.  Have a look first at :ref:`exampleuse` which shows the data that can be acquired with the potentiostat and how it is analyzed.  Then visit :ref:`voltagedivider` and the 2 or three sections that follow in order to get a feel for how the simulation software is used to introduce the electronics concepts needed to build the potentiostat. Lastly, you can look at :ref:`howtobuild` which presents the schematic among other things.  All other sections will be in various stats of disarray.

.. [*] Yes, this title is homage to Ewing's 1954 text and no, it is not at all suggestive that I am (or ever will be) comparable to Ewing as a scientist.
