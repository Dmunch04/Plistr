from tkinter import *
from tkinter import ttk

class Window:
    def __init__ (self, Filename):
        self.Filename = Filename
        self.Title = f'Plistr (1.0) - {self.Filename}'

        self.Root = Tk ()
        self.Root.title (self.Title)

        self.Tree = ttk.Treeview (self.Root)

        self.Tree['columns'] = ('one', 'two')
        self.Tree.column ('#0', width = 270, minwidth = 270, stretch = NO)
        self.Tree.column ('one', width = 150, minwidth = 150, stretch = NO)
        self.Tree.column ('two', width = 400, minwidth = 400)
        self.Tree.heading ('#0', text = 'Name', anchor = W)
        self.Tree.heading ('one', text = 'Type', anchor = W)
        self.Tree.heading ('two', text = 'Value', anchor = W)
        self.ItemsHolder = self.Tree.insert ('', 1, text = 'Items', values = ('Dictionary', ''))

    def Run (self, Items):
        Index = 2

        for Item in Items:
            if Item.Type.Type == 'Array':
                ArrayHolder = self.Tree.insert (self.ItemsHolder, Index, text = Item.Name, values = (Item.Type, ''))
                NewIndex = 1

                for Value in Item.Value.Value:
                    self.Tree.insert (ArrayHolder, NewIndex, text = f'Item{str (NewIndex)}', values = (Value.Type, Value.Value))

                    NewIndex += 1

            elif Item.Type.Type == 'Dictionary':
                DictionaryHolder = self.Tree.insert (self.ItemsHolder, Index, text = Item.Name, values = (Item.Type, ''))
                NewIndex = 1

                for Value in Item.Value.Value:
                    self.Tree.insert (DictionaryHolder, NewIndex, text = Value.Name, values = (Value.Type, Value.Value))

                    NewIndex += 1

            else:
                self.Tree.insert (self.ItemsHolder, Index, text = Item.Name, values = (Item.Type, Item.Value))

            Index += 1

        self.Tree.pack (side = TOP, fill = X)
        self.Root.mainloop ()
