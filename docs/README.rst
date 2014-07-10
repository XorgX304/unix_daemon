unix_daemon
===========
| unix_daemon is a python module emulating BSD daemon(3).
| This module provides a function named daemon.
| If this function is called, the process become a daemon and start to run background.


Requirements
^^^^^^^^^^^^
* Python 2.6 or 2.7 or 3.2 or 3.3
* Unix or Linux platform.

Tested
^^^^^^^^^
* Python 2.7 on Ubuntu 12.04 (x86_64)
* Python 2.6 on CentOS 6.4 (x86_64)
* Python 2.7 on Mac OS X 10.9

* Python 3.2 on Ubuntu 12.04 (x86_64)
* Python 3.3 on Mac OS X 10.9

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

Usage
^^^^^
unix_daemon.daemon(nochdir=False, noclose=False)
------------------------------------------------
The process become a daemon and start to run background.

  Arguments
    | If argument 1 'nochdir' is False, the process changes the calling process's current working directory to the root directory ("/");
    | otherwise, the current working directory is left unchanged.
    | The default value of the nochdir is False.

    | If argument 2 'noclose' is False, this function close file descriptors 0, 1 and 2 and redirect them to /dev/null.
    | Even if some of them have been closed, this function open these file descriptors and redirect to /dev/null if noclose is False.
    | The defult value of noclose is False.

  Return Value
    daemon returns the pid of new process.

  Note
    | This function call fork internally to detach tty safely.
    | Be careful to call this function when two or more than two python threads are running.

    | Normary, file descriptors 0, 1 and 2 are correspond to stdin, stdout and stderr.
    | However, even if any of these file discriptors refer to something else, they will still be closed when argument 'noclose' is False.

    | It is a good idea to call this function before creating any threads and before opening any files or sockets.

  Example
    Call unix_daemon.daemon(), then the process run backgrond.

    ::

      import unix_daemon
      import os

      print('pid: %s\n' % os.getpid())

      pid = unix_daemon.daemon()
      with open('/tmp/foo', 'a') as f:
          print('pid: %s\n' % os.getpid())
          f.write('new pid: %s\n' % pid)

    You can see the process id changes and the 2nd print is not displayed.

Development
^^^^^^^^^^^

Install requirements to developing copy pre-commit hook from repository.

::

  $ git clone https://github.com/wbcchsyn/unix_daemon.git
  $ cd unix_daemon
  $ pip install -r dev_utils/requirements.txt
  $ ln -s ../../dev_utils/pre-commit .git/hooks/pre-commit
