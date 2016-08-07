Hatena blogからpelicanに移行した
=================================

:date: 2016-08-07 16:16
:tags: 
:category: misc
:authors: cocuh
:lang: ja
:slug: start-blog

..
    :summary: Short version for index and feeds
    :modified: 2016-08-07 16:16
    :slug: my-super-post

少し前までHatena blogを使っていましたが，数式関連がかなりつらかったのでgithub pagesとpelicanに移行しました．
hatena blogには，これまでありがとうございましたという気持ちです．

ちょっとpelicanにも不満があるのでいづれ自分でblog generatorを作る気がします．

.. PELICAN_END_SUMMARY


なんでHatena blogが不満だったか
--------------------------------
hatenaの人が見てくれることもすこし期待して．

**1. 自動リンク**

hatena blogには自動リンク機能があります．
関連ワードにリンクはる機能ですけど，余計なところにlinkを貼ったりして厄介です．
proだとこの機能を切れるらしいですが，proにするほど使わないし．月額500円はちょっとたかい．


**2. 数式**

hatena記法には数式書ける方法がありますが，markdownでは使えないので，mathjaxを使っています．
mathjaxだと1行に複数書くとうまく動かなったり，mathjaxの中で自動リンクが働くとmathjaxが適用されなくなったります．
なので，自動リンクされない単語で1行に複数書かないように工夫する必要があってめんどくさいです．
machine learningとかやっていると数式だらけになるのでストレスなく数式が書けないとつらいです．


**3. 投稿インターフェース**

投稿はwebで投稿できますが，git pushでぽいぽい投げたいという気持ちがあります．
手軽さ的には，webで書くよりいつも使っているエディターで書きたいです．

hatenaにもatompubのAPIがありますが，2016年になってatompubを使いたいという気力はないです．
gitで投稿できればうれしい．


Hatenaの良いところ
-------------------

**1. hatena star**
**2. view数のメール**
**3. hatena bookmark**

投稿のモチベーションが維持できるのでこれは非常によい．

**4. subscribe**

最近あんまり見なくなりましたけど，hatenaで他のblogのsubscribeができるのでたのしいです．


**5. 各種サイトの埋め込み**

非常に便利



わたしがblogにもとめた要件
--------------------------

**1. 数式が書きやすい**
**2. ipython notebookで投稿できる**

machine learningの実験とかipython notebookでしてるので，それでもblogが書けるようにしたいです．
jupyter nbconvertを使うとreStructuredTextが出力できるので便利です．

.. math::

    f(\mathbf{x};\mathbf{w}) = \mathbf{w}^T\mathbf{x}

.. math::

    J(\mathbf{w}) = \sum_{(\mathbf{x}, y)\in D}\left(y-f(\mathbf{x}; \mathbf{w})\right)^2+ c\|\mathbf{w}\|_1

.. math::
    \mathbf{w}^\ast = \underset{\mathbf{w}}{\mathrm{argmin}} J(\mathbf{w})


**3. gitで投稿できる**
**4. デザインが簡単にcss+htmlでできる**
**5. コードが綺麗にhighlightできる**
**6. gist, github embedding**

デベロッパーはこういうのが便利に使えないと生きていけないので…

.. code-block:: python

    import re
    l = list(map(str, range(100)))


pelicanが満たしてない要件
-------------------------
pelicanは先の要件をすべて満たしてますが，次を満たしてないです．
なので元気がアレばstatic site generatorを作りたい．(まぁ元気があれば…)

**1. debugがめんどくさい**
**2. shareまわり**
**3. サムネイル生成**


..
    .. math::
        x^2

..
    inline :math:`x^2`
