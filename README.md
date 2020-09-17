# スタンプ生成器

## 用途

以下の内容が書かれたテキストから
> おは  
> よう

SVGを経由してこのような画像を作るスクリプト
![](./ohayo.svg)

SVG画像は現状、pythonのcairosvgで表示できるよう想定してある

## 使用方法

コマンドラインから

~~~shell
python stamp_generator.py <テキストファイル>
~~~

pythonから

`stamp_generator.py`の`gen_stamp`を呼び出す
