#!/usr/bin/env python
'''A sample application for cmd2.'''

from cmd2 import Cmd, make_option, options
import unittest, optparse, sys

import salt_cli

class BaseLineApp(Cmd):
    verbose = False
    target = 'none'

    @options([make_option('-v', '--verbose', action="store_true", help="More Detail")
             ])
    def do_target(self, arg, opts=None):
        """ Set the working target(s) using the complex matching, or just the id glob. """
        arg = ''.join(arg)
        self.prompt = '(tgt: {}) '.format(arg) 
        self.target = arg


    def send_line(self, data):
        self.stdout.write(data + '\n')


    def do_toggle(self, arg, opts=None):
        """ Toggles certain boolean style variables """
        arg = ''.join(arg)
        if arg == 'verbose':
            self.verbose =  not self.verbose
            self.send_line('Verbose output: ' + str(self.verbose))
        if arg == 'list':
            self.send_line('{}: {}'.format('Verbose Output', self.verbose))
        else:
            self.send_line('Toggle Options: list verbose')


    def do_env(self, arg, opts=None):
        self.send_line('{}: {}'.format('Target', self.target))
        self.send_line('{}: {}'.format('Verbose', self.verbose))


    def do_salt(self, arg, opts=None):
        """Shell dealing directly with salt"""
        i = salt_cli.SaltLineApp()
        i.set_prompt()
        i.cmdloop()
    

    def do_health(self, arg, opts=None):
        arg = ''.join(arg)
        if arg:
            # Do health checks on argument
            pass
        else:
            # Do health check on self.target
            if self.target == 'none':
                self.stdout.write('Please set your target or specify a host.')
            pass


app = BaseLineApp()
app.cmdloop()
