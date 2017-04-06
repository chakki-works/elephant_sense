import csv
import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '../../data/')


def list_labels():
    labeled_file = os.path.join(BASE_DIR, 'raw/labeled_qiita_posts.csv')
    with open(labeled_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # Skip header
        for row in reader:
            url = row[1]
            labels = row[3:]
            item_id = url.split('/')[-1]
            yield item_id, labels


def add_annotations():
    for item_id, labels in list_labels():
        item_file = os.path.join(BASE_DIR, 'raw/items/{}.json'.format(item_id))
        save_file = os.path.join(BASE_DIR, 'processed/items/{}.json'.format(item_id))
        with open(item_file, 'r') as rf, open(save_file, 'w') as wf:
            item = json.load(rf)
            item['annotations'] = [
                {
                    "annotator-id": annotator_id,
                    'quality': quality
                }
                for annotator_id, quality in enumerate(labels)
                ]
            wf.write(json.dumps(item, indent=4, ensure_ascii=False))


def main():
    add_annotations()


if __name__ == '__main__':
    main()