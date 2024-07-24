"By - Hussein: t.me/jj8jjj8"

from flask import Flask, request, jsonify
import requests , re,json,datetime
#from markupsafe import escape

#import spotipy,datetime
#from spotipy.oauth2 import SpotifyClientCredentials

from user_agent import generate_user_agent
import requests,os,re
import wget
from youtube_search import YoutubeSearch
import base64
from requests import session
from html import unescape
from re import findall
from bs4 import BeautifulSoup as bs

def generate_token():
	client_id = "6c44266fd2944c1e8e249addc27ae17c"
	client_secret = "a8ab1660f55c48deadfb9338027678bd"
	
	auth_options = {
	    'url': 'https://accounts.spotify.com/api/token',
	    'headers': {
	        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()
	    },
	    'data': {
	        'grant_type': 'client_credentials'
	    }
	}
	
	response = requests.post(auth_options['url'], headers=auth_options['headers'], data=auth_options['data'])
	if response.status_code == 200:
	    token = response.json()['access_token']
	return token

def YTLink(trackName,artist,):
	results = list(YoutubeSearch(str(trackName + " " + artist)).to_dict())
	YTSlug = ''
	for URLSSS in results:
		timeyt = URLSSS["duration"]
		timeyt = datetime.datetime.strptime(timeyt, '%M:%S')
		YTSlug = URLSSS['url_suffix']
		YTLink = str("https://www.youtube.com/" + YTSlug)
		break
	return YTLink
#spotify = spotipy.Spotify(
#client_credentials_manager=SpotifyClientCredentials(client_id='a145db3dcd564b9592dacf10649e4ed5',client_secret='389614e1ec874f17b8c99511c7baa2f6'))

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

def reels(url):
	cookies = {
	    '_ga_HYFL742GNR': 'GS1.1.1717265838.1.0.1717265838.0.0.0',
	    '_ga': 'GA1.1.1268182027.1717265838',
	    '__gads': 'ID=ee92df8e37a22417:T=1717265839:RT=1717265839:S=ALNI_Maf1lAc8gh_k213_o0h9Lb0q3BOHA',
	    '__gpi': 'UID=00000e39bc9df11d:T=1717265839:RT=1717265839:S=ALNI_MYg36c1aJEVTsrrq7SWBJdh7Y8LPg',
	    '__eoi': 'ID=2013eb5969ce8efb:T=1717265839:RT=1717265839:S=AA-Afjb0NEbplYb8UrZHDhGpYGDB',
	    '__gsas': 'ID=3c5ca9f6240fb535:T=1717265847:RT=1717265847:S=ALNI_MZxouHjuMrMafM_CQMczxdJmDvkrw',
	    'FCNEC': '%5B%5B%22AKsRol96yZWx7FK5sPkCWa1kmfU6tsXGconfu10nsHP9CB3x2vDd-oFwIPpJp-oxaQleN0SpAaw5YK8pVDRsL447EoZLPPe9ld_nFbhUCDqyErJh1YwpJZ1Pj58v12_WItXE_CCWIVa4RkTuSulwNUJfXDd0AemQNw%3D%3D%22%5D%5D',
	}
	headers = {
	    'authority': 'snapinsta.io',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7,ku;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://snapinsta.io',
	    'referer': 'https://snapinsta.io/en20',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	    'q': url,
	    't': 'media',
	    'lang': 'en',
	}
	r = requests.post('https://snapinsta.io/api/ajaxSearch', cookies=cookies, headers=headers, data=data).text
	res = json.loads(r)
	con = res.get('data', '')
	videos = []
	if con:
		soup = bs(con, "html.parser")
		find = soup.find_all("div", {"class": "download-items__btn"})
		for vid in find:
			final = vid.find('a', href=True)
			if final:
				video = final['href']
				videos.append(video)
			else:
				print("error")
	else:
		print("error2")
	return videos

