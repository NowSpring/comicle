# Webアプリ環境テンプレ

## Docker環境構築（Django×Vue）

- [DockerでPython×Django×Vue.jsの環境を構築する(サーバー起動編)](https://www.miracleave.co.jp/contents/1715/post-1715/)
- [DockerでPython×Django×Vue.jsの環境を構築する(CORS認証編)](https://www.miracleave.co.jp/contents/1863/post-1863/)

## バックエンドサーバー 編集

- [Djangoでアプリをアプリだけのフォルダににまとめる方法](https://qiita.com/HiroakiIwata/items/b75fff69c61fddd4487d)

## フロントエンドサーバー 編集

### Vuetify

- Vuetifyの追加：`vue add vuetify`

### .eslintrc.json 作成及び編集

- [ESLintと「eslint --init」による「.eslintrc.json」の生成](https://www.konosumi.net/entry/2019/09/01/165449)
- [【Vuetify】Component name "Home" should always be multi-word](https://zenn.dev/teba_eleven/articles/5af8f29e9e200d)
- [Module is not defined and process is not defined in eslint in visual studio code](https://itecnote.com/tecnote/module-is-not-defined-and-process-is-not-defined-in-eslint-in-visual-studio-code/)
- [【vue.js】VSCodeで vue/no-multiple-template-root エラーの原因と対策](https://qiita.com/Moris_Mk-II/items/af0f986531e99e6bf3f0#:~:text=%27vue/no%2Dmultiple%2Dtemplate%2Droot%27%3A%20%27off%27%20%20%20%20//%20%E3%81%93%E3%82%8C%E3%81%A7%E3%81%93%E3%81%AE%E4%BD%99%E8%A8%88%E3%81%AA%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E6%A9%9F%E8%83%BD%E3%82%92%E3%81%8A%E3%81%A3%E3%81%B5%E3%81%AB%E5%87%BA%E6%9D%A5%E3%82%8B%E7%AD%88%E3%81%AA%E3%81%AE%E3%81%AB%E3%80%81%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%AF%E8%A7%A3%E6%B6%88%E3%81%95%E3%82%8C%E3%81%9A%E3%80%82)


## その他

- [タブは半角スペース2つにしたい](https://simplesimples.com/web/application/vscode/tab-space/)
- `rm -rf .git`：gitファイルを削除
- `rm db.sqlite3`：データベースファイルを削除
- `rm apps/app_name/migrations/00*`：マイグレーション設定ファイルを削除
- `rm -rf node_modules package-lock.json && npm install`：clientサーバーで`npm run serve`実行に`sh: vue-cli-service: not found`のエラーが出た場合の対処
- `git branch --contains`：作業中のブランチを表示
 