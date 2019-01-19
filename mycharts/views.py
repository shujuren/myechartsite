from __future__ import unicode_literals
import math

import pandas as pd
import numpy as np
import random

from django.http import HttpResponse
from django.template import loader

from pyecharts import Line3D, Bar,Boxplot,EffectScatter,Bar3D
from django.shortcuts import render

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def abc(request):
    return render(request, 'index.html')

def index(request):
    template = loader.get_template('mychars/index.html')
    tu = mybar1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def mybar1(request):
    template = loader.get_template('mychars/mybar1.html')
    tu = mybar1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def mybar1_fun():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar: Bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2, is_convert=True)
    return bar


def mybar2(request):
    template = loader.get_template('mychars/mybar2.html')
    tu = mybar2_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def mybar2_fun():
    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - slider 示例")
    bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
    return bar


def mybar3(request):
    template = loader.get_template('mychars/mybar3.html')
    tu = mybar3_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def mybar3_fun():
    days = ["{}天".format(i) for i in range(30)]
    days_v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - xaxis/yaxis 示例")
    bar.add(
        "",
        days,
        days_v1,
        # 默认为 X 轴，横向
        is_datazoom_show=True,
        datazoom_type="slider",
        datazoom_range=[10, 25],
        # 新增额外的 dataZoom 控制条，纵向
        is_datazoom_extra_show=True,
        datazoom_extra_type="slider",
        datazoom_extra_range=[10, 25],
        is_toolbox_show=False,
    )
    return bar


def boxplot1(request):
    template = loader.get_template('mychars/boxplot1.html')
    tu = boxplot1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def boxplot1_fun():
    boxplot = Boxplot("箱形图")
    x_axis = ['expr1', 'expr2', 'expr3', 'expr4', 'expr5']
    y_axis = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
         1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
         830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
        [880, 880, 880, 860, 720, 720, 620, 860, 970, 950,
         880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
         910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
         870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
    ]
    _yaxis = boxplot.prepare_data(y_axis)  # 转换数据
    boxplot.add("boxplot", x_axis, _yaxis)
    return boxplot


def Scatter1(request):
    template = loader.get_template('mychars/Scatter1.html')
    tu = Scatter1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def Scatter1_fun():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [25, 20, 15, 10, 60, 33]
    es = EffectScatter("动态散点图示例")
    es.add("effectScatter", v1, v2)
    return es


