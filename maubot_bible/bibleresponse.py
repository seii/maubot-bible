class BibleResponse:
    def __init__(self, book, chapter, verse, text, translation=None, random=None):
        self.translation = "kjv" if translation is None else translation
        self.random = false if random is None else random
        self.book, self.chapter, self.verse, self.text, self.translation = book, chapter, verse, text, translation
        
    def getVerse(self):
        if(random):
            return f"<b>Random Verse:</b> {self.book} {self.chapter}:{self.verse}<br />{self.text}<br />(Translation: {self.translation})"
        else:
            return f"You asked for: <b>{self.book} {self.chapter}:{self.verse}:</b><br />{self.text}<br />(Translation: {self.translation})"