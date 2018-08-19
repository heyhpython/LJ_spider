#!/usr/bin/env bash

pyenv active spider
scrapy crawl lj
python LJ/data_cleaner.py

