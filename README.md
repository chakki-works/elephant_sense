# elephant-sense

content itself quality evaluation by machine learning

# Setup

Get [Qiita API token](https://qiita.com/api/v2/docs#認証認可) and set it to environment variable.

```
$ export QiitaToken=xxx
```

(only `read_qiita` scope is required)

## Data Preparation

* Locate the Qiita posts on `data/raw/items`
  * You can get Qiita posts by [Qiita API](https://qiita.com/api/v2/docs)
  * 1 post is 1 json file whose name is post `id` (like `0a0000aa0a0000a00aa0.json`).
* Locate the annotated file `labeled_qiita_posts.csv` on `data/raw`.
  * It's format is `No`,`url`,`Title`, and `annotator1`, `annotator2`... (column names are as you like ).

## Data Preprocessing

Run the following script.

```
python scripts/data/make_data.py
```

Then, labeled json file is stored at `data/processed/items`.

Next, execute preprocessing.

```
python scripts/data/preprocessing.py
```

`posts.json` will be created at `data/processed/`.  
`posts.json` includes splited tokens of each posts. You can use this to get the words in the posts.

