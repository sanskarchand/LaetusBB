from dataclasses import dataclass, field
from typing import Tuple

@dataclass
class Tag:
    tag: str
    attribs: Tuple[str] = field(default=())

TAG_LIST = [
    Tag("i"), Tag("b"), Tag("u"),
    Tag("color", ["value"]),
    Tag("code"),
    Tag("emoticon"),    # I loathe false positives
]


def parse_bbcode(bbcode_text):
    pass    
