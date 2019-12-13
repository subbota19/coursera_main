from datetime import datetime
from operator import itemgetter, attrgetter, methodcaller
from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    print("Hello")
    u1 = User(first_name="u1", last_name="u1")
    u2 = User(first_name="u2", last_name="u2")
    u3 = User(first_name="u3", last_name="u3")
    [x.save() for x in [u1, u2, u3]]

    b1 = Blog(title="blog1", author=u1)
    b2 = Blog(title="blog2", author=u2)
    [x.save() for x in [b1, b2]]

    b1.subscribers.add(u1, u2)
    b2.subscribers.add(u2)

    t1 = Topic(title="topic", author=u1, blog=b1)
    t2 = Topic(title="topic2_content", blog=b1, author=u3, created="2017-01-01 00:00:00")
    [x.save() for x in [t1, t2]]

    t1.likes.add(u1, u2, u3)


def edit_all():
    return User.objects.all().update(first_name="uu1")


def edit_u1_u2():
    return User.objects.all().filter(Q(first_name="u1") | Q(first_name="u2")).update(first_name="u1")


def delete_u1():
    return User.objects.all().delete(first_name="u1")


def unsubscribe_u2_from_blog():
    # lazy QueryList)))
    return [y.subscribers.remove(x) for y in Blog.objects.all() for x in y.subscribers.all() if x.first_name == "u2"]


def get_topic_created_grated():
    return Topic.objects.all().filter(created__year__gt=2018)


def get_topic_title_ended():
    return Topic.objects.all().filter(Q(title__endswith="content"))


def get_user_with_limit():
    return User.objects.all().order_by('id').reverse()[:2]


def get_topic_count():
    return Blog.objects.all().annotate(total=Count("topic__blog")).order_by("total")


def get_avg_topic_count():
    # for this func model should contain additional field in topic for total count(blog)
    return Blog.objects.annotate(total=Count("topic"))


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.annotate(Count("topic")).filter(topic__count__gt=1)


def get_topic_by_u1():
    return User.objects.all().filter(topic__author__first_name="u1")


def get_user_that_dont_have_blog():
    return User.objects.all().filter(blog__author__first_name=None).order_by("id")


def get_topic_that_like_all_users():
    return User.objects.all().annotate(total=Count("topic__likes")).filter(total=len(User.objects.all()))


def get_topic_that_dont_have_like():
    return Topic.objects.all().annotate(total=Count("likes")).filter(total=0)
