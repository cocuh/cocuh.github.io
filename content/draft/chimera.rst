複数の言語で一つのプログラムを書くということ(WIP)
====================================================


:tags: chimera, software design, python
:category: software 
:authors: cocuh
:slug: chimera
:lang: ja
:date: 2016-08-10 21:55

1つのプロジェクトが1つの言語で完結することが少なくなっています．
webアプリケーションで例えれば，backendはPythonで書き，frontendはJavaScriptを使っているなどです．
このような1つのプロジェクトに複数の言語が混在させるソフトウェア設計論について，あまり多く議論されてきませんでした．

本記事の内容は以下のようになっています．
..

  TODO

この記事の内容は `PyConJp 2016 <https://pycon.jp/2016/ja/schedule/presentation/33/>`__ にて発表予定です．


読むのに必要なスキル
~~~~~~~~~~~~~~~~~~~~~
- Pythonが読める
- Python以外の言語に触ったことのある

.. PELICAN_END_SUMMARY


Why I focus it.
---------------

私の研究の中でNP困難な問題を解く必要がでてきました．
並列計算をする必要がありGILのあるPythonのみでは困難です．
これでの研究はすべてPythonとIPython notebook上で行っているため，これまでの資産がありました．
この資産を捨て，Python以外の言語で再実装するのはナンセンスです．
そのため，NP困難な問題のソルバーをRustやCythonを用いて実装し，Pythonから実行可能にすることを考えます．

より抽象的に考えた際に，プログラミング言語それぞれの文法・文化・ライブラリに対し得意/不得意が存在すると考えることができます．
さきほどは，Pythonの不得意な処理(並列処理)に関しては，並列処理の得意なRustを用いて実装するという手段を取りました．
同様に，actor modelのような並行処理を行うプログラムを書く場合，Pythonよりerlangを用いて記述したくなりますが，実際の処理の部分はライブラリの豊富なPythonで実装したいです．
このように，あるコンポーネントはある言語で書きたいが，ほかのコンポーネントは別の言語で書きたいという欲求がでてきます．

本記事ではこのような，別々の言語で実装されたモジュールを組合せ，一つのプロジェクトを実現するプログラミング技法を議論します．


Chimera
-------

本記事では， `複数の言語が組み合わさった状態` を `キメラ` と呼ぶこととします．
厳密風な定義もいくつか考えましたが，しっくりこなかったのでゆるい定義となってます．

キメラの例をコードを用いて示します．

.. code::Python
  import numpy as np
  
  x = np.arange(5)    # x=[0, 1, 2, 3, 4]
  mean = x.mean()     # mean = 2

たとえば，numpyの :code:`numpy.arange` は実はCで実装されています． `source<https://github.com/numpy/numpy/blob/3e396148edfe91214c7baa03492f523ca53680e8/numpy/core/src/multiarray/ctors.c#L2939>`__
:code:`numpy.ndarray` もCのオブジェクトです． `doc<http://docs.scipy.org/doc/numpy/reference/c-api.types-and-structures.html>`__

なので，このコードはPythonとCが組み合わさった状態であるのでキメラです．




Chimeraの種類
----------------

モジュール間の関係には4種類あると私は思います．

1. 対等
  1. P2P
2. 従属
  1. 異なるホスト上のプロセスに呼び出し(Remote Procedure Call)
  2. 同一のホスト上に異なるプロセスが存在(Local Procedure Call)
  3. 同一のホスト上の同一のプロセス上にモジュールが(Procedure Call)



..
    .. math::
        x^2

..
    inline :math:`x^2`
