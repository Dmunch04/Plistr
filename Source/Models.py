from Constants import DataTypes

class DataType:
    def __init__ (self, Object):
        self.Type = DataTypes[type (Object)]

    def __repr__ (self):
        return self.Type

class Value:
    def __init__ (self, Value):
        self.Type = DataType (Value)
        self.Value = Value
        self.DisplayValue = str (Value)

    def __repr__ (self):
        return self.DisplayValue

class Item:
    def __init__ (self, Name, ItemValue):
        self.Name = Name
        self.Type = DataType (ItemValue)
        self.Value = Value (ItemValue)
        self.DisplayValue = str (ItemValue)

    def __str__ (self):
        return f'{self.Name}: {self.Type} -> {self.Value}'
