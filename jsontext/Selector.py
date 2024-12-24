from dataclasses import dataclass
from enum import StrEnum

@dataclass
class KeyOption(StrEnum):
    Advancements= "key.advancements"
    Attack= "key.attack"
    Back= "key.back"
    Chat= "key.chat"
    Command= "key.command"
    Drop= "key.drop"
    Forward= "key.forward"
    Fullscreen= "key.fullscreen"
    Hotbar1= "key.hotbar.1"
    Hotbar2= "key.hotbar.2"
    Hotbar3= "key.hotbar.3"
    Hotbar4= "key.hotbar.4"
    Hotbar5= "key.hotbar.5"
    Hotbar6= "key.hotbar.6"
    Hotbar7= "key.hotbar.7"
    Hotbar8= "key.hotbar.8"
    Hotbar9= "key.hotbar.9"
    Inventory= "key.inventory"
    Jump= "key.jump"
    Left= "key.left"
    LoadToolbarActivator= "key.loadToolbarActivator"
    PickItem= "key.pickItem"
    Playerlist= "key.playerlist"
    Right= "key.right"
    SaveToolbarActivator= "key.saveToolbarActivator"
    Screenshot= "key.screenshot"
    SmoothCamera= "key.smoothCamera"
    Sneak= "key.sneak"
    SpectatorOutlines= "key.spectatorOutlines"
    Sprint= "key.sprint"
    SwapOffhand= "key.swapOffhand"
    TogglePerspective= "key.togglePerspective"
    Use= "key.use"

@dataclass
class Selector:
    def __init__(self):
        pass

@dataclass
class Score(Selector):
    objective: str
    name: str
        
    def __str__(self) -> str:
        return f'"score" : {{"objective":"{self.objective}","name":"{self.name}"}}'
    
@dataclass
class Entity(Selector):
    selector: str 
    seperator: str = ""
    
    def __str__(self) -> str:
        return f'"selector":"{self.selector}","seperator":"{self.seperator}"'
        
@dataclass
class Keybind(Selector):
    key: KeyOption
    
    def __str__(self):
        return f'"keybind":"{self.key}"'