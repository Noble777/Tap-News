import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = 'amqp://suwtqtns:07i7ffur7LXu9NEAsn-erWjt44gl-NPa@barnacle.rmq.cloudamqp.com/suwtqtns'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'tap-news-SCRAPE_NEWS_TASK_QUEUE'

DEDUPE_NEWS_TASK_QUEUE_URL = 'amqp://kdgbnqyr:AnQaSwmgMxzJvrpXpcVPaz-Jmc6XQNmY@barnacle.rmq.cloudamqp.com/kdgbnqyr'
DEDUPE_NEWS_TASK_QUEUE_NAME = 'tap-news-dedupe-news-task-queue'

def clearQueue(queue_url, queue_name):
    queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if queue_client is not None:
            msg = queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
