.. _tips:

Tips & Tricks
=============

Here you'll find various bits of information that are useful for working with the FeAtHEr-Cm system.

Obtaining the source code
*************************

The source code is maintained on the `FeAtHEr-Cm Github site <https://github.com/bobthechemist/feathercm>`_.  On the right hand side of this page, you'll find a link to the releases with the latest one displayed.  If you want that one (chances are, you do) go ahead and click on the link, read the release information and download the source code zip file.  It is also possible to click `this link to go directly to the latest release <https://github.com/bobthechemist/feathercm/releases/latest>`_.

The zip file contains more information than you need (such as the raw files used to construct the documentation website).  You will want the material found in the `source` directory.  Copy all of the contents of this directory *except for client.py* onto your microcontroller.  Note that this process will overwrite any code you currently have in `cody.py` so store that in some location if it is necessary.  The `client.py` code is for your computer and allows for communication between the instrument and you.

An example of communicating is in the Example Data section of the Potentiostat module.
