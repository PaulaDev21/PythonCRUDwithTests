class BasicCard:
    def __init__(self, title, content='', related=[]):
        self.title = title
        self.content = content
        self.related = related

    def __str__(self):
        s = f'-----\n{self.title.upper()}\n{self.content}\n-----'
        s += f'\n{len(self.related)} related card(s):\n'
        return s

    def add_related(self, related_cards):
        if isinstance(related_cards, list):
            self.related += related_cards
        else:
            self.related.append(related_cards)

        print(self)


#c1 = BasicCard('test1', 'content1')
#c2 = BasicCard('test2', 'content2')
#print(c1)
#print(c2)
#c1.add_related(c2)
#print(c1)
