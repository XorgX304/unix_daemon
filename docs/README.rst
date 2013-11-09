unix_daemon
===========
| unix_daemon is a python module emulating BSD daemon(3).
| This module provides a function named daemon.
| If this function is called, the process become a daemon and start to run background.


Requirements
^^^^^^^^^^^^
* Python 2.6 or 2.7
* Unix or Linux platform.

Tested
^^^^^^^^^
* Ubuntu 12.04 (x86_64)
* CentOS 6.4 (x86_64)
* Mac OS X 10.9

Setup
^^^^^
* Install using pip
  ::

    $ sudo pip install unix_daemon

* Install from git.  
  ::

    $ git clone https://github.com/wbcchsyn/unix_daemon.git
    $ cd unix_daemon
    $ sudo python setup.py install

Development
^^^^^^^^^^^
Install requirements to developing copy pre-commit hook from repository.
  ::

    $ git clone https://github.com/wbcchsyn/unix_daemon.git
    $ cd unix_daemon
    $ pip install -r dev_utils/requirements.txt
    $ ln -s ../../dev_utils/pre-commit .git/hooks/pre-commit

