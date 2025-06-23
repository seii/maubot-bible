from typing import Optional, Type

from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin, MessageEvent
from maubot.handlers import command
from bibleresponse import BibleResponse

import json

class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("randomTrigger")
        helper.copy("baseApi")
        helper.copy("randomPath")

class BibleBot(Plugin):
    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config

    @command.new(name=lambda self: self.config["randomTrigger"],
            help="Request a random Bible verse reference")
    async def random_verse_handler(self, evt: MessageEvent) -> None:
        await evt.mark_read()
        
        url = f"https://{self.config["baseApi"]}/{self.config["randomPath"]}"
        
        try:
            response = await self.http.get(url, headers=headers)
            resp_json = await response.json()
        except Exception as e:
            await evt.respond(f"request failed: {e.message}")
            return None
        try:
            book = resp_json["random_verse"]["book"]
            chapter = resp_json["random_verse"]["chapter"]
            verse = resp_json["random_verse"]["verse"]
            text = resp_json["random_verse"]["text"]
            translation = resp_json["translation"]["name"]
            bibleResponse = BibleResponse(book, chapter, verse, text, translation)
            verse_resp = bibleResponse.randomVerse()
        except Exception as e:
            await evt.respond("No results, double check that you've chosen a real currency pair")
            self.log.exception(e)
            return None
        
        await evt.respond(verse_resp, allow_html=True)
