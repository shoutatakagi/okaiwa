#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import wikipedia
import time

#各種キー
CK = "QR4q8VZYowCgzGkGBAyiAc3G4"
CS = "uRNj9Ubn0uifafkNEErkzV7QveCfjSdsNcMnKkS4XcSKvO4q"
AT = "3068002118-PexBZB6i4wbG3Rr0CePSENXDXuHWkXNMGEIZN6Y"
AS = "UnShbbVfy49vMmpuLiTXqEKGP0663kNPlzTDL6rHT2lSu"

#OAuth認証
twitter = OAuth1Session(CK, CS, AT, AS)
id = 0

params = {"count" : 1, "since_id" : id}
req = twitter.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json", params = params) #最新のメンションを取得

mention = json.loads(req.text) #json形式からtext形式に
for tweet in mention:
	id = str(tweet["id_str"])
	men = str(tweet["text"])
print(men)