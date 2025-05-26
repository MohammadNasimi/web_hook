
from datetime import datetime
from uuid import uuid4
import yaml
import os

class Base:
    def __init__(self, updated_at:None):
        self.created_at = datetime.now()
        if updated_at is not None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at

class Notes(Base):    
    notes = []
    file_path = os.path.join(os.getcwd(), 'web_hook', 'yaml_file', 'notes.yaml')
    _loaded = False
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
    def read_notes_yaml(cls):
        try:
            with open(cls.file_path, 'r') as file:
                data = list(yaml.safe_load_all(file))[0]
        except FileNotFoundError:
            data = []
        return data
    @classmethod
    def write_notes_yaml(cls, notes):
        with open(cls.file_path, 'w') as file:
            yaml.dump(notes, file, 
                    default_flow_style=False,  
                    sort_keys=False,          
                    indent=4)
    

    @classmethod
    def list(cls):
        cls.notes = Notes.read_notes_yaml()
        return cls.notes

    @classmethod
    def get(cls,note_id):
        cls.notes = Notes.read_notes_yaml()
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
        # append in yaml file
        self.notes = Notes.read_notes_yaml()
        self.notes.append(new_note)
        self.write_notes_yaml(self.notes)
        return new_note
    
    @classmethod
    def update(cls, note_id, new_note:dict):
        cls.notes = Notes.read_notes_yaml()
        for note in cls.notes:
            if note['id'] == note_id:
                old_note = {
                            'title': note["title"],
                            'content': note["content"],
                            'tags': note["tags"],
                            'updated_at' :datetime.now()
                        }
                note["title"] = new_note["title"]
                note["content"] = new_note["content"]
                note["tags"] =  new_note["tags"]
                note["history"] = note["history"] + [old_note]
                note["updated_at"] = datetime.now()
                cls.write_notes_yaml(cls.notes)
                return True
        return False
    
    @classmethod
    def delete(cls,note_id):
        cls.notes = Notes.read_notes_yaml()
        for i, note in enumerate(cls.notes):
            if note['id'] == note_id:
                del cls.notes[i]
                cls.write_notes_yaml(cls.notes)
                return True
        return False