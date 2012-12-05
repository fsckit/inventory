from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

class SubscribeNamespace(BaseNamespace, BroadcastMixin):
  def on_transaction(self):
    self.broadcast_event_not_me('update')
