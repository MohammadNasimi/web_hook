
from datetime import datetime
from uuid import uuid4

class Base:
    def __init__(self, updated_at:None):
        self.created_at = datetime.now()
        if updated_at is not None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at

class Notes(Base):    
    notes = []
    def __init__(self, title, content, tags:list, history=[], updated_at=None):
        super().__init__(updated_at)
        self.id = str(uuid4())
        self.title = title
        self.content = content
        self.tags = tags
        self.history = history


    def __str__(self):
        return 

    @classmethod
    def list(cls):
        return cls.notes

    @classmethod
    def get(cls,note_id):
        note = next((note for note in cls.notes if note['id'] == note_id), None)
        return note
    
    def create(self):
        new_note = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'history': self.history,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        
        self.notes.append(new_note)
        return new_note
    
    @classmethod
    def update(cls, note_id, new_note:dict):
        for note in cls.notes:
            if note['id'] == note_id:
                old_note = {
                            'title': note["title"],
                            'content': note["content"],
                            'tags': note["tags"],
                        }
                history_note = note["history"]
                print(history_note)
                print(type(history_note)) 
                print(note["history"] + [old_note])

                note["title"] = new_note["title"]
                note["content"] = new_note["content"]
                note["tags"] =  new_note["tags"]
                note["history"] = note["history"] + [old_note]
                note["updated_at"] = datetime.now()
                return True
            
        return False
    
    @classmethod
    def delete(cls,note_id):
        for i, note in enumerate(cls.notes):
            if note['id'] == note_id:
                del cls.notes[i]
                return True
        return note