# v0.2.2.4 7 dic 2020 17:01 71220201701
#   v.0.2.2.4-71220201701
# changelog
#
# 1. limpieza minima de codigo viejo (presets eliminados)
# 2. preparacion para implementacion de argumentos por linea de comandos
# formato esperado> -monto -data_fci -data_bp -graficar
# 3. prearmado de funcion para argv


import pkg_resources
#import os           # para funcion futura desde terminal, se usara para poder ejecutar pip
#import sys
#import getopt, sys     # para futura implementacion con argumentos
#from sys import argv   # argv se usara para leer los argumentos que se den por linea de comandos

class col: #sin module
    R = '\033[31m'          # ROJO
    G = '\033[32m'          # VERDE

def Reset():
    workaround = '\033[m' #RESET COLORES. lo mismo que cuando usaba colorama y termcolor en el otro pj
    print(workaround)

class mensaje:
    reqdiag = 'Diagnostico de requisitos'
    runpip = "EJECUTAR pip install -r requeriments.txt\n"
    separador = "==========================================="
    plottitle = "Calculadora de TASAS version alpha"
    insamount = "Ingrese el monto a invertir:"
    montoenmem = "Monto ingresado: $"
    daygain = "\nGanancia a las 24 hs: $"
    fehgain = "\nGanancia a las 48 hs: $"
    weekgain = "\nGanancia a la primer semana: $"
    monthgain = "\nGanancia al primer mes: $"
    gainof = "ganancia de:"
    plotinout = "Importe/Ganancia"
    plottime = "Meses/Tiempo"
    

#comprobacion de modulos BETA
for package in ['matplotlib']:
    try:
        dist = pkg_resources.get_distribution(package)
        #print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print(mensaje.reqdiag)
        print('{} NO se encuentra instalado'.format(package)) 
for package in ['matplotlib']:
    try:
        dist = pkg_resources.get_distribution(package)
        #print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print(mensaje.runpip)
        print (mensaje.separador)
        #print('Ejecutar comando?')
    pass

try:
    import matplotlib.pyplot as ploteame
except:
    pass



class error:
    nofloat = 'no se aceptan flotantes.'
    notanumber = "NO es un numero."
    onlyposint = "NO es un numero válido\n(No se toman ni string, ni flotantes ni negativos"

# VARIABLES
a = 1
b = 13
c = 30
perdida = 2 # porcentaje
perdida_final = 0 # restar al final, es lo que retiene la entidad bancaria por cada operacion diaria

Flag_Set = 0

''' Primera Tasa fue de 23,95 
despues aumentó un 0.66 a 24.61
y después aumentó otro 0.96 a 25.57
tener en cuenta que esta tasa es ANUAL

la fluctuación total es la suma del total de los aumentos dados
se la añade a la primera tasa

en caso de haber una diferencia negativa, se la debe sumar por ejemplo 
0.96 + (-0.20) = 0.76, siendo 0.76 la nueva fluct total
'''
tasa = 23.95 # UALA
'''
HACER UNA FUNCION QUE CALCULE LA TASA EN PERIODOS DE 30 DIAS
POR EJEMPLO

#INGRESO 
plazo_fijo_ganancia_mensual = ingreso * (tasa_plazo_fijo / 100) / 12

'''
tasa_plazo_fijo = 37 # BANCO PROVINCIA
fluct = 0.66 # basado en aumento a 24.61
fluct2 = 0.96 # basado en aumento a 25,57
fluct3 = 0.4 # basado en aumento a 25.97
fluct_total = fluct + fluct2 + fluct3
tasa += fluct_total
total = 1 # workaround
final = 1 # workaround
resultado = [] # workaround
buffer_exit = "$"

data_fci = []
data_bp = []
''' presets eliminados en v.0.2.2.4-71220201642 '''

plot_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # MESES, EJE X    # OK - ESCALA CHEQUEADA
plot_scale_daily = [] # llenar con una funcion      # OK

fmt1 = 'b--'
fmt2 = 'g-.'

def Graficar_Proyecciones(data_fci, data_bp, escala, eje_st, eje_lim):   # OK - CHEQUEADO
    ploteame.title(mensaje.plottitle)
    ploteame.plot(escala,data_fci, fmt1,
                  escala,data_bp, fmt2)
    ploteame.grid(True)
    ploteame.xlim(eje_st, eje_lim)                                    # ALTERNATIVA A MODIFICAR AXIS, PERMITE MANTENER VALOR Y SEGUN REGISTRO
    ploteame.ylabel(mensaje.plotinout)
    ploteame.xlabel(mensaje.plottime)
    ploteame.legend(['FCI', 'BP'])                          # ALTERNATIVA A APLICAR EL LABEL EN EL PLOT, PERMITE MANTENER LA SINTAXIS, X1 Y X2
    ploteame.show()


