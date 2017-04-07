# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
import json
import unittest
from scripts.features.post import Post
from scripts.features.post_feature import PostFeature
import scripts.features.html_feature_extractor as hExt


class TestHtmlFeature(unittest.TestCase):

    def test_html_feature(self):
        post_json = json.loads(TEST_JSON)
        post = Post(post_json)
        post_f = PostFeature(post)
        fd = post_f \
        .add(hExt.HeaderCountExtractor()) \
        .to_dict()

        self.checkAttribute("header_count", fd)
    
    def checkAttribute(self, name, features):
        self.assertTrue(name in features)
        print(features[name])

TEST_JSON = r"""
{
    "created_at": "2016-09-23T13:27:44+09:00",
    "annotations":[
        {
            "annotator-id": "A",
            "quality": 0
        },
        {
            "annotator-id": "B",
            "quality": 0
        },
        {
            "annotator-id": "C",
            "quality": 1
        }
    ],
    "user": {
        "profile_image_url": "https://qiita-image-store.s3.amazonaws.com/0/62264/profile-images/1473695899",
        "permanent_id": 62264,
        "github_login_name": null,
        "followers_count": 24,
        "twitter_screen_name": "htht_",
        "id": "hththt",
        "followees_count": 36,
        "organization": "",
        "location": "東京",
        "website_url": "",
        "facebook_id": "",
        "items_count": 75,
        "description": "",
        "name": "hththt",
        "linkedin_id": ""
    },
    "id": "0a0d29de9a2785d00ca0",
    "rendered_body": "\n<h1>\n<span id=\"gulpspritesmith\" class=\"fragment\"></span><a href=\"#gulpspritesmith\"><i class=\"fa fa-link\"></i></a>gulp.spritesmith</h1>\n\n<ul>\n<li>CSS Spriteとそれに対応した scssファイルを生成する。</li>\n</ul>\n\n<p><a href=\"https://github.com/twolfson/gulp.spritesmith\" class=\"autolink\" rel=\"nofollow noopener\" target=\"_blank\">https://github.com/twolfson/gulp.spritesmith</a></p>\n\n<h3>\n<span id=\"サンプル表示\" class=\"fragment\"></span><a href=\"#%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E8%A1%A8%E7%A4%BA\"><i class=\"fa fa-link\"></i></a>サンプル表示</h3>\n\n<p><a href=\"https://qiita-image-store.s3.amazonaws.com/0/62264/e88862bc-2486-b3cd-e4d0-e26385816b6f.png\" target=\"_blank\" rel=\"nofollow noopener\"><img src=\"https://qiita-image-store.s3.amazonaws.com/0/62264/e88862bc-2486-b3cd-e4d0-e26385816b6f.png\" alt=\"スクリーンショット 2016-09-23 15.54.30.png\"></a></p>\n\n<h1>\n<span id=\"手順\" class=\"fragment\"></span><a href=\"#%E6%89%8B%E9%A0%86\"><i class=\"fa fa-link\"></i></a>手順</h1>\n\n<h3>\n<span id=\"パッケージをインストール\" class=\"fragment\"></span><a href=\"#%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB\"><i class=\"fa fa-link\"></i></a>パッケージをインストール</h3>\n\n<div class=\"code-frame\" data-lang=\"text\"><div class=\"highlight\"><pre>\n$ npm install\n</pre></div></div>\n\n<h3>\n<span id=\"sprite画像の生成\" class=\"fragment\"></span><a href=\"#sprite%E7%94%BB%E5%83%8F%E3%81%AE%E7%94%9F%E6%88%90\"><i class=\"fa fa-link\"></i></a>sprite画像の生成</h3>\n\n<ul>\n<li>spriteにしたい画像をimagesの中に入れる</li>\n</ul>\n\n<div class=\"code-frame\" data-lang=\"text\"><div class=\"highlight\"><pre>\n$ gulp sprite\n</pre></div></div>\n\n<ul>\n<li>sprite.pngが生成される</li>\n<li>_sprite.scssが生成される</li>\n</ul>\n\n<p><a href=\"https://qiita-image-store.s3.amazonaws.com/0/62264/50c96bff-9e35-43a9-19df-7f5916a0ed6e.png\" target=\"_blank\" rel=\"nofollow noopener\"><img src=\"https://qiita-image-store.s3.amazonaws.com/0/62264/50c96bff-9e35-43a9-19df-7f5916a0ed6e.png\" alt=\"スクリーンショット 2016-09-23 15.56.00.png\"></a></p>\n\n<h3>\n<span id=\"gulpの実行\" class=\"fragment\"></span><a href=\"#gulp%E3%81%AE%E5%AE%9F%E8%A1%8C\"><i class=\"fa fa-link\"></i></a>gulpの実行</h3>\n\n<div class=\"code-frame\" data-lang=\"text\"><div class=\"highlight\"><pre>\n$ gulp\n</pre></div></div>\n\n<h3>\n<span id=\"stylesassを編集保存\" class=\"fragment\"></span><a href=\"#stylesass%E3%82%92%E7%B7%A8%E9%9B%86%E4%BF%9D%E5%AD%98\"><i class=\"fa fa-link\"></i></a>style.sassを編集・保存</h3>\n\n<div class=\"code-frame\" data-lang=\"sass\">\n<div class=\"code-lang\"><span class=\"bold\">style.sass</span></div>\n<div class=\"highlight\"><pre>\n<span class=\"c1\">//生成されたspriteを読み込む指定</span>\n<span class=\"k\">@import</span> <span class=\"s\">\"sprite\";</span>\n\n<span class=\"c1\">//使いたい画像を読み込む指定(ここでは、引数に、「$sprite-」+画像のファイル名を書く)</span>\n\n<span class=\"nc\">.</span><span class=\"err\">使いたいクラス名{</span>\n  <span class=\"k\">@include</span><span class=\"nd\"> sprite</span><span class=\"p\">(</span><span class=\"nv\">$sprite-cat</span><span class=\"p\">)</span><span class=\"err\">;</span>\n<span class=\"err\">}</span>\n</pre></div>\n</div>\n\n<ul>\n<li>style.css.mapが生成</li>\n<li>style.cssが生成</li>\n</ul>\n\n<p><a href=\"https://qiita-image-store.s3.amazonaws.com/0/62264/cc58f250-7ad2-92c8-1bcf-c38f5b9a4396.png\" target=\"_blank\" rel=\"nofollow noopener\"><img src=\"https://qiita-image-store.s3.amazonaws.com/0/62264/cc58f250-7ad2-92c8-1bcf-c38f5b9a4396.png\" alt=\"スクリーンショット 2016-09-23 16.01.01.png\"></a></p>\n\n<h3>\n<span id=\"gulpfileサンプル\" class=\"fragment\"></span><a href=\"#gulpfile%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB\"><i class=\"fa fa-link\"></i></a>gulpfileサンプル</h3>\n\n<div class=\"code-frame\" data-lang=\"javascript\">\n<div class=\"code-lang\"><span class=\"bold\">gulpfile.js</span></div>\n<div class=\"highlight\"><pre>\n\n<span class=\"kd\">var</span> <span class=\"nx\">gulp</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s1\">'gulp'</span><span class=\"p\">);</span>\n<span class=\"kd\">var</span> <span class=\"nx\">spritesmith</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s1\">'gulp.spritesmith'</span><span class=\"p\">);</span>\n<span class=\"kd\">var</span> <span class=\"nx\">sass</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s1\">'gulp-sass'</span><span class=\"p\">);</span>\n<span class=\"kd\">var</span> <span class=\"nx\">browser</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s2\">\"browser-sync\"</span><span class=\"p\">);</span>\n<span class=\"kd\">var</span> <span class=\"nx\">autoprefixer</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s1\">'gulp-autoprefixer'</span><span class=\"p\">);</span>\n<span class=\"kd\">var</span> <span class=\"nx\">sourcemaps</span> <span class=\"o\">=</span> <span class=\"nx\">require</span><span class=\"p\">(</span><span class=\"s1\">'gulp-sourcemaps'</span><span class=\"p\">);</span>\n\n<span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">task</span><span class=\"p\">(</span><span class=\"s1\">'default'</span><span class=\"p\">,[</span><span class=\"s1\">'server'</span><span class=\"p\">],</span><span class=\"kd\">function</span><span class=\"p\">()</span> <span class=\"p\">{</span>\n  <span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">watch</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/sass/*.scss'</span><span class=\"p\">,</span> <span class=\"p\">[</span><span class=\"s1\">'sass'</span><span class=\"p\">]);</span>\n<span class=\"p\">});</span>\n<span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">task</span><span class=\"p\">(</span><span class=\"s1\">'sass'</span><span class=\"p\">,</span><span class=\"kd\">function</span> <span class=\"p\">()</span> <span class=\"p\">{</span>\n    <span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">src</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/sass/*.scss'</span><span class=\"p\">)</span>\n     <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">sourcemaps</span><span class=\"p\">.</span><span class=\"nx\">init</span><span class=\"p\">())</span>\n        <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">sass</span><span class=\"p\">())</span>\n        <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">autoprefixer</span><span class=\"p\">(</span><span class=\"s2\">\"last 2 version\"</span><span class=\"p\">,</span> <span class=\"s2\">\"ie 8\"</span><span class=\"p\">,</span> <span class=\"s2\">\"ie 7\"</span><span class=\"p\">))</span>\n     <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">sourcemaps</span><span class=\"p\">.</span><span class=\"nx\">write</span><span class=\"p\">(</span><span class=\"s1\">'../maps'</span><span class=\"p\">))</span>\n     <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">dest</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/css/'</span><span class=\"p\">))</span>\n     <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">browser</span><span class=\"p\">.</span><span class=\"nx\">reload</span><span class=\"p\">({</span><span class=\"nx\">stream</span><span class=\"o\">:</span><span class=\"kc\">true</span><span class=\"p\">}));</span>\n<span class=\"p\">});</span>\n\n<span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">task</span><span class=\"p\">(</span><span class=\"s2\">\"server\"</span><span class=\"p\">,</span> <span class=\"kd\">function</span><span class=\"p\">()</span> <span class=\"p\">{</span>\n    <span class=\"nx\">browser</span><span class=\"p\">({</span>\n        <span class=\"nx\">server</span><span class=\"o\">:</span> <span class=\"p\">{</span>\n            <span class=\"nx\">baseDir</span><span class=\"o\">:</span> <span class=\"s2\">\"htdocs/\"</span>\n        <span class=\"p\">}</span>\n    <span class=\"p\">});</span>\n<span class=\"p\">});</span>\n\n<span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">task</span><span class=\"p\">(</span><span class=\"s1\">'sprite'</span><span class=\"p\">,</span> <span class=\"kd\">function</span> <span class=\"p\">()</span> <span class=\"p\">{</span>\n  <span class=\"kd\">var</span> <span class=\"nx\">spriteData</span> <span class=\"o\">=</span> <span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">src</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/images/*.png'</span><span class=\"p\">).</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">spritesmith</span><span class=\"p\">({</span>\n    <span class=\"nx\">imgName</span><span class=\"o\">:</span> <span class=\"s1\">'sprite.png'</span><span class=\"p\">,</span>\n    <span class=\"nx\">cssName</span><span class=\"o\">:</span> <span class=\"s1\">'_sprite.scss'</span><span class=\"p\">,</span>\n    <span class=\"nx\">imgPath</span><span class=\"o\">:</span> <span class=\"s1\">'../images/sprite/sprite.png'</span><span class=\"p\">,</span>\n    <span class=\"nx\">cssFormat</span><span class=\"o\">:</span> <span class=\"s1\">'scss'</span><span class=\"p\">,</span>\n    <span class=\"nx\">cssVarMap</span><span class=\"o\">:</span> <span class=\"kd\">function</span> <span class=\"p\">(</span><span class=\"nx\">sprite</span><span class=\"p\">)</span> <span class=\"p\">{</span>\n      <span class=\"nx\">sprite</span><span class=\"p\">.</span><span class=\"nx\">name</span> <span class=\"o\">=</span> <span class=\"s1\">'sprite-'</span> <span class=\"o\">+</span> <span class=\"nx\">sprite</span><span class=\"p\">.</span><span class=\"nx\">name</span><span class=\"p\">;</span>\n    <span class=\"p\">}</span>\n  <span class=\"p\">}));</span>\n  <span class=\"nx\">spriteData</span><span class=\"p\">.</span><span class=\"nx\">img</span>\n    <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">dest</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/images/sprite/'</span><span class=\"p\">));</span>\n  <span class=\"nx\">spriteData</span><span class=\"p\">.</span><span class=\"nx\">css</span>\n    <span class=\"p\">.</span><span class=\"nx\">pipe</span><span class=\"p\">(</span><span class=\"nx\">gulp</span><span class=\"p\">.</span><span class=\"nx\">dest</span><span class=\"p\">(</span><span class=\"s1\">'htdocs/sass/'</span><span class=\"p\">));</span>\n<span class=\"p\">});</span>\n</pre></div>\n</div>\n\n<div class=\"code-frame\" data-lang=\"scss\">\n<div class=\"code-lang\"><span class=\"bold\">style.scss</span></div>\n<div class=\"highlight\"><pre>\n\n<span class=\"k\">@import</span> <span class=\"s2\">\"sprite\"</span><span class=\"p\">;</span>\n\n<span class=\"nt\">body</span><span class=\"p\">{</span>\n  <span class=\"na\">padding</span><span class=\"o\">:</span><span class=\"mi\">50</span><span class=\"kt\">px</span> <span class=\"mi\">0</span> <span class=\"mi\">0</span> <span class=\"mi\">50</span><span class=\"kt\">px</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n<span class=\"nt\">div</span><span class=\"p\">{</span>\n  <span class=\"na\">margin-bottom</span><span class=\"o\">:</span><span class=\"mi\">20</span><span class=\"kt\">px</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n<span class=\"nt\">h1</span><span class=\"p\">{</span>\n  <span class=\"na\">font-size</span><span class=\"o\">:</span><span class=\"mi\">30</span><span class=\"kt\">px</span><span class=\"p\">;</span>\n  <span class=\"na\">margin</span><span class=\"o\">:</span><span class=\"mi\">0</span> <span class=\"mi\">0</span> <span class=\"mi\">50</span><span class=\"kt\">px</span> <span class=\"mi\">0</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n\n<span class=\"na\">.icon1</span><span class=\"o\">::</span><span class=\"n\">before</span><span class=\"p\">{</span>\n  <span class=\"k\">@include</span><span class=\"nd\"> sprite</span><span class=\"p\">(</span><span class=\"nv\">$sprite-icon1</span><span class=\"p\">);</span>\n    <span class=\"na\">content</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">;</span>\n    <span class=\"na\">margin</span><span class=\"o\">:</span><span class=\"mi\">-3</span><span class=\"kt\">px</span> <span class=\"mi\">10</span><span class=\"kt\">px</span> <span class=\"mi\">0</span> <span class=\"mi\">0</span><span class=\"p\">;</span>\n    <span class=\"na\">display</span><span class=\"o\">:</span> <span class=\"no\">inline</span><span class=\"o\">-</span><span class=\"no\">block</span><span class=\"p\">;</span>\n    <span class=\"na\">vertical-align</span><span class=\"o\">:</span> <span class=\"no\">middle</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n<span class=\"na\">.icon2</span><span class=\"o\">::</span><span class=\"n\">before</span><span class=\"p\">{</span>\n  <span class=\"k\">@include</span><span class=\"nd\"> sprite</span><span class=\"p\">(</span><span class=\"nv\">$sprite-icon2</span><span class=\"p\">);</span>\n    <span class=\"na\">content</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">;</span>\n    <span class=\"na\">margin</span><span class=\"o\">:</span><span class=\"mi\">-3</span><span class=\"kt\">px</span> <span class=\"mi\">10</span><span class=\"kt\">px</span> <span class=\"mi\">0</span> <span class=\"mi\">0</span><span class=\"p\">;</span>\n    <span class=\"na\">display</span><span class=\"o\">:</span> <span class=\"no\">inline</span><span class=\"o\">-</span><span class=\"no\">block</span><span class=\"p\">;</span>\n    <span class=\"na\">vertical-align</span><span class=\"o\">:</span> <span class=\"no\">middle</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n<span class=\"na\">.icon3</span><span class=\"o\">::</span><span class=\"n\">before</span><span class=\"p\">{</span>\n  <span class=\"k\">@include</span><span class=\"nd\"> sprite</span><span class=\"p\">(</span><span class=\"nv\">$sprite-icon3</span><span class=\"p\">);</span>\n    <span class=\"na\">content</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">;</span>\n    <span class=\"na\">margin</span><span class=\"o\">:</span><span class=\"mi\">-3</span><span class=\"kt\">px</span> <span class=\"mi\">10</span><span class=\"kt\">px</span> <span class=\"mi\">0</span> <span class=\"mi\">0</span><span class=\"p\">;</span>\n    <span class=\"na\">display</span><span class=\"o\">:</span> <span class=\"no\">inline</span><span class=\"o\">-</span><span class=\"no\">block</span><span class=\"p\">;</span>\n    <span class=\"na\">vertical-align</span><span class=\"o\">:</span> <span class=\"no\">middle</span><span class=\"p\">;</span>\n<span class=\"p\">}</span>\n<span class=\"nc\">.cat</span><span class=\"p\">{</span>\n  <span class=\"k\">@include</span><span class=\"nd\"> sprite</span><span class=\"p\">(</span><span class=\"nv\">$sprite-cat</span><span class=\"p\">);</span>\n<span class=\"p\">}</span>\n</pre></div>\n</div>\n\n<div class=\"code-frame\" data-lang=\"html\">\n<div class=\"code-lang\"><span class=\"bold\">index.html</span></div>\n<div class=\"highlight\"><pre>\n\n<span class=\"cp\">&lt;!DOCTYPE html&gt;</span>\n<span class=\"nt\">&lt;html</span> <span class=\"na\">lang=</span><span class=\"s\">\"ja\"</span><span class=\"nt\">&gt;</span>\n<span class=\"nt\">&lt;head&gt;</span>\n<span class=\"nt\">&lt;meta</span> <span class=\"na\">charset=</span><span class=\"s\">\"utf-8\"</span><span class=\"nt\">&gt;</span>\n<span class=\"nt\">&lt;title&gt;</span>gulp.spritesmithテスト<span class=\"nt\">&lt;/title&gt;</span>\n<span class=\"nt\">&lt;link</span> <span class=\"na\">rel=</span><span class=\"s\">\"stylesheet\"</span> <span class=\"na\">type=</span><span class=\"s\">\"text/css\"</span> <span class=\"na\">href=</span><span class=\"s\">\"http://yui.yahooapis.com/3.18.1/build/cssreset/cssreset-min.css\"</span><span class=\"nt\">&gt;</span>\n<span class=\"nt\">&lt;link</span> <span class=\"na\">rel=</span><span class=\"s\">\"stylesheet\"</span> <span class=\"na\">href=</span><span class=\"s\">\"css/style.css\"</span><span class=\"nt\">&gt;</span>\n<span class=\"nt\">&lt;/head&gt;</span>\n<span class=\"nt\">&lt;body&gt;</span>\n<span class=\"nt\">&lt;h1&gt;</span>gulp.spritesmithテスト<span class=\"nt\">&lt;/h1&gt;</span>\n\n<span class=\"nt\">&lt;div</span> <span class=\"na\">class=</span><span class=\"s\">\"icon1\"</span><span class=\"nt\">&gt;</span>アイコン1<span class=\"nt\">&lt;/div&gt;</span>\n<span class=\"nt\">&lt;div</span> <span class=\"na\">class=</span><span class=\"s\">\"icon2\"</span><span class=\"nt\">&gt;</span>アイコン2<span class=\"nt\">&lt;/div&gt;</span>\n<span class=\"nt\">&lt;div</span> <span class=\"na\">class=</span><span class=\"s\">\"icon3\"</span><span class=\"nt\">&gt;</span>アイコン3<span class=\"nt\">&lt;/div&gt;</span>\n<span class=\"nt\">&lt;div</span> <span class=\"na\">class=</span><span class=\"s\">\"cat\"</span><span class=\"nt\">&gt;&lt;/div&gt;</span>\n<span class=\"nt\">&lt;/body&gt;</span>\n<span class=\"nt\">&lt;/html&gt;</span>\n</pre></div>\n</div>\n",
    "updated_at": "2016-09-27T18:26:03+09:00",
    "tags": [
        {
            "name": "gulp",
            "versions": []
        }
    ],
    "private": false,
    "coediting": false,
    "url": "http://qiita.com/hththt/items/0a0d29de9a2785d00ca0",
    "group": null,
    "body": "#gulp.spritesmith\n- CSS Spriteとそれに対応した scssファイルを生成する。\n\nhttps://github.com/twolfson/gulp.spritesmith\n\n\n###サンプル表示\n\n![スクリーンショット 2016-09-23 15.54.30.png](https://qiita-image-store.s3.amazonaws.com/0/62264/e88862bc-2486-b3cd-e4d0-e26385816b6f.png)\n\n\n#手順\n\n###パッケージをインストール\n\n```\n$ npm install\n```\n\n###sprite画像の生成\n\n- spriteにしたい画像をimagesの中に入れる\n\n```\n$ gulp sprite\n```\n\n- sprite.pngが生成される\n- _sprite.scssが生成される\n\n![スクリーンショット 2016-09-23 15.56.00.png](https://qiita-image-store.s3.amazonaws.com/0/62264/50c96bff-9e35-43a9-19df-7f5916a0ed6e.png)\n\n\n###gulpの実行\n\n```\n$ gulp\n```\n\n###style.sassを編集・保存\n\n```style.sass\n//生成されたspriteを読み込む指定\n@import \"sprite\";\n\n//使いたい画像を読み込む指定(ここでは、引数に、「$sprite-」+画像のファイル名を書く)\n\n.使いたいクラス名{\n  @include sprite($sprite-cat);\n}\n```\n\n- style.css.mapが生成\n- style.cssが生成\n\n![スクリーンショット 2016-09-23 16.01.01.png](https://qiita-image-store.s3.amazonaws.com/0/62264/cc58f250-7ad2-92c8-1bcf-c38f5b9a4396.png)\n\n\n###gulpfileサンプル\n\n```gulpfile.js\n\nvar gulp = require('gulp');\nvar spritesmith = require('gulp.spritesmith');\nvar sass = require('gulp-sass');\nvar browser = require(\"browser-sync\");\nvar autoprefixer = require('gulp-autoprefixer');\nvar sourcemaps = require('gulp-sourcemaps');\n\ngulp.task('default',['server'],function() {\n  gulp.watch('htdocs/sass/*.scss', ['sass']);\n});\ngulp.task('sass',function () {\n    gulp.src('htdocs/sass/*.scss')\n     .pipe(sourcemaps.init())\n        .pipe(sass())\n        .pipe(autoprefixer(\"last 2 version\", \"ie 8\", \"ie 7\"))\n     .pipe(sourcemaps.write('../maps'))\n     .pipe(gulp.dest('htdocs/css/'))\n     .pipe(browser.reload({stream:true}));\n});\n\ngulp.task(\"server\", function() {\n    browser({\n        server: {\n            baseDir: \"htdocs/\"\n        }\n    });\n});\n\ngulp.task('sprite', function () {\n  var spriteData = gulp.src('htdocs/images/*.png').pipe(spritesmith({\n    imgName: 'sprite.png',\n    cssName: '_sprite.scss',\n    imgPath: '../images/sprite/sprite.png',\n    cssFormat: 'scss',\n    cssVarMap: function (sprite) {\n      sprite.name = 'sprite-' + sprite.name;\n    }\n  }));\n  spriteData.img\n    .pipe(gulp.dest('htdocs/images/sprite/'));\n  spriteData.css\n    .pipe(gulp.dest('htdocs/sass/'));\n});\n```\n\n```style.scss\n\n@import \"sprite\";\n\nbody{\n  padding:50px 0 0 50px;\n}\ndiv{\n  margin-bottom:20px;\n}\nh1{\n  font-size:30px;\n  margin:0 0 50px 0;\n}\n\n.icon1::before{\n  @include sprite($sprite-icon1);\n    content: \"\";\n    margin:-3px 10px 0 0;\n    display: inline-block;\n    vertical-align: middle;\n}\n.icon2::before{\n  @include sprite($sprite-icon2);\n    content: \"\";\n    margin:-3px 10px 0 0;\n    display: inline-block;\n    vertical-align: middle;\n}\n.icon3::before{\n  @include sprite($sprite-icon3);\n    content: \"\";\n    margin:-3px 10px 0 0;\n    display: inline-block;\n    vertical-align: middle;\n}\n.cat{\n  @include sprite($sprite-cat);\n}\n```\n\n```index.html\n\n<!DOCTYPE html>\n<html lang=\"ja\">\n<head>\n<meta charset=\"utf-8\">\n<title>gulp.spritesmithテスト</title>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"http://yui.yahooapis.com/3.18.1/build/cssreset/cssreset-min.css\">\n<link rel=\"stylesheet\" href=\"css/style.css\">\n</head>\n<body>\n<h1>gulp.spritesmithテスト</h1>\n\n<div class=\"icon1\">アイコン1</div>\n<div class=\"icon2\">アイコン2</div>\n<div class=\"icon3\">アイコン3</div>\n<div class=\"cat\"></div>\n</body>\n</html>\n```\n",
    "title": "CSS Sprite自動生成(gulp.spritesmith)"
}
"""


if __name__ == "__main__":
    unittest.main()
