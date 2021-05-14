import statistics
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output# Load Data

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('Censo2020/Viviendas19.CSV')

CLAVIVP = {
    1: 'Casa',
    2: 'Casa que comparte terreno',
    3: 'Casa dúplex',
    4: 'Departamento',
    5: 'Vecindad',
}


COCINA = {
    1: 'Sí',
    3: 'No'
}

COMBUSTIBLE = {
    1: 'leña o carbón',
    2: 'gas',
    3: 'electricidad',
    4: 'Otro combustible',
    5: 'No cocinan'
}

AGUA_ENTUBADA = {
    1: 'dentro de la vivienda',
    2: 'sólo en el patio o terreno',
    3: 'No tienen agua entubada'
}

ABA_AGUA_ENTU = {
    1: 'del servicio público de agua',
    2: 'de un pozo comunitario',
    3: 'de un pozo particular',
    4: 'de una pipa',
    5: 'de otra vivienda',
    6: 'de la lluvia',
    7: 'de otro lugar'
}

TINACO = {
    1: 'Sí',
    2: 'No'
}

CISTERNA = {
    3: 'Sí',
    4: 'No'
}

BOMBA_AGUA = {
    5: 'Sí',
    6: 'No'
}

REGADERA = {
    7: 'Sí',
    8: 'No'
}

BOILER = {
    1: 'Sí',
    2: 'No'
}

AIRE_ACON = {
    5: 'Sí',
    6: 'No'
}

PANEL_SOLAR = {
    7: 'Sí',
    8: 'No'
}

REFRIGERADOR = {
    1: 'Sí',
    2: 'No'
}

LAVADORA = {
    3: 'Sí',
    4: 'No'
}

HORNO = {
    5: 'Sí',
    6: 'No'
}

TELEVISOR = {
    7: 'Sí',
    8: 'No'
}

COMPUTADORA = {
    1: 'Sí',
    2: 'No'
}

TELEFONO = {
    3: 'Sí',
    4: 'No'
}

INTERNET = {
    7: 'Sí',
    8: 'No'
}

FORMA_ADQUI = {
    1: 'la compró hecha',
    2: 'la mandó construir',
    3: 'la construyó ella (él) misma(o) o familiares',
    4: 'la heredó',
    5: 'la recibió como apoyo del gobierno',
    6: 'La obtuvo de otra manera'
}

FINANCIAMIENTO1 = {
    1: 'INFONAVIT',
    2: 'FOVISSSTE',
    3: 'PEMEX',
    4: 'FONHAPO',
    5: 'un banco',
    6: 'otra institución',
    7: 'Le prestó un familiar, amiga(o) o prestamista',
    8: 'Usó sus propios recursos'
}

DEUDA = {
    1: 'está totalmente pagada',
    2: 'la están pagando',
    3: 'la dejaron de pagar',
    8: 'No sabe'
}

TIPOHOG = {
    1: 'Familia nuclear',
    2: 'Familia ampliada',
    3: 'Familia y conocidos',
    5: 'Unipersonal',
    6: 'Corresidentes'
}

SEXO = {
    1: 'Hombre',
    3: 'Mujer'
}

TAMLOC = {
    1: 'Menos de 2 500 habitantes',
    2: 'De 2 500 a 14 999 habitantes',
    3: 'De 15 000 a 49 999 habitantes',
    4: 'De 50 000 a 99 999 habitantes',
    5: '100 000 y más habitantes'
}

