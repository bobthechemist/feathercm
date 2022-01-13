Appendix A - Electronics
========================

A collection of electronics notes and information that is of use.

Decibels
~~~~~~~~

Much like pH, power in electronics can span a wide range of magnitudes; therefore, presenting power using a logarithmic scale is often necessary.

.. math::

  dB = 10 \log{\frac{P_{out}}{P_{in}}}

Decibels are logarithmic ratios of *powers*, but often we use the same unit to describe ratios of amplitudes (e.g. voltage or current).  If a voltage is applied to a resistor, the power is described by:

.. math::

  P = VI \
  I = \frac{V}{R} \
  P = \frac{V^2}{R}

Substituting this expression into the decibel equation:

.. math::

  db = 10 \log{\frac{V^2_{out}}{V^2_{in}}}
  db = 20 \log{\frac{V_{out}}{V^2_{in}}}

So we note that when using the decibel scale to describe power relationships, we use a 10 before the log, and when we are describing magnitudes (voltages or currents) we will be using 20 before the log.
