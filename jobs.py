######################## jobs.Py ########################
## @Author Timo Bauer                                  ##
## @created 22.01.2021                                 ##
## Job Handling; schedule jobs                         ##
#########################################################

from config import twitter_api_keys, config
from datetime import datetime
import os
import gpiozero
import twitter
import time
import threading

def __getStatusMessage__():
    """
    concatenates multiple System informations and returns them as a string.
    WARNING: cpu-temperature works on raspberry pis only and os.getloadavg does not work on Windows
    ---
    RETURNS: string
    """
    message = "time: "
    message += str(datetime.now().time())
    message += " |CPU-Temp: "
    message += str(gpiozero.CPUTemperature().temperature)
    message += " |Load: "
    message += str(os.getloadavg())

    return message

def postStatusTweet():
    """
    posts a status tweet.
    ---
    RETURNS: True if the tweet was successfully sent, False if something went wrong.
    """
    api = twitter.Api(consumer_key=twitter_api_keys.CONSUMER_KEY, consumer_secret=twitter_api_keys.CONSUMER_SECRET, access_token_key=twitter_api_keys.API_KEY, access_token_secret=twitter_api_keys.API_SECRET)

    try:
        message = __getStatusMessage__()
        api.PostUpdate(message)
        return True
    except:
        return False
    finally:
        api = None
def __startJob__(interval, func, iterations = 0):
    """
    Starts the loop running the job frequently.
    see https://stackoverflow.com/a/11488902
    ---
    interval: int
        How often should the job be executed (in seconds)
    func: function
        The job-function
    iterations: int
        default: 0 (forever)
        How many times should the job be executed
    """
    if(iterations != 1):
        threading.Timer(interval, __startJob__, [interval, func, 0 if iterations == 0 else iterations-1]).start()

        func()

def register():
    """
    schedule the job
    """
    __startJob__(config.STATUS_UPDATE_TIME, postStatusTweet)
