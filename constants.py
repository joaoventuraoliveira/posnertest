'''
Código para Pygaze
'''
import os.path


# MAIN
DUMMYMODE = True # False for gaze contingent display, True for dummy mode (using mouse or joystick)
print("Por favor, insira o nome do participante (use 8 caracteres, no máximo), e depois aperte Enter.\n")
DIR = os.path.dirname(__file__) # Construindo o diretório de armazenamento de dados
DATADIR = os.path.join(DIR, 'data') #Incluir a pasta que armazenará o arquivo de logging

LOGFILENAME = input("Nome do participante: ") # logfilename, without path

LOGFILE = os.path.join(DATADIR, LOGFILENAME)


# DISPLAY

# Tamanho do display (olhar a resolução do monitor)
DISPSIZE= (1366,768)

DISPTYPE = 'psychopy' # pode ser 'psychopy' ou 'pygame'

# Tamanho da tela (calcular o tamanho físico da tela usada em centímetros)
#SCREENSIZE = (39.9,29.9)

FGC = (-0.9, -0.9, -0.9)
BGC = (0,0,0)
#FGC = (0,0,0)
#BGC = (255,255,255)
#Locais para apresentação das dicas (cues)
CUELOCS = ['right', 'left']

#Locais potenciais para os alvos
TARLOCS = ['right', 'left']


# SOAS- assincronia de início de estímulo (diferença entre  a sinalização e os conjuntos de alvos)

SOAS = [100, 900]

# Alvos
TARGETS = ['F','J']

# Definindo as caixas que aparecerão (largura e altura) (lados iguais)
BOXSIZE = 200


'''
As coordenadas são definidas de uma forma bastante invertera, no entanto. 
Vamos dar uma olhada mais de perto na esquerda: ela é definida como 25% da largura do display e 50% da altura do display. Mas
 a partir desses dois valores, metade do tamanho da caixa é subtraído. Porque? 
 Bem, em retângulosPyGaze são atualmente definidos por sua coordenada superior esquerda. 
 O centro da caixa esquerda é, em termos de largura e altura do display, (25 por cento, 50%). 
 O canto superior esquerdo é colocado mais alto e mais à esquerda desta coordenada. 
 Você precisa subtrair metade da altura da caixa da coordenada y (50% da altura do display) para deslocá-la para cima e subtrair metade da largura da caixa da coordenada x (25% da largura do display) para subtract half of the box height from the y-coordinate deslocá-la para a subtract half of the box width from the x-coordinate  esquerda. 
 O que você acaba subtraindo metade da largura e altura da caixa da coordenada central pretendida, é a coordenada superior esquerda pretendida da caixa.
'''

# Definindo as coordenadas centrais das ciaxas
BOXCORS = {}
BOXCORS['left'] = (int(DISPSIZE[0] * 0.25 - BOXSIZE * 0.5), int(DISPSIZE[1] * 0.5 - BOXSIZE * 0.5))
BOXCORS['right'] = (int(DISPSIZE[0] * 0.75 - BOXSIZE * 0.5), int(DISPSIZE[1] * 0.5 - BOXSIZE * 0.5))



# Tempos para as Screens do experimento

# Tempo de fixação do olhar para a primeira tela
FIXTIME = 1500

# Duração da tela de CUE (dica)
CUETIME = 0.05

# Duração da tela de feedback
FEEDBACKTIME = 3.0


# Número de repetições a serem executadas e randomização

TRIALREPEATS = 2 # Função vinculada ao módulo random / método random.shuffle()