def highlights(url):
	url = f"https://api.sssgram.com/st-tik/ins/dl?url={url}&timestamp=1708718711348"
	headers = {
		'authority': 'api.sssgram.com',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		#'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://www.sssgram.com',
		'referer': 'https://www.sssgram.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	response = requests.get(url,headers=headers)
	#if response.json()["status"] == "ok":
	return response.json()

def tiktok(url):
	#print(url)
	headers = {
		'authority': 'tikvideo.app',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://tikvideo.app',
		'referer': 'https://tikvideo.app/en',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
	}
	data = {
		'q': url,
		'lang': 'en',
	}
	response = requests.post("https://tikvideo.app/api/ajaxSearch",headers=headers,data=data)
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

def pinterest(url):
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

def pinterestV2(url):
	headers = {
		'authority': 'www.pinterest.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		#'origin': 'https://www.y2mate.com',
		'referer': 'https://www.pinterest.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
}
	data = {
		"data": {
			"options": {
				"source": "browser",
				"stats": [
					[
						"recaptcha_auth.done",1,"c",1,
						{"action":"mweb_auth"}
					]
				],
			"keepAlive":True}
		}
	}
	response = requests.get(url,headers=headers,data=data)
	m = response.text
	#print(m)
	try:
		#link = m.split('{"videoUrls":["')[1]
		links = []
		link = re.findall(r'https://v1\.pinimg\.com/videos/mc/.*?\.mp4',m)
		for i in link:
			if "_t4.mp4" in i or "_t5.mp4" in i:
				links.append(i)
		link = links[0]
	except:
		link = m.split('"images":{"url":"')[1].split('"},')[0]
	return {"link": link,"by": "By @jj8jjj8 ~ hussein rashid"}

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

def postV2(id):
    url = "https://getindevice.com/wp-json/aio-dl/video-data/"
    headers = {
        'Origin': 'https://getindevice.com/',
        'Referer': 'https://getindevice.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
    }
    data = {"url": id}
    response = requests.post(url, headers=headers, data=data)
    
    return response.json()

def postV3(url):
	shortcode = url.split("/")[4]
	print(shortcode)
	response = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{shortcode}%22%7D",headers={"user-agent": generate_user_agent()}).json()["data"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]
	return response

def fb(url,num=None):
	headers = {
		#'authority': 'fdown.net',
		#'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		#'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded',
		#'origin': 'https://fdown.net',
		'referer': 'https://getindevice.com/facebook-video-downloader/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		#'sec-fetch-dest': 'document:',
		#'sec-fetch-mode': 'navigate',
		#'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent()
	}
	data = {'url': url}
	
	response = requests.post("https://getindevice.com/wp-json/aio-dl/video-data/",headers=headers,data=data)
	#if response.json()["status"] == "ok":
	text = response.json()
	#url = re.findall('href="(.*?)" download=',text)
	result = True
	if len(url) < 1:
		result = False
	return  {
		"result": result,
		"links": text["medias"][1]["url"]
	}


def story(url):
	headers = {'user-agent': generate_user_agent()}
	response = requests.get(f"https://gramsnap.com/api/ig/story?url=https%3A%2F%2Fwww.instagram.com%2Fstories/{url}",headers=headers)
	return response.json()

def threads(url):
	#headers = {
#		'authority': 'savevideofrom.me',
#		'content-type': 'application/x-www-form-urlencoded',
#	}
#	data = {
#		'url': url,
#	}
#	response = requests.post('https://savevideofrom.me/wp-json/aio-dl/video-data/',headers=headers, data=data).json()
#	title = response['title']
#	url = response['medias'][1]['url']
#	return {"link": url,"title": title}
	id = url.split("/")[5]
	try:
		response = requests.get(f"https://api.twitterpicker.com/threads/post/media?id={id}",headers={"user-agent":generate_user_agent()}).json()["media"]
		images = [i["variants"][0]["url"] for i in response["images"]]
		videos = [i["variants"][0]["url"] for i in response["videos"]]
		return {"result": True,"images":images,"videos":videos}
	except Exception as error:
		print(error)
		return {"result": False,"images":[],"videos":[]}

class Spotify:
	def __init__(self):
		self.base_url = "https://api.spotify.com/v1/tracks/"
		self.headers = {
			"Authorization": f"Bearer {generate_token()}"
		}
	def regex(self,url):
		self.url = url.split("/track/")[1].split("?")[0]
		return self.url
	
	def track(self,url):
		self.url = self.regex(url)
		self.response = requests.get(
			self.base_url+self.url,
			headers=self.headers
		).json()
		return self.response

def spotify(url):
	try:
		song = Spotify().track(url)
		trackName = song['name']
		artist = song['artists'][0]['name']
		duration = int(song['duration_ms'])
		link = YTLink(trackName,artist)
		#link = media(link,site)
		return {
			"status": True,
			"title": f"{trackName} {artist}",
			"link": link
		}
	except:
		print(song)
		return {
			"status": False
		}

def tiktokV3(url):
	response = requests.post("https://api.tikmate.app/api/lookup",data={"url":url}).json()
	token = response["token"]
	id = response["id"]
	link = "https://tikmate.app/download/"+token+"/"+str(id)+".mp4"
	return link

def tiktokV4(url):
    headers = {
        'Authority': 'lovetik.com',
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.1.1563155980.1686484280; __gads=ID=8ab5aeca5487c0f1-227f5b1b59e10038:T=1686484286:RT=1686484286:S=ALNI_MadOUeX11vqaOD_u9KmsDgQtgaPkQ; __gpi=UID=00000c49df53e0aa:T=1686484286:RT=1686484286:S=ALNI_Ma6YE6x-NSfM_QqcvXbrZXKAHF59A; _ga_30X9VRGZQ4=GS1.1.1686484279.1.1.1686484453.0.0.0',
        'Origin': 'https://lovetik.com',
        'Referer': 'https://lovetik.com/sa/video/@2a__.12/7220470788711779591',
        'Save-Data': 'on',
        'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; DRA-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'query': url
    }

    response = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data)
    json_response = response.json()
    return json_response

