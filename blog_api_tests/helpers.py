import re


def validate_emails(comments):
    for comment in comments:
        assert re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
                        comment['email']), 'email {} is not valid for post {} comment {}'.format(comment['email'],
                                                                                                 comment['postId'],
                                                                                                 comment['id'])