def GenerarMes(dia_inicial, dia_final):                     # FUNCION PARA GENERAR LISTA CON DIAS DEL MES
    global plot_scale_daily
    plot_scale_daily = []
    for i in range(dia_inicial, dia_final):
        plot_scale_daily.append(i)
        i += 1

def Setear_Flag(flag):                                      # OK
    global Flag_Set
    '''
1 = FCI
2 = BP
0 = NO USAR
'''
    Flag_Set = flag

def Agregar_A_Lista(total_mensual, data_fci, data_bp):                         # OK
    global Flag_Set
    #global data_fci
    #global data_bp
    if Flag_Set == 1:
        total_mensual = float(total_mensual)
        data_fci.append(total_mensual)
    elif Flag_Set == 2:
        total_mensual = float(total_mensual)
        data_bp.append(total_mensual)
    else:
        pass


while True:
    ingreso = input(mensaje.insamount)
    ingreso_inicial = ingreso # se almacena el ingreso para evitar que luego
                              # se haga un calculo con ingreso y los meses
                              # queden con la variable ingreso ya procesada
    try:
        ingreso = float(ingreso)
        ingreso_inicial = float(ingreso_inicial)
        break
    except ValueError:
        print(error.notanumber)
            
    
def Calcular_Inversion(ingreso, tasa):
    global total
    global final
    #Fluctuar_Tasa()
    calc_inv = ingreso * (tasa / 100) / 12 / 30 # a la tasa se la debe dividir en 12 meses, luego un wa de 30 dias
    #print("Debug: ", calc_inv)
    calc_inve = calc_inv * c # multiplico por dias ## SE USABA EN VERSION ANTERIOR SIN FINES DE SEMANA
    final = float(calc_inve) - (float(calc_inve) * (perdida / 100)) - perdida_final # ganancia diaria pero la toma como final?
    total = ingreso + final # ganancia neta
    #print("Debug: ", final, total)

def Clear_Numeros():
    global buffer_exit
    for k in range(len(buffer_exit)):
        char = buffer_exit[k]
        resultado.append(char)    
    del resultado[9:]
    final = 0
    total = 0
    calc_inv = 0
    calc_inve = 0
    total_mensual = 0
    perdida = 0
    ingreso = ingreso_inicial
    
    #print("VALOR ACTUAL: ",
    #      "resultado: ", resultado,
    #      "final: ", final,
    #      "total: ", total,
    #      "calc_inv: ", calc_inv,
    #      "calc_inve: ", calc_inve,
    #      "total_mensual: ", total_mensual,
    #      "perdida: ", perdida,
    #      "ingreso: ", ingreso, "\n")

def Clear_Listas():
    data_fci.clear()
    data_fci.clear()
    #data_fci_preset.clear()
    #data_bp_preset.clear()

def nGanancia_Diaria(dia_inicial, dia_final, ingreso, tasa):     # incomplete
    #print(plot_scale_daily)                        # TEST LISTA            #      OK
    ''' FALTA FUNCION QUE HAGA UN PLOTEO Y GENERE UNA LISTA DE MANERA SIMILAR A ANUAL
    PERO DE FORMA DIARIA ASI SE PUEDE OBTENER UN RESULTADO DIA A DIA
    SE DEBE USAR PLOT_SCALE_DAILY COMO EJE DE ESCALA.
    ES POSIBLE QUE REQUIERA UNA MODIFICACION EN XLIM DE ACUERDO AL PRIMER Y ULTIMO
    REGISTRO DE LA LISTA GENERADA. 
    '''
    #print(dia_inicial, dia_final)
    for i in range(dia_inicial, dia_final):
        global buffer_dia
        global buffer_dexit
        global resultado_diario
        Calcular_Inversion(ingreso, tasa)
        total_mensual = total
        ingreso = total_mensual

        Agregar_A_Lista(total_mensual, data_fci_daily, data_bp_daily)

        buffer_dia=[]
        buffer_dia.append(total_mensual/dia_final)
        buffer_dexit = "$"
        datand = ""
        for datand in buffer_dia: # este FOR es el que se encarga de armar cada cosa
            buffer_dexit += str(datand/dia_final)
            
        print("dia", i, mensaje.gainof, buffer_dexit)
        buffer_dia.clear
        
        i += 1
        
    
    

