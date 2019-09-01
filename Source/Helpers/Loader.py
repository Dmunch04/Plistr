import plistlib

import Models
from Constants import DataTypes

def LoadFile (FileName) -> list:
    with open (FileName, 'rb') as Source:
        Data = plistlib.load (Source)

    return LoadValues (Data)

def LoadValues (Values) -> list:
    Items = []
    for Item in Values:
        Dict = False
        Value = Values[Item]
        DataType = DataTypes[type (Value)]

        if isinstance (Value, list):
            NewValue = []
            for ItemValue in Value:
                NewValue.append (Models.Value (ItemValue))

            Value = NewValue

        elif isinstance (Value, dict):
            Dict = True
            Value = LoadValues (Value)

        print (f'{Item}: {DataType} -> {Value}')
        Items.append (Models.Item (Item, Value))

        if Dict:
            Items[-1].Type = Models.DataType ({})

    return Items
