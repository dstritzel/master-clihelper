'''This will handle all of the salt based stuff'''

from cmd2 import Cmd, make_option, options
import unittest, optparse, sys

target = 'none'


class SaltCommonElements(Cmd):
    def do_target(self, arg, opts=None):
        global target
        arg = ''.join(arg)
        target = arg
        self.set_prompt()


class SaltCommandMode(SaltCommonElements):
    def set_prompt(self):
        self.prompt = "CMD_MODE(target: {})# ".format(target)


    def default(self, arg, opts=None):
        self.do_shell('salt -C "{}" cmd.run \'{}\''.format(target, arg))


class SaltLineApp(SaltCommonElements):
    def set_prompt(self):
        self.prompt = "Salt(target: {})# ".format(target)


    def do_state(self, arg, opts=None):
        """ Runs the specified state on the target. Use the 'target' command to set. """
        arg = ''.join(arg)
        self.do_shell('salt -C "{}" state.sls {}'.format(target, arg))


    def do_highstate(self, arg, opts=None):
        """  Runs a highstate on targets """
        arg = ''.join(arg)
        self.do_shell('salt -C "{}" state.sls {}'.format(target, arg))
   
 
    def do_run(self, arg, opts=None):
        """ Enters a cmd.run mode for all the targets """
        i = SaltCommandMode()
        self.stdout.write("To exit command mode use EOF or exit\n")
        self.stdout.write("Be VERY CAREFUL as almost every command will be sent to the minions.\n")
        i.set_prompt()
        i.cmdloop()
        self.set_prompt()