MUN = {
    1: "Abasolo",
    2: "Agualeguas",
    3: "Los Aldamas",
    4: "Allende",
    5: "Anáhuac",
    6: "Apodaca",
    7: "Aramberri",
    8: "Bustamante",
    9: "Cadereyta Jiménez",
    10: "El Carmen",
    11: "Cerralvo",
    12: "Ciénega de Flores",
    13: "China",
    14: "Doctor Arroyo",
    15: "Doctor Coss",
    16: "Doctor González",
    17: "Galeana",
    18: "García",
    19: "San Pedro Garza García",
    20: "General Bravo",
    21: "General Escobedo",
    22: "General Terán",
    23: "General Treviño",
    24: "General Zaragoza",
    25: "General Zuazua",
    26: "Guadalupe",
    27: "Los Herreras",
    28: "Higueras",
    29: "Hualahuises",
    30: "Iturbide",
    31: "Juárez",
    32: "Lampazos de Naranjo",
    33: "Linares",
    34: "Marín",
    35: "Melchor Ocampo",
    36: "Mier y Noriega",
    37: "Mina",
    38: "Montemorelos",
    39: "Monterrey",
    40: "Parás",
    41: "Pesquería",
    42: "Los Ramones",
    43: "Rayones",
    44: "Sabinas Hidalgo",
    45: "Salinas Victoria",
    46: "San Nicolás de los Garza",
    47: "Hidalgo",
    48: "Santa Catarina",
    49: "Santiago",
    50: "Vallecillo",
    51: "Villaldama"
}

PORCENTAJES = {
    6 : 4.8940,
    5 : 2,
    4 : 1,
    3 : 0.4667,
    2 : 0.2667,
    1 : 0.1573
}

intercept = 801547.40
mtsprecio = 625.5
bed = 84512.60
bath= 113268.90

Eco = 296771.15
Pop = 503001.95
Trad = 880253.41
Media =  1886257.30
Res = 3772514.60
Res2 = 10000000

def algoritmo(baño,metro):
        if(max(metro)>0):
            dato = []
            for i in range(0,len(baño)):
                if(metro[i]>0):
                        metrica = baño[i]*metro[i]
                        dato.append(metrica)

            aprox = statistics.mean(dato)

            dato=[]

            for i in range(0,len(baño)):
                    diff = abs(aprox-metro[i])
                    dato.append(diff)

            menor=dato[0]
            posicion=0

            for i in range(0,len(baño)):
                    if(min(dato)>300000):
                        posicion=max(baño)
                    else:
                        if(dato[i]<menor):
                            menor=dato[i]
                            posicion=i+1
            dato = []
            if(metro[posicion]<60):
                posicion = posicion - 1

            dato.append(baño[posicion])
            dato.append(metro[posicion])
            return(dato)
        else:
            aviso = "Te sugerimos considerar menos habitaciones."

def ope (cuarto_value,venta,porc,categoria):
        opcionesbaños=[]
        opcionesmts=[0]
        preciobase = intercept + (cuarto_value*bed)
        while(max(opcionesmts)<=0):
                opcionesmts=[]
                categoria = categoria - 1
                porc = PORCENTAJES[categoria]
                preciorestante = venta - (preciobase*porc)
                for i in range(1,cuarto_value+1):
                    preciorestante = venta - (preciobase*porc)
                    baños = i
                    bañosprecio = (baños*bath*porc)
                    precioconbaño = preciorestante - bañosprecio
                    bañomedio = i+0.5
                    bañosmedioprecio = (bañomedio*bath*porc)
                    precioconbañomedio = preciorestante - bañosmedioprecio
                    metros = round(precioconbaño/(mtsprecio*porc),2)
                    metrosmedio = round(precioconbañomedio/(mtsprecio*porc),2)
                    opcionesbaños.append(baños)
                    opcionesmts.append(metros)
                    opcionesbaños.append(bañomedio)
                    opcionesmts.append(metrosmedio)
        return (opcionesbaños, opcionesmts,preciorestante)


