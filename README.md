Py65ucsbieee
============

Py65ucsbieee is a fork of [mnaberez/py65](https://github.com/mnaberez/py65). Here are the changes from the original:

- 1.1.0ucsbieee (2021-14-05)

  - ``WAI`` instruction is now the exact same as the ``BRK`` instruction.
  - ``do_goto()`` no longer pauses on ``BRK``, and now pauses on ``STP``.

Getting Started
---------------

To build and install py65ucsbieee:

```
$ cd ${PY65UCSBIEEE}
$ python setup.py install --user
```

Now, ``py65mon`` should be installed.

Py65
----

Py65 was originally created by [Mike Naberezny](https://github.com/mnaberez).

It can be found here: [mnaberez/py65](https://github.com/mnaberez/py65).

It is well documented here: [py65.readthedocs.org](http://py65.readthedocs.org/).
