# -*- coding: utf-8 -*-
import sys
import os
import yaml

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import news_api_client as client


with open(os.path.join(os.path.dirname(__file__), '../..', "config.yaml"), 'r') as config_file:
    config = yaml.load(config_file)

def test_basic():
    sources = [source.encode('ascii') for source in config["newsApi"]["sources"]]
    print sources
    news = client.getNewsFromSource()
    print news
    assert len(news) > 0
    news = client.getNewsFromSource(sources=sources)
    assert len(news) > 0
    print 'test_basic passed!'

if __name__ == "__main__" :
    test_basic()
