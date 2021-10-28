.. _turbidity_design_transistor:

Essentials of transistor switching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Using a transistor switch

  * When using microcontrollers, we have to be careful with how much current is drawn from a pin (https://tinyurl.com/ye4uay78) use of transistor helps us turn a device on and off which little current drawn from the switch itself.

.. only:: latex

  ..note:: Please visit `this link <https://tinyurl.com/ye4uay78>`_ to complete this activity

.. only:: html

  .. raw:: html

    <iframe width='100%' height='500' src='https://tinyurl.com/ye4uay78' frameborder='0'></iframe

* Before looking at the transistor switch, let's focus on the LED circuit.  Mouse over the source and note the max voltage.  There is one resistor in the circuit, so the current should be determined using Ohm's Law.  Turns out this isn't quite right. Mouse over the resistor and note that the voltage drop is only 1.55.  Therefore, the LED is also acting like a resistor of sorts.  If the total voltage is 3.3 V and there is 1.55 dropped across the resistor, how much is dropped across the LED?  This amount is not fixed, and it's impractical to find the value mathematically, so we use a ballpark figure of an LED dropping about 1.8 V.  More importantly is that we want to ensure that there is no more than 20 mA of current flowing through the LED, or else it will be damaged.  So finding an optimal resistance requires

  * Finding remaining resistance (3.3 V - 1.8 V = 1.5 V)
  * Finding a resistor that gives us between 16-18 mA with that voltage (1.5/0.016 or 1.5/0.018 = 94 to 83 Ohm). Rounding to the next highest resistor value (100 typically) gives us a good starting point.

* The problem we note here is that the microcontroller can only deliver 8 mA from its digital IO pins but we want to deliver twice that amount to light the LED.  The transistor will help with this problem.
* One of the uses of a transistor is as a digital switch.  A transistor contains three connections, a collector, base, and emitter.  The base can be thought of as the toggle which turns on/off the flow of current from the collector to the emitter.
* To turn on a transistor switch requires a certain amount of current flowing into the base.  The actual amount of current depends on the type of transistor, but it will roughly be the amount of current we want to flow through our device (16 mA for the LED) divided by 100.
* Since the digital IO pins deliver 3.3 V and we want 160 uA to flow, we need a resistor with a value of about 20 K to apply the correct current to the transistor base.
* Note that the numbers don't quite add up, and that is because the transistor experiences a voltage drop as well, and we haven't taken that into consideration.  Again, this value varies based on the type of resistor and the amount of current flowing, but we can use a ballpark figure of 0.6 - 0.7 V.  So revisiting the entire switch circuit:

  * The signal we are switching is Vt - Vr1 - Vled - Vtrans = 0
  * The switch is Vt - Vr2 - Vtrans = 0

* If we want approximately 16 mA to flow through the LED, we need a resistor that solves 3.3 - (0.016) R - 1.8 - 0.65 = 0

* Here is a `good resource <https://www.nutsvolts.com/?/magazine/article/may2015_Secura>`_ for understanding how a transistor can be used as a digital switch.


.. tip:: See a problem?  Have a suggestion? Please `raise an issue <https://github.com/bobthechemist/feathercm/issues/new?title=design_transistor.rst&labels=documentation>`_ and share your thoughts there.
