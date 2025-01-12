
# Py65ucsbieee

Respository: <https://github.com/ucsbieee/py65>

Py65ucsbieee is a fork of [mnaberez/py65](https://github.com/mnaberez/py65). Here are the changes from the original:

- ucsbieee (2021-11-20)
  - `WAI` instruction acts as if an IRQ is always pending.
  - `do_goto()` no longer pauses on `BRK`, and now pauses on `STP`.
  - `BRK` now pushes correct `RTI` address.
  - `_run()` now checks for stop condition on first instruction.

## Getting Started

To build and install py65ucsbieee:

```bash
cd ${PY65UCSBIEEE}
python3 setup.py install --user # don't use sudo
```

Now, `py65mon` should be installed. Note that you may need to configure your envoronment variables.

To run:

```bash
py65mon
```

# Py65

Py65 was originally created by [Mike Naberezny](https://github.com/mnaberez). It can be found here: [mnaberez/py65](https://github.com/mnaberez/py65).

Py65 is well documented here: [py65.readthedocs.org](http://py65.readthedocs.org/).
