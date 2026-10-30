from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class DrawingWidget(Widget):
    target_colour_rgb = ListProperty([0, 0, 0])
    target_width_px = NumericProperty(2)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*self.target_colour_rgb)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.target_width_px)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
            return True
        return super().on_touch_move(touch)


class Interface(BoxLayout):
    pass


class DrawingApp(App):
    def build(self):
        return Interface()


if __name__ == '__main__':
    DrawingApp().run()
