#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import wikipedia
import time

CK = ""
CS = ""
AT = ""
AS = ""

twitter = OAuth1Session(CK, CS, AT, AS)

maeno_id = 0
a = 0

while a < 5:
	params = {"count" : 1}
	req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params) #最新のメンションを取得

	mention = json.loads(req.text) #json形式からtext形式に
	for tweet in mention:
		id = tweet["id"]
		men = str(tweet["text"])
	
	if id == maeno_id:
		pass
		print("passしたよー")
	else:
		mention_list = men.split(" ") #ユーザー名と本文を分割
		print (mention_list[1])

		wikipedia.set_lang("jp") #ウィキペヂアで検索
		wiki_serch = wikipedia.summary(mention_list[1] , sentences = 1 )

		params = {"status" : mention_list[0] + " " + wiki_serch} #ウィキペヂアでの検索結果をリプライ
		req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
		
		maeno_id = id
		
	a = a + 1
	time.sleep(10)