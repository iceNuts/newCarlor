# encoding: utf-8
#
# SpecialEvent Model

from mini import Document
from datetime import datetime
from bson import ObjectId

class SpecialEvent(Document):
    name        = str
    description = str
    location    = dict      #   contain long / short location
    start_time  = long
    end_time    = long
    photo_id    = str
    capacity    = int
    additionals = dict      #   like discount 
    members     = list      #   uids

    @gen.coroutine
    @staticmethod
    def get_future_event_with(handler, timestamp, limit):
        event_list = []
        cursor = handler.db.SpecialEvent.find({
            'start_time' : {'$gt' : timestamp}
            }).limit(limit)
        while(yield cursor.fetch_next):
            a = cursor.next_object()
            _id = a['_id']
            joined = a['members']

            # Get Status Info

            comment_count = yield handler.db.Review.find({
                'event_id' : str(_id)
                }).count()
            likes_count = yield handler.db.Like.find({'$and': [
                {'liked_id' : str(_id)},
                {'event_type' : 'special'}
                ]}).count()

            # Get Joind Info

            joined_count = len(joined)
            joined_sample_uids = members[:min(5, joined_count)]

            for i in xrange(len(joined_sample_uids)):
                joined_sample_uids[i] = ObjectId(joined_sample_uids[i])

            u_cursor = handler.db.User.find({
                '_id' : {'$in' : joined_sample_uids}
                })

            joined_sample = []
            while(yield u_cursor.fetch_next):
                u = u_cursor.next_object()
                joined_sample.append(
                        {
                            'first_name' : u['first_name'], 
                            'last_name'  : u['last_name']
                        }
                    )

            event_list.append(
                    {
                        'name'          : a['name'],
                        'description'   : a['description'],
                        'location'      : a['location'],
                        'start_time'    : a['start_time'],
                        'end_time'      : a['end_time'],
                        'photo_id'      : a['photo_id'],
                        'capacity'      : a['capacity'],
                        'additionals'   : a['additionals'],
                        'comment_count' : comment_count,
                        'likes_count'   : likes_count,
                        'joined_count'  : joined_count,
                        'joined_sample' : joined_sample
                    }
                )

        return event_list
                

        





