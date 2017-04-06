# -*- coding: utf-8 -*-
import json
import os
import re

from scripts.data.tokenizer import MeCabTokenizer
from scripts.data.normalization import normalize_unicode, normalize_number
from scripts.data.cleaning import clean_code, clean_html_tags
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/processed')


def cleaning(text):
    replaced_text = text.lower()
    replaced_text = clean_code(html_text=replaced_text)  # remove source code
    replaced_text = clean_html_tags(html_text=replaced_text)  # remove html tag
    replaced_text = re.sub(r'\$.*?\$+', '', replaced_text)  # remove math equation
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # remove @mention
    replaced_text = re.sub(r'https?:\/\/.*?([\r\n ]|$)', '', replaced_text)  # remove URL
    replaced_text = re.sub(r'　', '', replaced_text)  # remove zenkaku space
    return replaced_text


def normalization(text):
    normalized_text = normalize_unicode(text)
    normalized_text = normalize_number(normalized_text)
    return normalized_text


def process(text):
    tokenizer = MeCabTokenizer('/usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    text = cleaning(text)
    text = normalization(text)
    words = tokenizer.wakati_baseform(text)
    return words


if __name__ == '__main__':
    items = {'data': [], 'labels': [], 'files': []}
    dir_name = os.path.join(DATA_DIR, 'items')
    for file_name in os.listdir(dir_name):
        if not file_name.endswith('.json'):
            continue
        with open(os.path.join(dir_name, file_name)) as f:
            item = json.load(f)
            items['data'].append(item['rendered_body'])
            items['labels'].append(item['annotations'])
            items['files'].append(file_name)

    data = [process(text) for text in items['data']]
    items['data'] = data

    with open(os.path.join(DATA_DIR, 'posts.json'), 'w') as f:
        json.dump(items, f)
