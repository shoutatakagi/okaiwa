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

	twitter = OAuth1Session(CK, CS, AT, AS)
	req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params) #最新のメンションを取得
	tweetjouhou = json.loads(req.text) #json形式からtext形式に

	for tweet in tweetjouhou:
		id = tweet["id"]
		mention = tweet["text"]
		username = tweet["user"]["screen_name"]
	mention_list = mention.split(" ") #ユーザー名と本文を分割
	
	if maenoid == id:
		print("passしたよー")
		pass
	else:
		print(id)
		print(mention)
		
		men = [x for x in mention_list[1]]
		if men[-2:] == [u'\u3068',u'\u306f']:#メンションが_とは_で終わっていたら
			kensaku = [x for x in men[:-2]]
			kensaku = "".join(kensaku)
			wikipedia.set_lang("jp")
			try:
				wiki_serch = wikipedia.summary(kensaku , sentences = 1)
				print(wiki_serch)
				params = {"status" : "@"+ username + " " + wiki_serch}
			except:
				print(wiki_serch)
				params = {"status" : "@" + username + " " + "該当なしだよ〜"} 
			req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
			maenoid = id
		else:
			print("とはでおわってなかったよー")
			mentionid = id
			pass
	
	a = a + 1
	time.sleep(100)