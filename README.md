# okaiwa
okaiwaはメンションに対してwikipediaのsummaryをリプライするプログラムです。

pythonで作りました。

CK = Consumer Key
CS = Consumer Secret
AT = Access Token
AS = Access Token Secret
として各人自分のkeyを入れてください。
wikikensakukun.pyを実行。
twitter APIでメンションを取得→取得したメンションが「〜とは」となっていたら、「〜」の部分ををwikipediaで検索→検索結果をリプライ　という流れです。

twitter APIの具体的な使い方について参考にさせていただきました
https://qiita.com/konojunya/items/59a68d35e44db8b87186


