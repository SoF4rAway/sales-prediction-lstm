from flask import Blueprint, render_template, request
from lstm.model import model
from lstm.graph import graph
from connection import connect

cursor = connect()

views = Blueprint('views', __name__)

material_1 = 11000329
material_2 = 11000113
material_3 = 11000288

pred_1, actual_1, material_desc_1 = model(material_1, cursor)
graphJSON1 = graph(pred_1, actual_1, material_desc_1)

pred_2, actual_2, material_desc_2 = model(material_2, cursor)
graphJSON2 = graph(pred_2, actual_2, material_desc_2)

pred_3, actual_3, material_desc_3 = model(material_3, cursor)
graphJSON3 = graph(pred_3, actual_3, material_desc_3)

@views.route('/')
def home():
    return render_template('home.html',
                           material_desc_1=material_desc_1,
                           material_desc_2=material_desc_2,
                           material_desc_3=material_desc_3,
                           )

@views.route('/material')
def material    ():
    return render_template('material.html',
                           graphJSON1=graphJSON1,
                           graphJSON2=graphJSON2,
                           graphJSON3=graphJSON3,
                           material_desc_1=material_desc_1,
                           material_desc_2=material_desc_2,
                           material_desc_3=material_desc_3)