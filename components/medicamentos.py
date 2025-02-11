from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app

# ====tela de medicamentos

# tabela de medicamentoss
layout = dbc.Col([
    dbc.Row([
        html.Legend('Tabela de Medicamentos'),
        html.Div(id='tabela-medicamento', className='dbc'),
    ], style={'margin-top': '10px'}),

    # grafico de medicamentos
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='grafico-medicamento', style={'margin': '20px'}),
        ], width=9),

        # card do valor de medicamentos
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H3('Medicamentos'),
                    html.Legend("R$ 000,00", id='medicamento-valor-card',
                                style={'font-size': '50px'}),
                    html.H6('Total de Medicamentos'),
                ], style={'text-align': 'center', 'padding-top': '10px'})
            )
        ], width=3)
    ]),
], style={'padding': '10px'}),

# ========CALLBACKS