#LAYOUT ---------------------------------------------------------------------------------------------------
app.layout = html.Div(children=[

    html.Div(children=[
        dbc.Row([
        #Primera columna ----- ENTRADAS
           dbc.Col(
                dbc.Form(children=[
                    dbc.FormGroup(
                        [
                            dbc.Label('Tipo de vivienda', className="mr-2"),
                            dbc.Select(id='my-input',
                                                options=[{'label': CLAVIVP[i], 'value': i} for i in CLAVIVP],
                                                value = 1, className="mr-1")
                        ], className="mr-4"),

                    dbc.FormGroup(
                        [
                            dbc.Label('Municipio', className="mr-2"),
                            dbc.Select(id='mun',
                                                options=[{'label': MUN[i], 'value':i} for i in MUN],
                                                 value='',className="mr-1")
                        ], className="mr-3"),

                    dbc.FormGroup(
                        [
                            dbc.Label('Hogar', className="mr-2"),
                            dbc.Select(id='hogar',
                                                options=[{'label': TIPOHOG[i], 'value':i} for i in TIPOHOG],
                                                 value=1,className="mr-1")
                        ], className="mr-3"),

                    dbc.FormGroup(
                    [
                       dbc.Label('Edad', className="mr-2"),
                            dbc.Input(id='edad',
                            placeholder=' ',bs_size="sm",
                            type='number',
                            value='', className="mr-1")
                        ], className="mr-4"),

                    dbc.FormGroup(
                    [
                       dbc.Label('Sexo', className="mr-2"),
                            dbc.RadioItems(id='sexo',
                             options=[{'label': SEXO[i], 'value': i} for i in SEXO],
                            value='', className="mr-1")
                        ], className="mr-4"),

                    dbc.FormGroup(
                    [
                       dbc.Label('Habitaciones', className="mr-2"),
                            dbc.Input(id='cuartos',
                                        placeholder='',bs_size="sm",
                                      type='number',
                                      value='',className="mr-1")
                        ], className="mr-4")

                ],className="mx-auto"),
            width=3, className="mx-auto"),


       #Segunda Columna ---- CONTENIDO
            dbc.Col(children=[
                html.Div(children=[

                #Primer fila -----------------------------------------------------
                    dbc.Row([
                        dbc.CardDeck([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("Ingreso", className="card-title"),
                                        html.P(children=["En este contexto la persona promedio cuenta con un ingreso de $",html.I(id="my-output")],className="card-text"),

                                    ]
                                )
                            ),

                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("Precio", className="card-title"),
                                        html.P(children=["Por otro lado el precio estimado que esta dispuesto a pagar es de $",html.I(id="my-output2")],className="card-text"),

                                    ]
                                )
                            )])
                ]),



                #Segunda fila -----------------------------------------------------
                     dbc.Row([
                        dbc.Col(
                            html.Div(
                        dbc.CardDeck([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("Distribución del ingreso.", className="card-title"),
                                        dcc.Graph(id="graph"),
                                    ]
                                )
                            )]),className="auto-mx")
                         ,width=7),
                        dbc.Col([
                         html.Div([
                            dbc.CardDeck([
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.CardImg(src="assets/baños.png", top=True),
                                            dbc.CardBody([
                                                            html.P(children=["BAÑOS: ",html.B(id="baños")],className="card-text"),
                                            ])
                                        ]
                                    )
                                ),

                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.CardImg(src="assets/metraje.png", top=True),
                                            dbc.CardBody(html.P(["METROS: ",html.B(id="metraje")],className="card-text")),



                                        ]
                                    )
                                )])],className="auto-mx"),
                            html.Div([
                             dbc.CardDeck([
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.CardImg(src="/assets/Picture1.png"),
                                            dbc.CardBody([
                                                            html.P(["HABITACIONES: ",html.B(id="cuarto")],className="card-text"),
                                            ]),

                                        ]
                                    )
                                ),
                                 dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.CardImg(src="/assets/aviso2.png", top=True),
                                            dbc.CardBody([
                                                            html.P(["AVISO: ",html.B(id="aviso")],className="card-text"),
                                            ]),

                                        ]
                                    )
                                )
                            ])
                            ],className="mt-3")
                        ],width=5),

                ],className="mt-4"),




    ]),
],className="mx-auto")
        ])])
])