def barpandas(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = barpandas_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def barpandas_fun():
    title = "bar demo"
    index = pd.date_range('3/8/2017', periods=6, freq='M')
    df1 = pd.DataFrame(np.random.randn(6), index=index)
    df2 = pd.DataFrame(np.random.randn(6), index=index)

    dtvalue1 = [i[0] for i in df1.values]
    dtvalue2 = [i[0] for i in df2.values]
    index1 = [i for i in df1.index.format()]

    bar = Bar(title, "bar demo 的啊")
    bar.add('xxx', index1, dtvalue1)
    bar.add('yyy', index1, dtvalue2)
    return bar


def barpandas1(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = barpandas1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def barpandas1_fun():
    title = "pandas1"
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

    df1 = pd.DataFrame(df['A'])
    df2 = pd.DataFrame(df['B'])

    dtvalue1 = [i[0] * 10 for i in df1.values]
    dtvalue2 = [i[0] * 10 for i in df2.values]
    index1 = [i for i in df.index.format()]

    bar = Bar(title, "pandas1")
    bar.add('xxx', index1, dtvalue1)
    bar.add('yyy', index1, dtvalue2)
    return bar


def barpandas2(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = barpandas2_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def barpandas2_fun():
    title = "Height For Class"
    df = pd.DataFrame(pd.read_csv('mycharts/class.csv', encoding='gbk', header=0))

    df1 = pd.DataFrame(df['Height'])
    df2 = pd.DataFrame(df['Name'])

    dtvalue1 = [i[0] for i in df1.values]

    index1 = [i[0] for i in df2.values.tolist()]

    bar = Bar(title, "Height For Class")
    bar.add('Height', index1, dtvalue1)
    return bar


def boxplotpandas(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = boxplotpandas_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def boxplotpandas_fun():
    boxplot = Boxplot("箱形图")

    df = pd.DataFrame(pd.read_csv('mycharts/class.csv', encoding='gbk', header=0))

    df1 = pd.DataFrame(df['Height'])
    df2 = pd.DataFrame(df['Weight'])

    dtvalue1 = [i[0] for i in df1.values]
    dtvalue2 = [i[0] for i in df2.values]

    x_axis = ['身高', '体重']
    y_axis = [dtvalue1, dtvalue2]

    _yaxis = boxplot.prepare_data(y_axis)  # 转换数据
    boxplot.add("箱形图", x_axis, _yaxis)
    return boxplot


def boxplotpandas1(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = boxplotpandas1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def boxplotpandas1_fun():
    boxplot = Boxplot("箱形图")

    df = pd.DataFrame(pd.read_csv('mycharts/class.csv', encoding='gbk', header=0))
    df1 = df[df["Sex"] == "女"]
    df2 = df[df["Sex"] == "男"]

    dtvalue11 = df1['Height'].values.tolist()
    dtvalue12 = df1['Weight'].values.tolist()

    dtvalue21 = df2['Height'].values.tolist()
    dtvalue22 = df2['Weight'].values.tolist()

    x_axis = ['Height', 'Weight']
    y_axis1 = [dtvalue11, dtvalue12]
    y_axis2 = [dtvalue21, dtvalue22]

    boxplot.add("女学生", x_axis, boxplot.prepare_data(y_axis1))
    boxplot.add("男学生", x_axis, boxplot.prepare_data(y_axis2))
    return boxplot


def Scatter2(request):
    template = loader.get_template('mychars/mypage1.html')
    tu = Scatter2_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def Scatter2_fun():
    df = pd.DataFrame(pd.read_csv('mycharts/class.csv', encoding='gbk', header=0))
    df1 = df[df["Sex"] == "女"]

    dtvalue11 = df1['Height'].values.tolist()
    dtvalue12 = df1['Weight'].values.tolist()

    es = EffectScatter("女生体重身高分布图")
    es.add(
        "",
        [dtvalue11[0]],
        [dtvalue12[0]],
        symbol_size=20,
        effect_scale=3.5,
        effect_period=3,
        symbol="pin",
    )
    es.add(
        "",
        [dtvalue11[1]],
        [dtvalue12[1]],
        symbol_size=12,
        effect_scale=4.5,
        effect_period=4,
        symbol="rect",
    )
    es.add(
        "",
        [dtvalue11[2]],
        [dtvalue12[2]],
        symbol_size=30,
        effect_scale=5.5,
        effect_period=5,
        symbol="roundRect",
    )
    es.add(
        "",
        [dtvalue11[3]],
        [dtvalue12[3]],
        symbol_size=10,
        effect_scale=6.5,
        effect_brushtype="fill",
        symbol="diamond",
    )
    es.add(
        "",
        [dtvalue11[4]],
        [dtvalue12[4]],
        symbol_size=16,
        effect_scale=5.5,
        effect_period=3,
        symbol="arrow",
    )
    es.add(
        "",
        [dtvalue11[5]],
        [dtvalue12[5]],
        symbol_size=6,
        effect_scale=2.5,
        effect_period=3,
        symbol="triangle",
    )
    return es


def threeD1(request):
    template = loader.get_template('mychars/threeD1.html')
    tu = threeD1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def threeD1_fun():
    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]

    df = pd.read_csv("mycharts/abc.csv")
    data = df.values.tolist()

    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add(
        "",
        x_axis,
        y_axis,
        [[d[1], d[0], d[2]] for d in data],
        is_visualmap=True,
        visual_range=[0, 20],
        visual_range_color=range_color,
        grid3d_width=200,
        grid3d_depth=80,
    )
    return bar3d


def line3d(request):
    template = loader.get_template('mychars/pyecharts.html')
    l3d = fun_line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host=REMOTE_HOST,
        script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def fun_line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    myline3d = Line3D("3D line plot demo", width=1200, height=600)
    myline3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return myline3d