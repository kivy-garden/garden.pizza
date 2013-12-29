#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pizza
=====

The class Pizza displays a pizza chart.

serie, chart_size, legend_color, legend_title_rayon, legend_value_rayon and
chart_border are properties.

Example ::

    pie = Pizza(serie=[
                ["Français", 5, 'a9a9a9'],
                ["Belge", 25, '808080'],
                ["Anglais", 20, '696969'],
                ["Allemand", 30, '778899'],
                ["Italien", 20, '708090']],
                chart_size=256,
                legend_color='ffffcc',
                legend_value_rayon=100,
                legend_title_rayon=160,
                chart_border=2)

'''

__title__ = 'garden.pizza'
__version__ = '0.1'
__author__ = 'julien@hautefeuille.eu'
__all__ = ('Pizza',)

import math
import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex


class Pizza(RelativeLayout):
    '''
    Pizza class

    '''
    serie = ListProperty()
    chart_size = NumericProperty(256)
    legend_color = StringProperty('ffffcc')
    legend_value_rayon = NumericProperty(100)
    legend_title_rayon = NumericProperty(160)
    chart_border = NumericProperty(2)

    def __init__(self, **kwargs):
        super(Pizza, self).__init__(**kwargs)
        self.chart_center = self.chart_size / 2.0
        self.bind(
            pos=self.update_pizza,
            size=self.update_pizza,
            serie=self.update_pizza,
            chart_size=self.update_pizza,
            legend_color=self.update_pizza,
            legend_value_rayon=self.update_pizza,
            legend_title_rayon=self.update_pizza,
            chart_border=self.update_pizza)
        self.bind(
            pos=self.update_label,
            size=self.update_label,
            serie=self.update_label,
            chart_size=self.update_label,
            legend_color=self.update_label,
            legend_value_rayon=self.update_label,
            legend_title_rayon=self.update_label,
            chart_border=self.update_label)

    def update_pizza(self, *args):
        '''
        Draw pizza on canvas

        '''
        with self.canvas:
            self.canvas.clear()
            offset_rotation = 0  # In degrees

            # Fix legend color
            Color(
                get_color_from_hex(self.legend_color)[0],
                get_color_from_hex(self.legend_color)[1],
                get_color_from_hex(self.legend_color)[2], 100)

            # Draw pie chart border circle
            border_circle = Line(circle=(
                self.chart_center,
                self.chart_center,
                self.chart_center),
                width=self.chart_border)

            for title, value, color in self.serie:
                angle = math.radians(((value * 3.6) / 2.0) + offset_rotation)
                title_x_pt = (math.sin(angle)) * self.legend_title_rayon
                title_y_pt = (math.cos(angle)) * self.legend_title_rayon

                # Fix color for each zone
                Color(
                    get_color_from_hex(color)[0],
                    get_color_from_hex(color)[1],
                    get_color_from_hex(color)[2], 100
                )

                # Draw zone animation
                zone = Ellipse(
                    size=(self.chart_size, self.chart_size),
                    segments=value * 3.6,
                    angle_start=offset_rotation,
                    angle_end=offset_rotation + (value * 3.6), t='in_quad'
                )

                # Offset control of each zone, drawing starts on offset
                offset_rotation += value * 3.6

    def update_label(self, *args):
        '''
        Draw legend labels

        '''
        self.clear_widgets()  # Clean widget tree
        offset_rotation = 0  # In degrees

        for title, value, color in self.serie:
            angle = math.radians(((value * 3.6) / 2.0) + offset_rotation)
            value_x_pt = (math.sin(angle)) * self.legend_value_rayon
            value_y_pt = (math.cos(angle)) * self.legend_value_rayon
            title_x_pt = (math.sin(angle)) * self.legend_title_rayon
            title_y_pt = (math.cos(angle)) * self.legend_title_rayon

            # Title
            self.add_widget(Label(
                size_hint=(None, None),
                text="[color=" + self.legend_color + "]" +
                title + "[/color]",
                center_x=self.chart_center + title_x_pt,
                center_y=self.chart_center + title_y_pt,
                markup=True))

            # Value
            self.add_widget(Label(
                size_hint=(None, None),
                text="[color=" + self.legend_color + "]" +
                str(value) + "[/color]",
                center_x=self.chart_center + value_x_pt,
                center_y=self.chart_center + value_y_pt,
                markup=True))

            offset_rotation += value * 3.6


class ChartApp(App):
        """
        Example application

        """
        def build(self):

            from kivy.uix.slider import Slider
            import random

            def test(*args):
                lang_pizza.legend_value_rayon = slider_ray.value
                fruit_pizza.legend_value_rayon = slider_ray.value

            def rand(*args):
                lang = ["Français", "Belge", "Anglais", "Allemand", "Italien"]
                value = [25, 10, 15, 30, 20]
                color = ['a9a9a9', '808080', '696969', '778899', '708090']
                random.shuffle(lang)
                random.shuffle(value)
                random.shuffle(color)
                lang_pizza.serie = zip(lang, value, color)

            layout = GridLayout(cols=2, padding=50)
            lang_pizza = Pizza(serie=[
                ["Français", 5, 'a9a9a9'],
                ["Belge", 25, '808080'],
                ["Anglais", 20, '696969'],
                ["Allemand", 30, '778899'],
                ["Italien", 20, '708090']],
                chart_size=256,
                legend_color='ffffcc',
                legend_value_rayon=100,
                legend_title_rayon=170,
                chart_border=2)

            fruit_pizza = Pizza(serie=[
                ["Pomme", 20, '6495ed'],
                ["Poire", 20, '7b68ee'],
                ["Abricot", 20, '4169e1'],
                ["Prune", 20, '0000ff'],
                ["Ananas", 20, '00008b']],
                chart_size=256,
                legend_color='ffffcc',
                legend_value_rayon=100,
                legend_title_rayon=170,
                chart_border=2)

            slider_v = Slider(min=0, max=300, value=50)
            slider_v.bind(value=rand)

            slider_ray = Slider(min=0, max=250, value=100)
            slider_ray.bind(value=test)

            layout.add_widget(lang_pizza)
            layout.add_widget(fruit_pizza)
            layout.add_widget(slider_v)
            layout.add_widget(slider_ray)

            return layout

if __name__ == '__main__':
    ChartApp().run()
