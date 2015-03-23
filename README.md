# fabmod5-rpi
FabModules on HTML5をRaspberry piと連携させるためのソフトウェアです。

## 機器構成
[](fabmod5-structure.png)

## 依存環境
Raspberry pi: Raspbian wheezyで確認済みです。

リレーサーバ: CentOS 6.5上で構築しました。

いずれもpythonのtornadoフレームワークを利用しています。

tornadoのインストール
```
sudo pip install tornado
```

## Raspberry pi
MDX-15/20のシリアルUSBケーブルをRaspberry piのUSBポートに挿入して下さい。
```
cd websocket
python client.py
```

## リレーサーバ
```
cd relay-server
python server.py
```
