# docker-compose.yml説明
* version
docker-compose.ymlの記法バージョン
* services
services配下に各コンテナの情報を記載します。
今回だとdemo-appが該当箇所です。
demo-appはコンテナ名ではないので気をつけてください。
service名は一般的にはコンテナ名と同じにしてる気がします。。。
コンテナ名を設定したかったら、
```
container_name: コンテナ名
```
で設定可能です。
* build
ビルドするDockerfileのパスを指定します。
* volumes
コンテナのディレクトリをホスト側のディレクトリにマウントします。
マウントは、コンテナ側のディレクトリとホスト側のディレクトリを一緒にするイメージです。
ちょっと説明しづらいんで調べてみてください。マウントはDockerに限った話ではなく、一般的な用語です。
https://amateur-engineer-blog.com/docer-compose-volumes/
このサイトとかわかりやすいです。
* ports
ホスト側のポートとコンテナのポートをつなげています。(ポートフォワーディング)
左側がホスト側のポート番号。右側がコンテナ側のポート番号です。
webブラウザ上でlocalhost:8000にアクセスすると、コンテナの8000番にポートフォワーディングされます。
