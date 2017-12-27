"""
kubel

Usage:
  kubel -h | --help
  kubel -v | --version
  kubel init (azure|gcp) [--jupyter][--airflow][--force]
  kubel add_config <app>
  kubel hello <command> [--dry-run]
  kubel app <app> <command> [--dry-run]
  kubel cluster <command> [--dry-run]

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -f --force                        Force.
  --jupyter                         Set config to include jupyter.
  --echo                            Only print the comand, don't execute.

Examples:
  kubel cluster new

Help:
  For help using this tool, please see the Github repository:
  https://github.com/kubelaunch/kubelaunch-cli
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION
from os.path import abspath, dirname, join, isfile
import os

def main():
    """Main CLI entrypoint."""
    import kubelaunch.commands as kc
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
          if hasattr(kc, k) and v:
            module = getattr(kc, k)
            kc = getmembers(module, isclass)
            command = [command[1] for command in kc if command[0] != 'Base'][0]
            command = command(options)
            command.run()
