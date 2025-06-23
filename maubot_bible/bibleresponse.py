class BibleResponse:
    def __init__(self, book, chapter, verse, text, translation=None):
        self.translation = "kjv" if translation is None else translation
        self.book, self.chapter, self.verse, self.text, self.translation = book, chapter, verse, text, translation
        
    def randomVerse(self):
        return f"<b>Random Verse:</b> {self.book} {self.chapter}:{self.verse}<br />{self.text}<br />(Translation: {self.translation})"