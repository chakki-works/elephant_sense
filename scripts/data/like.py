# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/processed')


if __name__ == '__main__':
    items = {'data': [], 'labels': [], 'files': []}
    dir_name = os.path.join(DATA_DIR, 'items')
    for file_name in os.listdir(dir_name):
        if not file_name.endswith('.json'):
            continue
        with open(os.path.join(dir_name, file_name)) as f:
            item = json.load(f)
            items['data'].append(int(item['likes']))
            items['labels'].append(item['annotations'])
            items['files'].append(file_name)

    with open(os.path.join(DATA_DIR, 'likes.json'), 'w') as f:
        json.dump(items, f)
