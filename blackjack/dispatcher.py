class Dispatcher:
    def __init__(self):
        self._handlers = {}

    def on(self, topic, handler):
        self._handlers.setdefault(topic, []).append(handler)
    
    def off(self, topic, handler):
        self._handlers.setdefault(topic, [handler]).remove(handler)
    
    def dispatch(self, **keywords):
        for handler in self._handlers:
            handler(**keywords)
