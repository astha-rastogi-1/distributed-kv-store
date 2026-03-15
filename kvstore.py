"""
In-memory key-value store used as Raft state machine
"""

class KeyValueStore:

    def __init__(self):
        self._store = {}
    
    def put(self, key, value):
        # ensure sommand is not none
        assert value is not None
        self._store[key] = value
    
    def delete(self, key):
        self._store.pop(key, None)
    
    def get(self, key:str):
        return self._store.get(key)
