import click_log_processor
import os
import sys
import json

from datetime import datetime
from sets import Set

with open(os.path.join(os.path.dirname(__file__), '..', 'config.json')) as config_file:    
    config = json.load(config_file)

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

PREFERENCE_MODEL_TABLE_NAME = config["recommendation_service"]["preference_model_table"]
NEWS_TABLE_NAME = config["mongodb"]["news_table"]

NUM_OF_CLASSES = 17

# Start MongoDB before running following tests.
def test_basic():
    db = mongodb_client.get_db()
    db[PREFERENCE_MODEL_TABLE_NAME].delete_many({"userId": "test_user"})

    msg = {"userId": "test_user",
           "newsId": "test_news",
           "timestamp": str(datetime.utcnow())}

    click_log_processor.handle_message(msg)

    model = db[PREFERENCE_MODEL_TABLE_NAME].find_one({'userId':'test_user'})
    assert model is not None
    assert len(model['preference']) == NUM_OF_CLASSES

    print 'test_basic passed!'


if __name__ == "__main__":
    test_basic()
