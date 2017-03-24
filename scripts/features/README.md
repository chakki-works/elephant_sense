# Feature Framework

The post is read in `Post` class by `Reader`.  
Then, we want to add the features to the `Post`. For that reason, `PostFeature` is prepared.  

Only you have to do to add the feature is implements feature extractor by inheriting the `FeatureExtractor`.

For example, following is the class to get title length feature.

```py
from scripts.features.feature_extractor import FeatureExtractor


class TitleLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        return len(post.title)

```

You can test `extract` method independently.

Then, add this feature to `PostFeature`. The code is like below.  
(You can see it in the [notebook](https://github.com/chakki-works/elephant_sense/blob/master/notebooks/feature_test.ipynb))

```py
reader = Reader()
pf_dicts = []
for p in reader.post_iterator():  # read posts from data directory and iterate it.
    pf = PostFeature(p)  # create post feature
    pf.add(TitleLengthExtractor())  # add your feature class instance. extract method will be executed.
    pf.add(SectionCountExtractor())
    pf_d = pf.to_dict()
    pf_dicts.append(pf_d)
    
pf_df = pd.DataFrame(pf_dicts)  # convert to the pandas dafatrame
```

You can use preprocessed feature by "extracted" argument.  
In the above, `SectionCountExtractor` can use `extracted["title_length"]`.

Enjoy!
