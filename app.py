"By - Hussein: t.me/jj8jjj8"

from flask import Flask, request, jsonify
import requests , re,json
#from markupsafe import escape

import spotipy,datetime
from spotipy.oauth2 import SpotifyClientCredentials

from user_agent import generate_user_agent
import telebot,requests,os,re
import wget
from youtube_search import YoutubeSearch

def YTLink(trackName,artist):
	results = list(YoutubeSearch(str(trackName + " " + artist)).to_dict())
	YTSlug = ''
	for URLSSS in results:
		timeyt = URLSSS["duration"]
		timeyt = datetime.datetime.strptime(timeyt, '%M:%S')
		YTSlug = URLSSS['url_suffix']
		YTLink = str("https://www.youtube.com/" + YTSlug)
		break
	return YTLink
spotify = spotipy.Spotify(
client_credentials_manager=SpotifyClientCredentials(client_id='a145db3dcd564b9592dacf10649e4ed5',client_secret='389614e1ec874f17b8c99511c7baa2f6'))

def media(url,site):
	print(url)
	headers = {
		'authority': 'www.y2mate.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://www.y2mate.com',
		'referer': 'https://www.y2mate.com/mates/analyzeV2/ajaxm',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		'k_query': url,
		'k_page': site,
		'hl': 'en',
		'q_auto': "1"
	}
	response = requests.post("https://www.y2mate.com/mates/analyzeV2/ajax",headers=headers,data=data)
	#if response.json()["status"] == "ok":
	return response.json()

def tiktokV2(url):
	headers = {
		'authority': 'ttsave.app',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/json',
		'origin': 'https://ttsave.app',
		'referer': 'https://ttsave.app/',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		"id": url,
		#'k_page': site,
#		'hl': 'en',
	}
	response = requests.post("https://ttsave.app/download?mode=video&key=f5760dbb-4e86-42a3-9cd5-a3f822866fbb",headers=headers,json=data)
	#if response.json()["status"] == "ok":
	text = response.text
	photo = re.findall('<a href=(.*?)" target',text)
	name = re.findall('title="(.*?)"',text)
	views = re.findall('<span class="text-gray-500">(.*?)</span>',text)
	links = None
	audio = None
	type = "video"
	if "DOWNLOAD AUDIO (MP3)" in text:
		links = re.findall('<img src="(.*?)">',text)
		audio = re.findall('<a href="(.*?)" onclick',text)
		type = "photos"
	else:
		links = re.findall('<a href="(.*?)" onclick',text)
	return {
		"photo": photo,
		"name": name,
		"views": views,
		"links": links,
		"audio": audio,
		"type": type
	}

def twitter(url):
	headers = {
		'authority': 'ssstwitter.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://ssstwitter.com',
		'referer': 'https://ssstwitter.com/',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		"hx-request": "true",
		"hx-target": "target",
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': "empty",
		'sec-fetch-mode': "core",
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		'id': url,
		'locale': "en",
		'source': 'from',
		#"tt": "1530f2ae5f337201c01cf1f84d3fa3c6",
#		"ts": "1696714020"
}
	response = requests.post("https://ssstwitter.com/",headers=headers,data=data)
	#if response.json()["status"] == "ok":
	url = response.text
	link = re.findall('<a href="(.*?)"',url)[3]
	return {"link": link}
def snapchat(url):
	headers = {
		'authority': 'solyptube.com',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://solyptube.com',
		'referer': 'https://solyptube.com/snapchat-video-download',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': "empty",
		'sec-fetch-mode': "core",
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		'url': url,
		#'source': 'from',
}
	response = requests.post("https://solyptube.com/findsnapchatvideo",headers=headers,data=data)
	info = response.json()
	url = info["data"]["snapList"][0]["snapUrls"]["mediaUrl"]
	title = info["title"]
	data = {
		"link": url,
		"title": title,
		#"By - Hussein": "t.me/jj8jjj8"
	}
	return data
def snapStory(url):
	headers = {
		'authority': 'solyptube.com',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://solyptube.com',
		'referer': 'https://solyptube.com/snapchat-video-download',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': "empty",
		'sec-fetch-mode': "core",
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		'url': url,
		#'source': 'from',
}
	response = requests.post("https://solyptube.com/findsnapchatvideo",headers=headers,data=data)
	info = response.json()
	url = info["data"]["snapList"]
	title = info["title"]
	data = {
		"link": url,
		"title": title,
		#"By - Hussein": "t.me/jj8jjj8"
	}
	return data

