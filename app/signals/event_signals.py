from typing import Callable, Dict, List
import asyncio

class Signal:
    def __init__(self):
        self._receivers: List[Callable] = []
        
    def connect(self, func: callable):
        self._receivers.append(func)
        
    async def send(self, **kwargs):
        for receiver in self._receivers:
            if asyncio.iscoroutinefunction(receiver):
                await receiver(**kwargs)    
            else:
                receiver(**kwargs)
                
user_created = Signal()
user_updated = Signal()
user_deleted = Signal()                    