# encoding: utf-8
#
# Notification Model

from mini import Document
from datetime import datetime

# Handle :
#   Event information


class EventNotification(Document):
    event_id = str
    detail = str


# Handle :
#   App / Invitaion in groups
#   Add Friend
class FriendNotification(Document):
    detail = str
    foo_uid = str  # from foo
    bar_uid = str  # to bar
