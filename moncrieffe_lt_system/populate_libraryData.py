import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moncrieffe_lt_system.settings')

import django
django.setup()
from moncrieffeLTS.models import Media, User, Topic


def populate():

    topics =[
        {"topic": "Sports"},
        {"topic": "Parenting"},
        {"topic": "Childres"},
        {"topic": "Education"}
    ]

    media =[
        {"type": "Book", "title": "The Blind side",
        "isbn": 9780739340530, "author": "Micheal L. Lewis",
        "image": "sportsBook.jpg"
        },
        {"type": "Book", "title": "The Baby Book",
        "isbn": 9780004174426, "author": "William Sears",
        "image": "babyBook.jpg"
        },
        {"type": "Book", "title": "Where Does Maisy Live?",
        "isbn": 9780744575330, "author": "Lucy Cousins",
        "image": "babyBook.jpg"
        },
        {"type": "Book", "title": "Discrete mathematical structures",
        "isbn": 9780132297516, "author": "Bernard Kolman",
        "image": "educationBook.jpg"
        },

    ]

    users = [
        {"user_id": "dahliamoncrieffe", "first_name": "Dahlia", "last_name": "Moncrieffe"},
         {"user_id": "sagenasiah", "first_name": "Nasiah", "last_name": "Peterson"}
    ]
    for topic in topics:
        def add_topic(topic):
            t = Topic.objects.get_or_create(topic=topic)[0]
            t.save()
            return t
        add_topic(topic["topic"])

    for mediaItems in media:
        def add_media(media_type, title, isbn, author):
            m = Media.objects.get_or_create(media_type=media_type,title=title, isbn=isbn,author=author)[0]
            #m.topic = Topic.objects.get(topic=topic)
            m.save()
            return m
        add_media(mediaItems["type"], mediaItems["title"], mediaItems["isbn"], mediaItems["author"])

    for user in users:
        def add_user(user_id, first_name, last_name):
            u = User.objects.get_or_create(user_id=user_id, first_name=first_name, last_name=last_name)[0]
            u.save()
            return u
        add_user(user["user_id"], user["first_name"], user["last_name"])
# Start execution here!
if __name__ == '__main__':
    print(" Starting moncrieffeLTS population script...")
    populate()

