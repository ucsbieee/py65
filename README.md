
# Py65ucsbieee

Respository: <https://github.com/ucsbieee/py65>

Py65ucsbieee is a fork of [mnaberez/py65](https://github.com/mnaberez/py65). Here are the changes from the original:

- 1.1.0ucsbieee (2021-05-23)
  - `WAI` instruction acts as if an IRQ is always pending.
  - `do_goto()` no longer pauses on `BRK`, and now pauses on `STP`.

## Getting Started

To build and install py65ucsbieee:

~~~bash
cd ${PY65UCSBIEEE}
python setup.py install --user
~~~

Now, `py65mon` should be installed. Note that you may need to configure your envoronment variables.

To run:

~~~bash
py65mon
~~~

# Py65

Py65 was originally created by [Mike Naberezny](https://github.com/mnaberez). It can be found here: [mnaberez/py65](https://github.com/mnaberez/py65).

Py65 is well documented here: [py65.readthedocs.org](http://py65.readthedocs.org/).
