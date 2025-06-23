from typing import Optional, Type

from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin, MessageEvent
from maubot.handlers import command
from .bibleresponse import *

import json

class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("baseTrigger")
        helper.copy("baseApi")
        helper.copy("randomPath")

class BibleBot(Plugin):
    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config

    @command.new(name=lambda self: self.config["baseTrigger"],
            help="Request a random Bible verse reference")
    @command.argument("verse", pass_raw=True, required=True)
    async def verse_handler(self, evt: MessageEvent, verse: str) -> None:
        await evt.mark_read()
        
        if(verse == ""):
            await evt.respond(f"This trigger requires at least one parameter")
            return None
        
        if(verse.lower() == "random"):
            url = f"https://{self.config["baseApi"]}/{self.config["randomPath"]}"
        else:
            url = f"https://{self.config["baseApi"]}/{verse}?translation=kjv"
        
        try:
            response = await self.http.get(url)
            resp_json = await response.json()
        except Exception as e:
            await evt.respond(f"request failed: {e.message}")
            return None
            
        try:
            if(verse.lower() == "random"):
                book = resp_json["random_verse"]["book"]
                chapter = resp_json["random_verse"]["chapter"]
                verse = resp_json["random_verse"]["verse"]
                text = resp_json["random_verse"]["text"]
                translation = resp_json["translation"]["name"]
                random = True
            else:
                book = resp_json["verses"][0]["book_name"]
                chapter = resp_json["verses"][0]["chapter"]
                verse = resp_json["verses"][0]["verse"]
                text = resp_json["verses"][0]["text"]
                translation = resp_json["translation_name"]
            
            bibleResponse = BibleResponse(book, chapter, verse, text, translation, random)
            verse_resp = bibleResponse.getVerse()
        except Exception as e:
            await evt.respond("No results, double check that you've chosen a real chapter and verse pairing")
            self.log.exception(e)
            return None
        
        await evt.respond(verse_resp, allow_html=True)
