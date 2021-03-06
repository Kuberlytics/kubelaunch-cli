"""The init command initializes a configuration file in
   the users home directory."""

from .base import Base
import ruamel.yaml
import os.path
from shutil import copyfile


class Init(Base):
    """Initialize!"""
    def run(self):
        """"Run will copy a file from launch_files """
        self.check_overwrite_launch_file()
        if self.options['gcp']:
            cluster_location='gcp'
        elif self.options['azure']:
            cluster_location='azure'
        self.message(cluster_location)
        config=self.load_yaml(self.launch_dir+'/clusters/'+cluster_location+'.yaml')

        #Create the launch_file in the user directory
        ruamel.yaml.round_trip_dump(config, open(self.launch_file, 'w'))
        copyfile(self.notebooks_dir+'/clusters/'+cluster_location+'.ipynb', self.cwd+'/'+cluster_location+'.ipynb')
        copyfile(self.base_dir+'/data/readme.md', self.cwd+'/readme.md')

        if self.options['--jupyter']:
            print("Appending Jupyter")
            self.append_launch_file('jupyter')
            
