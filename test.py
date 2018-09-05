from bokeh.io import output_file, show
from bokeh.models import Title
from bokeh.plotting import figure

output_file("test.html")

p = figure(x_range=(0, 5))
p.text(x=[1,2,3], y = [0,0,0], text=['hello\nworld!', 'hello\nworld!', 'hello\nworld!'], angle = 0)

p.add_layout(Title(text="Sub-Title", text_font_style="italic"), 'above')
p.add_layout(Title(text="Title", text_font_size="16pt"), 'above')

show(p)