# -*- coding: utf-8 -*-
'''
daemon module emulating BSD Daemon(3)

Copyright (c) 2013 wbcchsyn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import os
import errno


__all__ = ['daemon']


def daemon(nochdir=False, noclose=False):
    r''' Fork twice and become a daemon.

         If argument `nochdir' is False, this process changes the calling
         process's current working directory to the root directory ("/");
         otherwise, the current working directory is left unchanged.
         The Default of nochdir is False.

         If  argument `noclose' is False,
         this function close file descriptor 0, 1 and 2 and reopen /dev/null;
         otherwise, leave them.
         The defult value of noclose is False.

         daemon returns the pid of new process.
    '''

    ## 1st fork
    pid = os.fork()
    if pid != 0:
        os.waitpid(pid, os.P_WAIT)
        os._exit(0)

    ## 2nd fork
    os.setsid()
    if os.fork() != 0:
        os._exit(0)

    ## daemon process
    # ch '/'
    if not nochdir:
        os.chdir('/')

    if not noclose:
        # close stdin, stdout, stderr
        for i in xrange(3):
            try:
                os.close(i)
            except OSError as e:
                # Do nothing if the descriptor has already closed.
                if e.errno == errno.EBADF:
                    pass

        # Open /dev/null for stdin, stdout, stderr
        os.open(os.devnull, os.O_RDONLY)  # stdin
        os.open(os.devnull, os.O_WRONLY)  # stdout
        os.dup(1)                         # stderr

    return os.getpid()
