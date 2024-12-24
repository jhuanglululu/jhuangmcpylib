from dataclasses import dataclass
from typing import Union
from enum import StrEnum
from copy import deepcopy

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

class ClickEventOption(StrEnum):
    URL = "open_url"
    RUN = "run_command"
    SUGGEST = "suggest_command"
    COPY = "copy_to_clipboard"
    
class HoverEventOption(StrEnum):
    TEXT = "show_text"
    
@dataclass
class ClickEvent:
    value: str
    action: ClickEventOption = ClickEventOption.RUN
    
    def __str__(self) -> str:
        return f'{{"action":"{self.action}","value":"{self.value}"}}'
        
@dataclass
class HoverEvent:
    content: Union[str, 'Text', 'TextList']
    action: HoverEventOption = HoverEventOption.TEXT
    
    def __str__(self) -> str:
        if type(self.content) is str:
            return f'{{"action":"{self.action}","contents":"{self.content}"}}'
        return f'{{"action":"{self.action}","contents":{str(self.content)}}}'

class Color(StrEnum):
    WHITE = "white"
    BLACK = "black"
    GRAY = "gray"
    GOLD = "gold"
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    GREEN = "green"
    AQUA = "aqua"
    LIGHT_PURPLE = "light_purple"
    DARK_GRAY = "dark_gray"
    DARK_BLUE = "dark_blue"
    DARK_GREEN = "dark_green"
    DARK_AQUA = "dark_aqua"
    DARK_RED = "dark_red"
    DARK_PURPLE = "dark_purple"

@dataclass
class Text:
    content: str | Selector
    color: Color = None
    bold: bool = None
    italic: bool = None
    underlined: bool = None
    strikethrough: bool = None
    clickevent: ClickEvent = None
    hoverevent: HoverEvent = None
    
    def __str__(self) -> str:
        result: str
        if type(self.content) is str:
            result = f'"text":"{self.content}"'
        else:
            result = str(self.content)
        if self.color is not None:
            result += f',"color":"{self.color}"'
        if self.bold is not None:
            result += f',"bold":{str(self.bold).lower()}'
        if self.italic is not None:
            result += f',"italic":{str(self.italic).lower()}'
        if self.underlined is not None:
            result += f',"underlined":{str(self.underlined).lower()}'
        if self.strikethrough is not None:
            result += f',"strikethrough":{str(self.strikethrough).lower()}'
        if self.clickevent is not None:
            result += f',"clickEvent":{str(self.clickevent)}'
        if self.hoverevent is not None:
            result += f',"hoverEvent":{str(self.hoverevent)}'
            
        return f'{{{result}}}'

@dataclass
class TextList:
    texts: list[Union[Text, 'TextList']] = None
    
    def __init__(self, texts: list[Union[Text, 'TextList']]) -> None:
        self.texts = texts.copy()
    
    def __str__(self) -> str:
        return f'[{",".join(map(str, self.texts))}]'
    
    def append(self, text: Union[Text, 'TextList']) -> None:
        self.texts.append(deepcopy(text))
        
    def extend(self, texts: list[Union[Text, 'TextList']]) -> None:
        self.texts.extend(texts.copy())