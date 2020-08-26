class Person:
    def __init__(self, addr, name, client):
        self.addr = addr
        self.name = name
        self.client = client
        self.name = None
        def set_name(self, name):
            self.name = name

        def __repr__(self):
            return f"Person({self.addr}, {self.name})"