#FUNCIONES ------------------------------------------------------------------
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='my-output2', component_property='children'),
    Output("graph", "figure"),
    Output(component_id='baños', component_property='children'),
    Output(component_id='metraje', component_property='children'),
    Output(component_id='cuarto', component_property='children'),
    Output(component_id='aviso', component_property='children'),
    Input(component_id='my-input', component_property='value'),
    Input(component_id='mun', component_property='value'),
    Input(component_id='edad', component_property='value'),
    Input(component_id='sexo', component_property='value'),
    Input(component_id='cuartos', component_property='value'),
    Input(component_id='hogar', component_property='value')
)
def update_output_div(input_value,mun_value,edad_value,sexo_value,cuartos_value,hogar_value):
    filtro = df[df.CLAVIVP == int(input_value)]
    if (mun_value != '' and mun_value != None): filtro = filtro[filtro.MUN==int(mun_value)]
    if (edad_value != '' and edad_value != None): filtro = filtro[filtro.JEFE_EDAD.isin([edad_value-2, edad_value+2])]
    if (sexo_value != '' and sexo_value != None): filtro = filtro[filtro.JEFE_SEXO==sexo_value]
    if (cuartos_value != '' and cuartos_value != None): filtro = filtro[filtro.CUADORM==cuartos_value]
    if (hogar_value != '' and hogar_value != None): filtro = filtro[filtro.TIPOHOG==int(hogar_value)]

    if(len(filtro)==0):
        aviso = "Búsqueda demasiado específica, seamos más flexibles."
        ingreso = ''
        venta = ''
        graf = [0]
        fig = px.histogram(graf, nbins=50, range_x=[0,200000])
        bañosOP = ''
        metrajeOP = ''
        cuartos = ''
        return  ingreso,venta,fig,bañosOP,metrajeOP,cuartos
    else:
        graf = filtro['INGTRHOG']
        num = filtro['INGTRHOG'].median()
        num2 = filtro['INGTRHOG'].mean()
        cuartos_prospectados = int(filtro['CUADORM'].median())

        ingreso = (num+num2)/2
        venta = ((ingreso*0.3)*12)*10
        renta = 0.008*venta

        if(venta>Res):
            categoria = 6
            segmento = "Residencial Plus"
            nse = "A/B"
        elif(venta>Media):
            categoria = 5
            segmento = "Residencial"
            nse = "C+"
        elif(venta>Trad):
            categoria = 4
            segmento = "Media"
            nse = "C"
        elif(venta>Pop):
            categoria = 3
            segmento = "Tradicional"
            nse = "C-"
        elif(venta>Eco):
            categoria = 2
            segmento = "Popular"
            nse = "D+"
        else:
            categoria = 1
            segmento = "Económico"
            nse = "D"

        porc = PORCENTAJES[categoria]

        opcionesbaños=[]
        opcionesmts=[]

        if (cuartos_value != '' and cuartos_value != None):
            cuartos = cuartos_value
        else:
            cuartos = cuartos_prospectados

        mtsesperados = int(cuartos) * 100
        opciones = ope(int(cuartos),venta,porc,categoria)


        baños = opciones[0]
        metraje = opciones[1]
        restante = opciones[2]
        pera= algoritmo(baños,metraje)

        if(max(metraje)<=0):
            bañosOP=0
            metrajeOP=0
        else:
            if(pera[1]>400):
                if(cuartos==1):
                    metrajeOP = 150
                elif(cuartos==2):
                    metrajeOP = 200
                elif(cuartos==3):
                    metrajeOP = 250
                else:
                    metrajeOP = 300
                bañosOP = pera[0]
                aviso = "Casa díficil de clasificar"
            else:
                bañosOP = pera[0]
                metrajeOP = pera[1]


        if(metrajeOP > mtsesperados*1.5):
            aviso = "Te sugerimos considerar más habitaciones."
        else:
            aviso = "Parece que todo va bien."


        fig = px.histogram(graf, nbins=50, range_x=[0,200000],color_discrete_sequence=["#e5b0ea"],
                           )

        fig.update_layout(xaxis_title_text='Ingreso', # xaxis label
                           yaxis_title_text='Personas',
                               font=dict(
                                        family="Courier New, monospace",
                                        size=18,
                                        color="White"
                                    ),
                           showlegend=False,

                           paper_bgcolor='rgba(0,0,0,0)',
                           plot_bgcolor='rgba(0,0,0,0)')


        return  '{:20,.2f}'.format(ingreso),'{:20,.2f}'.format(venta),fig,bañosOP,metrajeOP,cuartos,aviso



if __name__ == "__main__":
    app.run_server(debug=True)
