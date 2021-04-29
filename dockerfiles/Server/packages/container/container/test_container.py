import os
import subprocess
from decorators import Singleton
from subprocess import Popen, PIPE, STDOUT

@Singleton
class TestContainer:

    def __init__(self):
        self.name = ""
        self.id = ""
        self.test_o_name = ""
        self.timeout= 5

    def start(self):
        result = subprocess.run(['docker','run', '-it', '-d', self.name], stdout=subprocess.PIPE)
        self.id = str(result.stdout[:12], 'utf-8')

    def remove(self):
        subprocess.check_call(['docker', 'container', 'stop', self.id])
        subprocess.check_call(['docker', 'container', 'rm', self.id])
        self.id = ""

    def copy_to(self, folder, dst):
        subprocess.check_call(['docker', 'cp', folder, f'{self.id}:/home/tests/{dst}'])

    def copy_from(self, file, to):
        return subprocess.run(['docker', 'cp', self.id + ':/home/tests/' + file ,to], stdout=subprocess.PIPE)
    
    def _extend_exec_(self, cmd):
        base = ['docker', 'exec', self.id]
        base.extend(cmd)
        return base
    
    def subprocess_cmd(self,cmd):
        subprocess.run(self._extend_exec_(cmd))
    
    def subprocess_check_cmd(self,cmd):
        return subprocess.check_output(self._extend_exec_(cmd), stderr=subprocess.PIPE)


    def subprocess_call_cmd(self,cmd):
        return subprocess.call(self._extend_exec_(cmd), timeout=self.timeout)

    def os_cmd(self,cmd):
        return os.system(f'docker exec {self.id} {cmd}')
