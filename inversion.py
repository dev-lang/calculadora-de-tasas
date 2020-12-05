# v0.2.2 4 dic 2020 23:00
import matplotlib.pyplot as ploteame

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
#fluct4 = 0
fluct_total = fluct + fluct2 + fluct3
tasa += fluct_total
total = 1 # workaround
final = 1 # workaround
resultado = [] # workaround
buffer_exit = "$"

data_fci = []
data_bp = []
''' los presets son solamente a modo de demostracion '''
data_fci_preset = [32668.229333333333,33336.458666666666,34728.73363857422,36179.156046500175,37690.15437934489,39264.258550228646,40904.10413240658,42612.43677209378,44392.116785589096,46246.1239483947,48177.5624843501,50189.666263133986]
data_bp_preset = [32966.933333333334,33933.86666666667,35984.603342222224,38159.272870870525,40465.364928033465,42910.82181518429,45504.06581354859,48254.02819088071,51170.17996121627,54262.564503539106,57541.83215170298,61019.27687473757]
#data_fci_preset_broken = [458666666666,34728.73363857422,36179.156046500175,37690.15437934489,39264.258550228646,40904.10413240658,42612.43677209378,44392.116785589096,46246.1239483947,48177.5624843501,50189.666263133986]
#data_bp_preset_broken = [35984.603342222224,38159.272870870525,40465.364928033465,42910.82181518429,45504.06581354859,48254.02819088071,51170.17996121627,54262.564503539106,57541.83215170298,61019.27687473757]



plot_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # MESES, EJE X    # OK - ESCALA CHEQUEADA

fmt1 = 'b'
fmt2 = 'g'

def Graficar_Proyecciones(data_fci, data_bp, plot_scale):   # OK - CHEQUEADO
    ploteame.title("Calculadora de TASAS version alpha")
    ploteame.plot(plot_scale,data_fci, fmt1,
                  plot_scale,data_bp, fmt2)
    ploteame.grid(True)
    #print("axis: ", ploteame.axis())
    #print(data_fci.index[13], data_bp.index[13])
    #ploteame.axis(1, 13, data_fci.index[13], data_bp.index[13])
    #print("axis: ", ploteame.axis())
    ploteame.xlim(1, 13)                                    # ALTERNATIVA A MODIFICAR AXIS, PERMITE MANTENER VALOR Y SEGUN REGISTRO
    ploteame.ylabel("Importe/Ganancia")
    ploteame.xlabel("Meses/Tiempo")
    ploteame.legend(['FCI', 'BP'])                          # ALTERNATIVA A APLICAR EL LABEL EN EL PLOT, PERMITE MANTENER LA SINTAXIS, X1 Y X2
    ploteame.show()

def Setear_Flag(flag):                                      # OK
    global Flag_Set
    '''
1 = FCI
2 = BP
0 = NO USAR
'''
    Flag_Set = flag

def Agregar_A_Lista(total_mensual):                         # OK
    global Flag_Set
    global data_fci
    global data_bp
    if Flag_Set == 1:
        total_mensual = float(total_mensual)
        data_fci.append(total_mensual)
    elif Flag_Set == 2:
        total_mensual = float(total_mensual)
        data_bp.append(total_mensual)
    else:
        pass


while True:
    ingreso = input("Ingrese el monto a invertir:")
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
    data_fci_preset.clear()
    data_bp_preset.clear()

def nGanancia_Diaria():     # incomplete
    for n in range(a, c):
        n += 1
        pass

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
        
        Agregar_A_Lista(total_mensual)
        
        
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
            
        print("mes", i, "ganancia de:", buffer_exit)
        buffer.clear
        
        i += 1


    
#print(ingreso, tasa)
Calcular_Inversion(ingreso, tasa)

Clear_Numeros()


diaria = final/30
correccion = 2.71

# debug
#print("diaria: ", diaria,
#      "final: ", final,
#      type(diaria),
#      type(final))

print("Monto ingresado: $", ingreso, "\nTasa estimada:", tasa,          #   OK
      "\nGanancia a las 24 hs: $", diaria-correccion,                   #   FAIL
      "\nGanancia a las 48 hs: $", (diaria-correccion)*2,               #   FAIL
      "\nGanancia a la primer semana: $", (diaria-correccion)*7,        #   FAIL HEREDADO
      "\n\nGanancia al primer mes: $", final, "\nTotal: $", total, "\n")#   FAIL HEREDADO

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

Graficar_Proyecciones(data_fci, data_bp, plot_scale)
