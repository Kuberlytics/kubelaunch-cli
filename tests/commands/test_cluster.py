"""Tests for our `kubel cluster` subcommand."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
import os

class TestCluster(TestCase):
#    def test_returns_multiple_lines(self):
#        output = popen(['kubel', 'init'], stdout=PIPE).communicate()[0]
#        lines = output.split('\n')
#        self.assertTrue(len(lines.decode('UTF-8')) != 1)
    def test_returns_not_line(self):
        output = popen(['kubel', 'cluster', 'login', '--dry-run'], stdout=PIPE).communicate()[0]
        lines = output.decode('UTF-8').split('\n')
        print(lines)
        self.assertTrue(len(lines) > 1 and len(lines) < 7)

    #def test_returns_adding_config(self):
    #    output = popen(['kubel', 'cluster', 'login', '--dry-run'], stdout=PIPE).communicate()[0]
    #    self.assertTrue('gcloud init' in output.decode('UTF-8'))
