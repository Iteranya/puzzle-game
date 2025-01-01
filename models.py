from dataclasses import dataclass


@dataclass
class CardItem:
    id: str
    name: str  
    image_file:str
    sound_file:str
    revealed: bool = False

@dataclass
class StageItem:
    id:str
    name:str
    description:str
