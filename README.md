garden.pizza
============

The class Pizza draws a pizza chart.

serie, chart_size, legend_color, legend_title_rayon, legend_value_rayon and
chart_border are properties, they could be changed dynamically.

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