def nGanancia_Anual(ingreso, tasa): # corregir dias de fin de semana (excluirlos)
    for i in range(a, b):
        #global ingreso
        global buffer
        global buffer_exit
        global resultado
        # calcular ganancia 
        # Calcular_Inversion()
        # poner la ganacia junto al valor anterior en una variable
        Calcular_Inversion(ingreso, tasa)
        total_mensual = total #+ final
        ingreso = total_mensual
        
        Agregar_A_Lista(total_mensual, data_fci, data_bp)
        
        
        ''' DEBUG DE REGISTRO '''
        ##print("DATA FCI: ", data_fci)
        ##print("DATA_BP: ", data_bp)
        # print("datos del registro lista de fci: \n", data_fci)
        
        
        # mostrar el valor en cada instancia
        #print(final)
        buffer=[]
        # print("registro de buffer: ", buffer)
        buffer.append(total_mensual)
        buffer_exit = "$"
        datan = ""
        for datan in buffer: # este FOR es el que se encarga de armar cada cosa
            buffer_exit += str(datan)
            
        print("mes", i, mensaje.gainof, buffer_exit)
        buffer.clear
        
        i += 1


    
#print(ingreso, tasa)


# debug
#print("diaria: ", diaria,
#      "final: ", final,
#      type(diaria),
#      type(final))


def Precalculo(ingreso, tasa):
    global diaria
    global correccion
    Calcular_Inversion(ingreso, tasa)
    Clear_Numeros()
    diaria = final/30

    if diaria <= 2.71:
        correccion = 0
    else:
        correccion = 2.71

Precalculo(ingreso, tasa)

print(mensaje.montoenmem, ingreso, "\nTasa estimada:", tasa,          #   OK
      mensaje.daygain, diaria-correccion,                   #   FAILs corregidos
      mensaje.fehgain, (diaria-correccion)*2,               
      mensaje.weekgain, (diaria-correccion)*7,        
      mensaje.monthgain, final, "\nTotal: $", total, "\n")



ingreso = ingreso_inicial
total = ingreso
#print(ingreso, total, ingreso_inicial)


#Calcular_Inversion(ingreso, tasa_plazo_fijo)

#Clear_Numeros()

#Clear_Listas()
# 1        
Setear_Flag(1)
#print("FLAGSET: ", Flag_Set)
# 2
print(" TASA FCI")
# 3
''' GANANCIA ANUAL POR TASA FCI '''

#print("INGRESO INICIAL: $", ingreso_inicial)
nGanancia_Anual(ingreso_inicial, tasa)
# 1
Setear_Flag(2)
#print("FLAGSET: ", Flag_Set)
# 2
print("\n TASA PLAZO FIJO")
# 3
''' GANANCIA ANUAL POR TASA PLAZO FIJO '''
nGanancia_Anual(ingreso_inicial, tasa_plazo_fijo)

#print("\nDEBUG DE VARIABLES\n",
#      "FCI GENERADA:",  type(data_fci), data_fci, "\n",
#      "PLAZO FIJO BP GENERADA:", type(data_bp), data_bp, "\n",
#      "FCI PREDEFINIDA:", type(data_fci_preset), data_fci_preset, "\n",
#      "PLAZO FIJO BP PREDEFINIDA:", type(data_bp_preset), data_bp_preset)

Graficar_Proyecciones(data_fci, data_bp, plot_scale, 1, 13)

Clear_Listas()
Clear_Numeros()

#

GenerarMes(1, 31)
print("\n")
# GENERAR LISTA MENSUAL     #   OK
#Graficar_Proyecciones(data_fci_daily, data_bp_daily, plot_scale_daily, 1, 31)
# FALTA CORREGIR ERROR QUE DUPLICA EJE X
# error al graficar 30 dias





''' version alpha, sin implementar o testear
# estructura base para despues implementar argumentos
if len(sys.argv) < 2: # sin argumentos, no muestra nada en pantalla, salvo un aviso
    print(col.R + "") 
    print("Debe especificar parametro.\nPor ejemplo -m para chocolate :)")  # CHOCOLATE ES UN EASTER EGG
    #Reset()
    #pausa()
    sys.exit(1)
elif sys.argv[1] == "-data_fci":
    print("por el momento se requieren si o si tres o mas parametros "
elif sys.argv[1] == "-data_bp":
    print("por el momento se requieren si o si tres o mas parametros "
    #pausa()                     # PAUSA OBLIGATORIA PARA EVITAR CIERRE DEL PROGRAMA
elif sys.argv[1] > 1 "" and sys.argv[2] == "-data_fci" and sys.argv[3] == "-data_bp": # mostrar en modo texto
    pass
elif sys.argv[1] > 1 "" and sys.argv[2] == "-data_fci" and sys.argv[3] == "-data_bp" and sys.argv[4] == "-graficar": 
	# ademas del modo texto, graficar
    pass
'''