def info_instagram(username):
	try:
		response = requests.get(f"https://storiesig.info/api/ig/userInfoByUsername/{username}").json()["result"]["user"]
		return response
	except Exception as error:
		print(error)
		return None

class SoundCloud:
	def __init__(self):
		self.session = session()
		self.UserAgent = generate_user_agent()
	def download(self, url):
		headers = {
			"Host": "m.soundcloud.com",
			"upgrade-insecure-requests": "1",
			"user-agent": self.UserAgent,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"x-requested-with": "com.instantbits.cast.webvideo",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"accept-encoding": "gzip, deflate, br, zstd",
			"accept-language": "en,ar-AE;q=0.9,ar;q=0.8,en-GB;q=0.7,en-US;q=0.6"
		}
		try:
			self.session.headers.update(headers)
			data = unescape(self.session.get(url).text)
			client_id = findall(r'"clientId":"(.*?)"', data)[0]
			track_authorization = findall(r'"track_authorization":"(.*?)"', data)[0]
			url_data = findall(r"https://.*?/media/(.*?)/(.*?)/stream/hls", data)[0]
		except:
			return {"status": False}
		headers = {
			"Host": "api-mobi.soundcloud.com",
			"Connection": "keep-alive",
			"User-Agent": self.UserAgent,
			"Accept": "*/*",
			"Origin": "https://m.soundcloud.com",
			"X-Requested-With": "com.instantbits.cast.webvideo",
			"Sec-Fetch-Site": "same-site",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Dest": "empty",
			"Referer": "https://m.soundcloud.com/",
			"Accept-Encoding": "gzip, deflate, br, zstd",
			"Accept-Language": "en,ar-AE;q=0.9,ar;q=0.8,en-GB;q=0.7,en-US;q=0.6"
		}
		self.session.headers.update(headers)
		params = {
			"client_id": client_id,
			"track_authorization": track_authorization,
			"stage": ""
		}
		url = f"https://api-mobi.soundcloud.com/media/{url_data[0]}/{url_data[1]}/stream/progressive"
		media = self.session.get(url, params=params).json()["url"]
		return {"status": True,"link": media}

def soundcloud(url):
	sound = SoundCloud()
	return sound.download(url)

#def 

site = "instagram"
site = "tiktok"

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

@app.route("/info_instagram")
def info_user_instagram():
	username = request.args.get("username")
	return info_instagram(username)

@app.route("/reels")
def reelsat():
	url = request.args.get("url")
	site = "reels"
	return reels(url)

@app.route("/post")
def pos():
	url = request.args.get("url")
	return post(url)

@app.route("/postV2")
def posV2():
	id = request.args.get("id")
	return postV2(id)

@app.route("/postV3")
def posV3():
	url = request.args.get("url")
	return postV3(url)

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

@app.route("/pinterestV2")
def pinteressstV2():
	url = request.args.get("url")
	return pinterestV2(url)


@app.route("/tiktok")
def tik():
	url = request.args.get("url")
	site = "tiktok"
	return media(url,site)

@app.route("/tiktokV2")
def tik2():
	url = request.args.get("url")
	return tiktokV2(url)

@app.route("/tiktokV3")
def tik3():
	url = request.args.get("url")
	return tiktokV3(url)

@app.route("/tiktokV4")
def tik4():
	url = request.args.get("url")
	return tiktokV4(url)


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
	return threads(url)


@app.route("/spotify")
def spotif():
	url = request.args.get("url")
	return spotify(url)


@app.route("/facebook")
def facebook():
	url = request.args.get("url")
	link = fb(url)
	return link


@app.route("/soundcloud")
def cound_c():
	url = request.args.get("url")
	site = "SoundCloud"
	return soundcloud(url,site)


if __name__ == "__main__":
	#media.run()
    app.run(host='0.0.0.0', port=8080)
