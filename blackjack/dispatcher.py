class Dispatcher:
    """イベントを管理する."""

    def __init__(self):
        self._handlers = {}

    def on(self, topic, handler):
        self._handlers.setdefault(topic, []).append(handler)
    
    def off(self, topic, handler):
        self._handlers.setdefault(topic, [handler]).remove(handler)
    
    def dispatch(self, topic, **keywords):
        for handler in self._handlers.setdefault(topic, []):
            handler(**keywords)


dispatcher = Dispatcher()