"""The base command."""

import os
from shutil import copyfile
from .apps import jupyter
import ruamel.yaml
import subprocess
from shutil import copyfile
from .apps.jupyter import *

class Base(object):
    """A base command."""
    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.base_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.launch_dir=self.base_dir+'/data/launch_files'
        self.notebooks_dir=self.base_dir+'/data/notebooks'
        self.cwd=os.getcwd()
        self.launch_file = self.cwd+'/launch.yaml'
        self.launch_config = {}
        self.cluster_commands = {}
        self.app_commands = {}

    def append_launch_file(self, app):
        app_config=self.launch_dir+'/apps/'+app+'.yaml'
        if os.path.isfile(app_config):
            print('Adding configuration for '+app+' to launch.yaml.')
            config=self.load_yaml(app_config)
            ruamel.yaml.round_trip_dump(config, open(self.launch_file, 'a'))
            self.launch_config=self.load_yaml(self.launch_file)
            if app=='jupyter':
                jupyter_init(self)
        else:
            print('The configuration for the application ', app, 'is not available.' )
        copyfile(self.notebooks_dir+'/apps/'+app+'.ipynb', self.cwd+'/'+app+'.ipynb')

    def bash_command(self, command, syntax):
        if self.options['--dry-run']:
            print("Printing (not running) "+command+":\n", syntax)
        else:
            try:
                print("Executing "+command+":\n", syntax)
                result=subprocess.check_output(syntax, stderr=subprocess.STDOUT, shell=True)
                result=result.decode("utf-8")
                return result
            except subprocess.CalledProcessError as e:
                return(e.output.decode("utf-8"))

    def bash_command2(self, command, syntax):
        print("Executing "+command+":\n", syntax)
        popen = subprocess.Popen(syntax, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
        return

    def check_launch_file(self, key=None):
        if os.path.exists(self.launch_file):
            self.launch_config=self.load_yaml(self.launch_file)
            if key !=None and key not in self.launch_config:
                print('That application is not in the launch.yaml file.')
                quit()
        else:
            print("The launch.yaml file is not present in curently directory.  Run 'kubel init' to create it. ")
            quit()

    def check_overwrite_launch_file(self):
        if os.path.isfile(self.launch_file) and not self.options['--force']:
            print('The launch.yaml file already exists in the current directory. Add the --force flag to overwrite.' )
            quit()
        else:
            return True

    def load_yaml(self, file):
        with open(file, 'r') as yaml:
            kwargs=ruamel.yaml.round_trip_load(yaml, preserve_quotes=True)
        return kwargs

    def message(self, app):
        print('Adding configuration for '+app+' to launch.yaml.')

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
