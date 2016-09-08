Python+Rustでマルチスレッドな並列プログラミング
======================================================

:date: 2016-09-08 19:21
:tags: Rust, Python, programming
:category: software
:authors: cocuh
:slug: python_rust_parallel
:lang: ja

| アルゴリズムを見て **「むむっ…マルチスレッドで共有メモリごりごりしたい」** と思うことが皆様あると思います．
| しかしながらPythonにはGILがあるため，マルチスレッドをしても並列に処理されません．
|
| C++やRustで書いてもいいですが，データ処理をする人間からすると，C++/Rustは常用したくないです．
| Rustで処理したものをディスクに保存して，Pythonから読み出すという手もありますが，管理が煩雑でミスをはらみやすいです．
| そのため， **アルゴリズムのcoreの部分をRustで書き，Python bindingを作る** ことを考えます．

.. PELICAN_END_SUMMARY

Rust <-> Pythonのbindingとして， `rust-cpython <https://github.com/dgrunwald/rust-cpython>`_ があります．

https://github.com/dgrunwald/rust-cpython

| このライブラリは，Rustのコンパイル時にPythonからimport可能なshared objectにできます．
| (余談ですがRustからPython interpreterを呼び出すこともできます)
| 記法はこんな感じ
| Rustなので，並行処理が便利にできます・ω・

.. code:: Rust

  #![crate_type = "dylib"]
  #[macro_use]
  extern crate cpython;

  use std::thread;
  use std::sync::{Arc, Mutex};
  use cpython::{PyResult, Python, PyList, ToPyObject};

  py_module_initializer!(sort, initsort, PyInit_sort, |py, m| {
      try!(m.add(py, "__doc__", "sleep sort"));
      try!(m.add(py, "sleep_sort", py_fn!(py, sleep_sort(py_args: PyList))));
      Ok(())
  });


  fn sleep_sort(py: Python, py_args: PyList) -> PyResult<PyList> {

      // convert Python object to Rust object
      let args: Vec<u32> = py_args.iter(py)
          .map(|x| x.extract(py))
          .filter(|x| x.is_ok())
          .map(|x| x.ok().unwrap())
          .collect::<Vec<_>>();

      // generate workers
      let result = Arc::new(Mutex::new(Vec::<u32>::new()));
      let workers = args.into_iter().map(|x| {
              let result = result.clone();
              thread::spawn(move || {
                  thread::sleep_ms(x * 100);
                  let mut result = result.lock().unwrap(); // Rust's COOL mutex!!
                  result.push(x);
              })
          })
          .collect::<Vec<_>>();

      // join worker threads
      workers
          .into_iter()
          .map(|x| {
              x.join();
          })
          .collect::<Vec<_>>();

      // convert Rust object to Python object
      let res = result.lock().unwrap().to_py_object(py);
      Ok(res)
  }


:code:`Cargo.toml` はこんな感じ

.. code::

  [package]
  name = "sort"
  version = "0.1.0"
  authors = ["cocuh"]

  [dependencies.cpython]
  git = "https://github.com/dgrunwald/rust-cpython.git"
  default-features = false
  features = ["python3-sys"]

  [lib]
  name="sort"
  crate-type=["dylib"]

| これをcargoでbuildすると:code:`.so` が:code:`./target/debug/hoge.so` にできます．
| この :code:`.so` を :code:`sort.cpython-35m-x86_64-linux-gnu.so` にrenameして同じディレクトリでpythonを開くと読み込めます

.. code:: pycon

  Python 3.5.2 (default, Jun 28 2016, 08:46:01)
  [GCC 6.1.1 20160602] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import sort
  >>> sort
  <module 'sort' from '/tmp/rust-sort/target/debug/sort.cpython-35m-x86_64-linux-gnu.so'>
  >>> sort.sleep_sort([5,1,2,6,8,2,4,2,3,8,0,2])
  [0, 1, 2, 2, 2, 2, 3, 4, 5, 6, 8, 8]
  >>>

| このままだとめんどくさいので
| pipで便利に入れられるようなツールを作ったのでどうぞおつかいください

https://github.com/cocuh/python-rust-ext

:code:`setup.py` をこんな感じに書けば :code:`python setup.py install` で勝手にビルドして入れてくれます．べんり！

.. code:: python

  from setuptools import setup
  from rust_ext import build_rust, install_with_rust, RustModule

  rust_modules = [
      RustModule(
              'sort',
              'src/Cargo.toml',
      ),
  ]

  setup(
          name='sort',
          version='0.0.1',
          cmdclass={
              'build_rust': build_rust,
              'install_lib': install_with_rust,
          },
          options={
              'build_rust': {
                  'modules': rust_modules,
              }
          },
          zip_safe=False,
  )


| こんな感じで意外と便利にpython extensionをRustで書けるので，やってみてはいかがでしょうか．
| いま，分枝限定法をPythonで便利に使えるRustを書いてたりしますが，其の話はまた今度できれば．

..
    .. math::
        x^2

..
    inline :math:`x^2`
