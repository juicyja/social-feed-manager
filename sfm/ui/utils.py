import os.path
import time

#from django.core.management import call_command
#from django.db.models.signals import post_save
#from django.dispatch import receiver

#from ui.models import TwitterFilter

# A little added cushion
WAIT_BUFFER_SECONDS = 2


def set_wait_time(last_response):
    """based on last tweepy api response, calculate a time buffer in
    seconds to wait before issuing next api call."""
    wait_time = 0
    try:
        remaining = int(last_response.getheader('x-rate-limit-remaining'))
        reset = int(last_response.getheader('x-rate-limit-reset'))
        reset_seconds = reset - int(time.time())
    except:
        remaining = reset_seconds = 1
    # the out-of-calls-for-this-window case
    if remaining == 0:
        return reset_seconds + WAIT_BUFFER_SECONDS
    else:
        wait_time = (reset_seconds / remaining) + WAIT_BUFFER_SECONDS
    # #22: saw some negative ratelimit-reset/wait_times
    # so cushion around that too
    while wait_time < WAIT_BUFFER_SECONDS:
        wait_time += WAIT_BUFFER_SECONDS
    return wait_time


def delete_conf_file(tfilterid):
    filename = "sfm-twitter-rule#%s-filter.conf" % tfilterid
    file_path = "<PATH TO SUPERVISOR CONF FILES>/%s" % filename
    if os.path.exists(file_path):
        os.remove(file_path)
