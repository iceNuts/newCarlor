# encoding: utf-8
#
# ChatGroup Model

from mini import Document

class ChatGroup(Document):
    event_id        = str   #   associated event id (PUBLIC) / or nil as private
    in_party        = bool  #   True means special event 
    host_user_id    = str   #   host user id
    members         = list  #   user id list
    name            = str
    capacity        = int   #   default as 10 (UPGRADEABLE)
    photo_id        = str   #   ChatGroup description photo
    description     = str
