#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import time
import wikipedia

CK = 
CS = 
AT = 
AS = 

a = 0
maenoid = 0
while a < 5:
	params = {"count" : 1}
	twitter = OAuth1Session(CK, CS, AT, AS)#OAuth認証
	req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params)#最新のメンションを取得
	mention = json.loads(req.text)#json形式からtext形式に

	for tweet in mention:#getしたmentionからidとmention本文を抽出
		id = tweet["id"]
		men = tweet["text"]
	mention_list = men.split(" ")#ユーザー名と本文を分割
	
	if maenoid == id:#最新mentionのidと1つ前に取得したmentionのidをくらべてる
		pass
		print("passしたよー")
	else:
		print(id)
		print(men)
		wikipedia.set_lang("jp")#言語の設定
		try:
			wiki_serch = wikipedia.summary(mention_list[1] , sentences = 1)#wikipediaでmentionを検索し、検索結果の1文目を保存
			print(wiki_serch)
			params = {"status" : mention_list[0] + " " + wiki_serch}
		except:
			params = {"status" : mention_list[0] + " " + "該当なしだよ〜"} 
		req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)#検索結果をリプライする
		maenoid = id
	
	a = a + 1
	time.sleep(100)