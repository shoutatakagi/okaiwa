maeno_id = 0
while true:
	params = {"count" : 1}
	req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params) #最新のメンションを取得

	mention = json.loads(req.text) #json形式からtext形式に
	for tweet in mention:
		id = str(tweet["id_str"])
		men = str(tweet["text"])
	
	if id == maeno_id:
		pass
	else:
		mention_list = men.split(" ") #ユーザー名と本文を分割

		wikipedia.set_lang("jp") #ウィキペヂアで検索
		wiki_serch = wikipedia.summary(mention_list[1] , sentences = 1 )

		params = {"status" :　mention_list[0] + " " + wiki_serch} #ウィキペヂアでの検索結果をリプライ
		req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
		
		maeno_id = id
		
	time.sleep(300)