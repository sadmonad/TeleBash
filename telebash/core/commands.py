class DummyBashCommand:
    def __init__(self, bash_cmd):
        self.cmd = bash_cmd['cmd']
        self.args = bash_cmd['args']
        self.use_sudo = bash_cmd['use_sudo']


class DummyCommand:
    def __init__(self, cmd):
        self.description = cmd['description']
        self.bash_cmd = DummyBashCommand(cmd['bash_cmd'])
