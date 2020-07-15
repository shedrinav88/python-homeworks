class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing!')


class Pen(Stationery):
    def draw(self):
        print('Start writing!')


class Pencil(Stationery):
    def draw(self):
        print('Start sketching!')


class Handle(Stationery):
    def draw(self):
        print('Start writing with handle!')


st = Stationery('brush')
st.draw()

pen = Pen('Parker')
pen.draw()

penc = Pencil('Krause')
penc.draw()

handle = Handle('Turtle')
handle.draw()

