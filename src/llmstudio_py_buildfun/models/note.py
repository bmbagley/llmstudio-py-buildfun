"""Create model of an individual note from logseq md files."""

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# From llm, builds class of each note, but does not include conversion which may need to be creaated in a utility or something else, not sure of structure yet
# from datetime import datetime
# from pymongo import MongoClient
# from typing import List, Dict
#
# class Note:
#     def __init__(self, note_id: str, content: str, tags: List[str] = None):
#         """
#         Initialize a Note object.
#
#         Args:
#             note_id (str): Unique identifier for the note.
#             content (str): Main text content of the note.
#             tags (List[str], optional): List of tags associated with the note. Defaults to None.
#         """
#         self.note_id = note_id
#         self.content = content
#         self.tags = tags if tags else []
#         self.created_at = datetime.utcnow()  # Auto-set creation timestamp
#
#     @classmethod
#     def from_dict(cls, data: Dict):
#         """Create a Note instance from a dictionary."""
#         return cls(
#             note_id=data.get("note_id"),
#             content=data.get("content"),
#             tags=data.get("tags", [])
#         )