def pint(url):
	headers = {
		'authority': 'dotsave.app',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://dotsave.app',
		'referer': 'https://dotsave.app/',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		'url': url,
		'lang': "en",
		'type': 'redirect'
}
	response = requests.post("https://dotsave.app/",headers=headers,data=data)
	#if response.json()["status"] == "ok":
	link = re.findall('<a id="downloadBtn" href="(.*?)" hidden rel="nofollow">',response.text)[0].replace("https://dl.cdn.io.vn/?url=","")
	photo = re.findall('<div class="video-header mb-3"><img src="(.*?)" class="avatar"',response.text)[0]
	data = {
		"link": link,
		"thmub": photo,
		#"By - Hussein": "t.me/jj8jjj8"
	}
	return data

def post(url):
	headers = {
		'authority': 'www.w3tyos.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://www.w3toys.com',
		'referer': 'https://www.w3toys.com/core/ajax.php',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
	}
	data = {
		'url': url,
		'host': "instagram"
	}
	response = requests.post("https://www.w3toys.com/core/ajax.php",headers=headers,data=data)
	text = response.text
	urls = re.findall('<a href="(.*?)" class',text)
	photos = []
	videos = []
	for url in urls:
		url = "https://www.w3toys.com/"+url
		f = requests.head(url)
		f = f.headers["Content-Disposition"].split('filename="')[1].split('"')[0]
		if "jpeg" in f or "png" in f or "jpg" in f:
			photos.append(url)
		else:
			videos.append(url)
	data = {
		"photo": photos,
		"video": videos
		}
	return data

def fb(url,num=None):
	headers = {
		'authority': 'www.getfvid.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://www.getfvid.com',
		'referer': 'https://www.getfvid.com/downloader',
		'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document:',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
	}
	data = {'url': url}
	
	response = requests.post("https://www.getfvid.com/downloader",headers=headers,data=data)
	#if response.json()["status"] == "ok":
	text = response.text
	url = re.findall('<a href="(.*?)" target',text)
	result = True
	if len(url) < 1:
		result = False
	return  {
		"result": result,
		"links": url
	}

def story(url):
	headers = {'user-agent': generate_user_agent()}
	response = requests.get(f"https://gramsnap.com/api/ig/story?url=https%3A%2F%2Fwww.instagram.com%2Fstories/{url}",headers=headers)
	return response.json()

app = Flask(__name__)

@app.route("/")
def Welcome():
	return """Welcome, this is my API for download from any site

content: https://t.me/jj8jjj8 ~ for how u use it"""

@app.route("/instagram")
def insta():
	url = request.args.get("url")
	site = "instagram"
	return media(url,site)

@app.route("/post")
def pos():
	url = request.args.get("url")
	return post(url)

@app.route("/story")
def in_story():
	url = request.args.get("url")
	return story(url)

@app.route("/highlights")
def in_highlights():
	url = request.args.get("url")
	return highlights(url)

@app.route("/pinterest")
def pinterest():
	url = request.args.get("url")
	return pint(url)

@app.route("/tiktok")
def tik():
	url = request.args.get("url")
	site = "tiktok"
	return media(url,site)

@app.route("/tiktokV2")
def tik2():
	url = request.args.get("url")
	return tiktokV2(url)

@app.route("/snapchat")
def snap():
	url = request.args.get("url")
	return snapchat(url)

@app.route("/snapStory")
def snap_s():
	url = request.args.get("url")
	return snapStory(url)

@app.route("/twitter")
def twitt():
	url = request.args.get("url")
	return twitter(url)

@app.route("/threads")
def thread():
	url = request.args.get("url")
	headers = {
		'authority': 'savevideofrom.me',
		'content-type': 'application/x-www-form-urlencoded',
	}
	data = {
		'url': url,
	}
	response = requests.post('https://savevideofrom.me/wp-json/aio-dl/video-data/',headers=headers, data=data).json()
	title = response['title']
	url = response['medias'][1]['url']
	return {"link": url,"title": title}

@app.route("/spotify")
def spotif():
	url = request.args.get("url")
	
	song = spotify.track(url)
	trackName = song['name']
	artist = song['artists'][0]['name']
	duration = int(song['duration_ms'])
	
	site = "youtube"
	link = YTLink(trackName,artist)
	#link = media(link,site)
	return {
		"title": f"{trackName} {artist}",
		"link": link
	}

@app.route("/facebook")
def facebook():
	url = request.args.get("url")
	link = fb(url)
	return link

if __name__ == "__main__":
	#media.run()
    app.run(host='0.0.0.0', port=8080)
