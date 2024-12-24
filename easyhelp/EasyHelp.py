from jhuangmcpylib.jsontext.Text import Text, TextList, Color, HoverEvent, ClickEvent, ClickEventOption
from jhuangmcpylib.jsontext.Selector import Keybind

from dataclasses import dataclass
from typing import TypedDict

NEXTLINE = Text("\\n")

@dataclass
class Variable:
    name: str
    description: str
    
    def formatTextList(self) -> TextList:
        return TextList([
            NEXTLINE,
            Text("⋆ ", Color.GRAY, False, False, False),
            Text(self.name, Color.YELLOW),
            Text(f': {self.description}', Color.WHITE)
        ])

@dataclass
class Command:
    name: str
    command: str
    description: str
    variables: list[Variable] = None
    
    def formatTextList(self) -> TextList:
        
        if self.variables is not None:
            descriptionText = Text(f': {self.description}', Color.WHITE,
                    hoverevent=HoverEvent(content=TextList([
                        Text("Variables: ", Color.GOLD),
                        TextList([ variable.formatTextList() for variable in self.variables ])
                    ])))
        else:
            descriptionText = Text(f': {self.description}', Color.WHITE)
        
        return TextList([
            Text("? ", Color.GRAY, False, False, False),
            Text(self.name, Color.GREEN,
                hoverevent=HoverEvent(content="Click to select"),
                clickevent=ClickEvent(action=ClickEventOption.SUGGEST, value=self.command)),
            descriptionText,
            NEXTLINE
        ])

@dataclass
class Key:
    keybind: list[Keybind]
    description: str
    
    def formatKey(self) -> TextList:
        result: list[Text]
        
        for i, k in enumerate(self.keybind):
            if i == 0:
                result = [Text(k, Color.GREEN)]
            else:
                result.append(Text(" + ", Color.WHITE))
                result.append(Text(k, Color.GREEN))
        
        return TextList(result)
    
    def formatTextList(self) -> TextList:
        return TextList([
            Text("? ", Color.GRAY, False, False, False),
            self.formatKey(),
            Text(f": {self.description}", Color.WHITE),
            NEXTLINE
        ])

@dataclass
class EasyHelp:
    header: Text | TextList
    footer: Text | TextList
    description: Text | TextList = None
    commands: list[Command] = None
    keys: list[Key] = None 
    
    def __str__(self) -> str:
        
        result = TextList([NEXTLINE, self.header, NEXTLINE, NEXTLINE])
        
        if self.description is not None:
            result.extend([self.description, NEXTLINE, NEXTLINE])
        
        if self.commands is not None:
            result.extend([TextList([
                Text("Commands", Color.GOLD),
                NEXTLINE,
                TextList([ command.formatTextList() for command in self.commands ])
            ]), NEXTLINE])
        
        if self.keys is not None:
            result.extend([TextList([
                Text("Keys", Color.GOLD),
                NEXTLINE,
                TextList([ key.formatTextList() for key in self.keys ])
            ]), NEXTLINE])
        
        result.append(self.footer)
        return str(result)