import subprocess


class DummyExecutor:
    _executor = subprocess
    results = ''

    @classmethod
    def execute(cls, cmd):
        args = cls.process_args(cmd.args)
        cls.results = cls._executor.run([cmd.cmd, args], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return cls.results

    @classmethod
    def process_args(cls, args):
        return ' '.join(args)
