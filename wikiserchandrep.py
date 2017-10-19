#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json

#各種キー
CK = 
CS = 
AT = 
AS = 

#OAuth認証
twitter = OAuth1Session(CK, CS, AT, AS)


#最新のメンションの取得
	params = {"count" : 1}
	req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params) #最新のメンションを取得

	mention = json.loads(req.text) #json形式からtext形式に
	for tweet in mention:
		id = str(tweet["id_str"])
		men = str(tweet["text"])
	
	mention_list = men.split(" ") #ユーザー名と本文を分割

#ウィキペヂアで検索
	wikipedia.set_lang("jp")
	wiki_serch = wikipedia.summary(mention_list[1] , sentences = 1 )

#ウィキペヂアでの検索結果をリプライ
	params = {"status" :　mention_list[0] + " " + wiki_serch}
	req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
	
	