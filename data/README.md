# Annotation Policy

## Sentence Role

We annotated the role of sentence by xml class like following.

```
<s role="o">In this document, I describe how to do the annotation.</s>
<s role="b">Because the annotation is the most important work in the machine learning.</s>
<s role="a">First I show the annotation ways, Second I tell the important points when doing the annotation.</s>
<s role="t">It will be useful for you if you want to make your own dataset.</s>
```

```
<s role="b">Sometimes you want to correct the commit log in the git repository.</s>
<s role="s">You can do it by below command.</s>
```

The kinds of roles is below.

* `o`: objective. It shows the objective of the document.
* `b`: background. It describes why this article is written.
* `a`: approach. It shows the overview (step of explanation) of the document.
* `t`: target. It tells who have to read this article.
* `s`: solution. It tells that the knowledge that writer discovered.

