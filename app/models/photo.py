# encoding: utf-8
#
# Photo Model

from mini import Document


class Photo(Document):
    object_id = str  # associated object id
    s3_link = str  # photo link
