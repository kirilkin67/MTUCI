from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Triangle, BoxShadow
from random import random, randint

Window.size = (500, 800)


def box_shadow(pos, size):
    Color(0, 0, 0, 0.65)

    # return BoxShadow(insert=True, pos=pos, size=size, offset=(0.0, 0.0), blur_radius=10.0,
    #                  spread_radius=(-10.0, -10.0), border_radius=(10.0, 10.0, 10, 10))
    return BoxShadow(insert=True, pos=pos, size=size, blur_radius=20.0,
                     spread_radius=(-10.0, -10.0))


def draw_disk(touch):
    base_size = randint(50, 200)
    size = (base_size, base_size)
    pos = (touch.x - base_size / 2, touch.y - base_size / 2)
    Ellipse(pos=pos, size=size)


def draw_ellipse(touch):
    size = (randint(50, 200), randint(50, 200))
    pos = (touch.x - size[0] / 2, touch.y - size[1] / 2)
    Ellipse(pos=pos, size=size)


def draw_rectangle(touch):
    size = (randint(50, 200), randint(50, 200))
    pos = (touch.x - size[0] / 2, touch.y - size[1] / 2)
    Rectangle(pos=pos, size=size)


def draw_square(touch):
    base_size = randint(50, 200)
    size = (base_size, base_size)
    pos = (touch.x - base_size / 2, touch.y - base_size / 2)
    Rectangle(pos=pos, size=size)


class DrawWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            # очистка холста
            self.canvas.clear()
            color = (random(), random(), random(), 1)
            shape = random()
            Color(*color)
            if shape < 0.2:
                draw_ellipse(touch)
            elif shape < 0.4:
                draw_disk(touch)
            elif shape < 0.6:
                draw_rectangle(touch)
            elif shape < 0.8:
                draw_square(touch)
            else:
                size = (randint(50, 200), randint(50, 200))
                Triangle(
                    points=[touch.x - size[0] / 2, touch.y - size[1] / 2, touch.x + size[0] / 2, touch.y - size[1] / 2,
                            touch.x, touch.y + size[1] / 2])


class Draw(App):
    def build(self):
        parent = BoxLayout()
        widget = DrawWidget()
        parent.add_widget(widget)
        return parent


if __name__ == '__main__':
    Draw().run()
