import asyncio
import requests
import os
import datetime
import json

sending_queue = asyncio.Queue()

class DiscordEmbed:
    def __init__(self):
        self.embed_data = {}

    def setTitle(self, title: str):
        self.embed_data["title"] = title

    def setDescription(self, desc: str):
        self.embed_data["description"] = desc

    def setUrl(self, url: str):
        self.embed_data["url"] = url

    def applyTimestamp(self, value: bool):
        if value:
            isotime = datetime.datetime.utcnow().isoformat()
            self.embed_data["timestamp"] = str(isotime)
        else:
            del self.embed_data["timestamp"]

    def setColor(self, color: int):
        self.embed_data["color"] = color

    def setFooter(self, text: str, **kwargs):
        footer = {
            "text": text
        }
        if "icon" in kwargs:
            footer["icon_url"] = kwargs["icon"]
        if "proxy" in kwargs:
            footer["proxy_icon_url"] = kwargs["proxy"]
        self.embed_data["footer"] = footer

    def setImage(self, **kwargs):
        image = {}
        if "url" in kwargs:
            image["url"] = kwargs["url"]
        if "proxy" in kwargs:
            image["proxy_url"] = kwargs["proxy"]
        if "height" in kwargs:
            image["height"] = kwargs["height"]
        if "width" in kwargs:
            image["width"] = kwargs["width"]
        self.embed_data["image"] = image

    def setThumbnail(self, **kwargs):
        thumb = {}
        if "url" in kwargs:
            thumb["url"] = kwargs["url"]
        if "proxy" in kwargs:
            thumb["proxy_url"] = kwargs["proxy"]
        if "height" in kwargs:
            thumb["height"] = kwargs["height"]
        if "width" in kwargs:
            thumb["width"] = kwargs["width"]
        self.embed_data["thumbnail"] = thumb

    def setVideo(self, **kwargs):
        video = {}
        if "url" in kwargs:
            video["url"] = kwargs["url"]
        if "height" in kwargs:
            video["height"] = kwargs["height"]
        if "width" in kwargs:
            video["width"] = kwargs["width"]
        self.embed_data["video"] = video

    def setProvider(self, **kwargs):
        prov = {}
        if "name" in kwargs:
            prov["name"] = kwargs["name"]
        if "url" in kwargs:
            prov["url"] = kwargs["url"]
        self.embed_data["provider"] = prov

    def setAuthor(self, **kwargs):
        author = {}
        if "name" in kwargs:
            author["name"] = kwargs["name"]
        if "url" in kwargs:
            author["url"] = kwargs["url"]
        if "icon" in kwargs:
            author["icon_url"] = kwargs["icon"]
        if "proxy" in kwargs:
            author["proxy_icon_url"] = kwargs["proxy"]
        self.embed_data["author"] = author

    def addField(self, name: str, value: str, inline: bool):
        if "fields" not in self.embed_data:
            self.embed_data["fields"] = []
        field = {
            "name": name,
            "value": value,
            "inline": inline
        }
        self.embed_data["fields"].append(field)

    def getData(self):
        return self.embed_data

    def getJSON(self):
        return json.dumps(self.embed_data)

    def __str__(self):
        return self.getJSON()

class WebhookMessage:
    def __init__(self):
        self.form_data = {}

    def setContent(self, msg: str):
        self.form_data["content"] = msg

    def setUsername(self, user: str):
        self.form_data["username"] = user

    def setAvatar(self, url: str):
        self.form_data["avatar_url"] = url

    def setTTS(self, value: bool):
        self.form_data["tts"] = value

    def addEmbed(self, embed: DiscordEmbed):
        if "embeds" not in self.form_data:
            self.form_data["embeds"] = []
        if len(self.form_data["embeds"]) <= 10:
            self.form_data["embeds"].append(embed.getData())
        else:
            print("Embed was discarded. Number of embeds per webhook message must be no more than 10")

    def getData(self):
        return self.form_data

    def getJSON(self):
        return json.dumps(self.form_data)

    def __str__(self):
        return self.getJSON()

class DiscordWebhook:
    def __init__(self, url: str):
        self.url = url

    def setContent(self, data: WebhookMessage):
        self.content = data

    def getContent(self):
        return self.content

    def getUrl(self):
        return self.url

async def webhook_worker_task():
    print("Starting webhook worker task...")
    while True:
        message = await sending_queue.get()
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        ratelimit_lock = True
        while ratelimit_lock:
            req = requests.post(message.getUrl(), headers = header, data = message.getContent().getJSON())
            code = req.status_code
            response_headers = req.headers
            response_body = None
            try:
                response_body = json.loads(req.text)
            except:
                response_body = req.text
            if code == 401:
                ratelimit_lock = False
                print("Discarding webhook request with invalid url")
            elif code == 403:
                ratelimit_lock = False
                print("Webhook request was discarded due to missing permissions\nMessage:" + str(response_body))
            elif code == 429:
                print("Discord ratelimited us. Backing off and retrying after " + str(response_body["retry_after"] / 1000) + " seconds")
                print("Message:" + str(response_body))
                await asyncio.sleep(float(response_body["retry_after"] / 1000))
            else:
                ratelimit_lock = False
        sending_queue.task_done()

