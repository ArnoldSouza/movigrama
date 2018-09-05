#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:11:27 2018

@author: arnold
"""

from bokeh.models import (HoverTool,  # present details in the plot
                          ColumnDataSource,  # specify source
                          Title,  # add title and subtitles
                          DatetimeTickFormatter)  # format datetime axis

import pandas as pd  # manage dataframe
from bokeh.io import show, output_file  # bokeh imports
from bokeh.plotting import figure  # bokeh imports


def assembly_chart(df, complements):
    """function to assembly the chart"""
    print('starting the plot...')

    # specify the output file name
    output_file("movigrama_chart.html")

    # create ColumnDataSource objects directly from Pandas data frames
    source = ColumnDataSource(df)

    # build figure of the plot
    p = figure(x_axis_type='datetime',
               x_axis_label='days of moviment',
               y_axis_label='unities movimented',
               plot_width=1230,
               plot_height=500,
               active_scroll='wheel_zoom')

    # TODO Specify X range (not all plots have 365 days of moviment)

    # build the Stock Level bar
    r1 = p.vbar(x='DT',
                bottom=0,
                top='STOCK',
                width=pd.Timedelta(days=1),
                fill_alpha=0.4,
                color='#99d8c9',
                source=source)

    # build the OUT bar
    p.vbar(x='DT',
           bottom=0,
           top='SOMA_SAI',
           width=pd.Timedelta(days=1),
           fill_alpha=0.8,
           color='crimson',
           source=source)

    # build the IN bar
    p.vbar(x='DT',
           bottom=0,
           top='SOMA_ENTRA',
           width=pd.Timedelta(days=1),
           fill_alpha=0.8,
           color='seagreen',
           source=source)

    # edit title
    # adds warehouse title
    p.add_layout(Title(text=complements['warehouse'],
                       text_font='helvetica',
                       text_font_size='10pt',
                       text_color='orangered',
                       text_alpha=0.5,
                       align='center',
                       text_font_style="italic"), 'above')
    # adds product title
    p.add_layout(Title(text=complements['product'],
                       text_font='helvetica',
                       text_font_size='10pt',
                       text_color='orangered',
                       text_alpha=0.5,
                       align='center',
                       text_font_style="italic"), 'above')
    # adds main title
    p.add_layout(Title(text='Movigrama Endicon',
                       text_font='helvetica',
                       text_font_size='16pt',
                       text_color='orangered',
                       text_alpha=0.9,
                       align='center',
                       text_font_style="bold"), 'above')

    # adapt the range to the plot
    p.x_range.range_padding = 0.1
    p.y_range.range_padding = 0.1

    # format the plot's outline
    p.outline_line_width = 4
    p.outline_line_alpha = 0.1
    p.outline_line_color = 'orangered'

    # format major labels
    p.axis.major_label_text_color = 'gray'
    p.axis.major_label_text_font_style = 'bold'

    # format labels
    p.axis.axis_label_text_color = 'gray'
    p.axis.axis_label_text_font_style = 'bold'

#    p.xgrid.grid_line_color = None  # disable vertical bars
#    p.ygrid.grid_line_color = None  # disable horizontal bars

    # change placement of minor and major ticks in the plot
    p.axis.major_tick_out = 10
    p.axis.minor_tick_in = -3
    p.axis.minor_tick_out = 6
    p.axis.minor_tick_line_color = 'gray'

    # format properly the X datetime axis
    p.xaxis.formatter = DatetimeTickFormatter(
                days=['%d/%m'],
                months=['%m/%Y'],
                years=['%Y'])

    # iniciate hover object
    hover = HoverTool()
    hover.mode = "vline"  # activate hover by vertical line
    hover.tooltips = [("SUM-IN", "@SOMA_ENTRA"),
                      ("SUM-OUT", "@SOMA_SAI"),
                      ("COUNT-IN", "@TRANSACT_ENTRA"),
                      ("COUNT-OUT", "@TRANSACT_SAI"),
                      ("STOCK", "@STOCK"),
                      ("DT", "@DT{%d/%m/%Y}")]
    # use 'datetime' formatter for 'DT' field
    hover.formatters = {"DT": 'datetime'}
    hover.renderers = [r1]  # display tolltip only to one render
    p.add_tools(hover)

    show(p)  # plot action

    print('plot finished')
