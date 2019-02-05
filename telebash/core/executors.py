import subprocess


class DummyExecutor:
    _executor = subprocess
    results = ''

    @classmethod
    def execute(cls, cmd):
        cls.results = cls._executor.run([cmd['cmd'], cmd['args']], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return cls.results
