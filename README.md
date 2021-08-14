# bpy-sandbox

詳細は[公式Docs](https://docs.blender.org/api/current/index.html)の参照を推奨


## 実行Ver.
* 2.83.1 (Windows10)

## 外部Pythonライブラリの追加
* インストールしたBlenderのフォルダ内にPythonが同梱されており，外部Pythonライブラリを追加できる
    * pip: (blender.exeのある階層)/(バージョン名フォルダ)/python/Scripts/pip.exe
        * コンソールから`pip.exe install (xxx)`のように実行することで，pipの機能が利用できる

## Script実行法
* Note: 複数の実行法がある
    * Add-onとしてクラスを作成する
        * クラスとして追加し([参考](https://docs.blender.org/api/current/info_overview.html))，GUIからコマンドを選択することで実行する(Edit→Operator Search)
    * Scriptingモード左側のコマンドラインから入力する
        * 対話入力のため，長いコマンドには向かない．API確認で用いることが多い．Tabキーで補完できる
    * Scriptingモード中央のテキストエディタから実行する
        * `bpy.ops`などオペレーションを逐次実行することで，スクリプト実行時に所望の動作を実現する
