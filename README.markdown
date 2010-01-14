guppy - Dependency Injection Framework for Python
=================================================

guppy tries to provide a simple, intuitive and pythonic dependency
injection (inversion of control) framework.

guppy is a derivered work of this [ioc pseudo container](http://code.activestate.com/recipes/413268/).


installation
------------

    > python setup.py install


usage examples
--------------

every python object can be registered using the FeatureBroker `features`
with a unique identifier.

    > import guppy
    > guppy.features.Provide('an.identifier', 23)

the registration must be take place before a consumer can require the object.

those consumers can also define the protocol, interface and/or type which the
provided object must implement.

    > assert 23 == guppy.RequiredFeature('an.identifier', guppy.isInstanceOf(int))


bug reporting
-------------

please report bugs [here on github](http://github.com/copton/guppy/issues).


license
-------

[GPLv2](http://www.gnu.org/licenses/gpl-2.0.html)


authors
-------

* Rico Schiekel &lt;fire at downgra dot de&gt;
* Alexander Bernauer &lt;alex at copton dot net&gt;


similar projects
----------------

* Strappy - <http://github.com/asgeir/strappy/>
* SpringPython - <http://springpython.webfactional.com/>
* snake-guice - <http://code.google.com/p/snake-guice/>
* Pinsor - <http://code.google.com/p/pinsor/>
