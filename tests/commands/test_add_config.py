"""Tests for our `kubel init` subcommand."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
import os



class TestAddConfig(TestCase):
#    def test_returns_multiple_lines(self):
#        output = popen(['kubel', 'init'], stdout=PIPE).communicate()[0]
#        lines = output.split('\n')
#        self.assertTrue(len(lines.decode('UTF-8')) != 1)
    def test_returns_not_line(self):
        output = popen(['kubel', 'init', 'gcp', '--force'], stdout=PIPE).communicate()[0]
        lines = output.decode('UTF-8').split('\n')
        print(lines)
        self.assertTrue(len(lines) > 1 and len(lines) < 4)

    def test_returns_adding_config(self):
        output = popen(['kubel', 'add_config', 'jupyter'], stdout=PIPE).communicate()[0]
        self.assertTrue('Adding configuration for jupyter to launch.yaml.' in output.decode('UTF-8'))
