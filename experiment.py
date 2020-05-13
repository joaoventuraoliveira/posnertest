'''
Código para Pygaze
'''

from constants import *
from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.keyboard import Keyboard
import pygaze.libtime as timer
from pygaze.logfile import Logfile
import random



# Criando todas as instâncias (display, screen e coleta de tecla)

# Criando display que será apresentado no monitor do PC
disp = Display()


# Criando a keyboard para coleta de respostas
kb = Keyboard()
# Após kb - Criando o logfile para armazenar e salvar os dados coletados
log = Logfile()

# Tela de instruções do experimento


instructions = 'Seja bem vindo(a)!\n' \
               'Neste experimento as letras F e J apareceraão em ambos os lados da tela.\n' \
               'Se você ver a letra F, então pressione a tecla F.\n' \
               'Se você ver a letra J, então pressione a tecla J.\n' \
               'Tente ser tão rápido e preciso quanto possível durante os ensaios.\n\n' \
                'Aperte a barra de espaço do teclado para começar.\n\n' \
               'Boa sorte!'


instscr = Screen()
instscr.draw_text(text = instructions, fontsize = 22)



# Criando a tela de fixação

fixscr = Screen()
fixscr.draw_fixation(fixtype = 'cross', diameter = 15)



# draw the left box
fixscr.draw_rect(x = BOXCORS['left'][0], y=BOXCORS['left'][1], w = BOXSIZE, h=BOXSIZE, pw = 3, fill = False)
# draw the right box
fixscr.draw_rect(x = BOXCORS['right'][0], y = BOXCORS['right'][1], w = BOXSIZE, h = BOXSIZE, pw = 3, fill = False)



# Criando uma dict para as telas de Cue

cuescr = {}
cuescr['left'] = Screen()
cuescr['right'] = Screen()

# Copiando as configurações da tela de fixação para as telas de Cue
cuescr['left'].copy(fixscr)
cuescr['right'].copy(fixscr)


# Desenhando as telas de Cue com linhas mais grossas
cuescr['left'].draw_rect(x = BOXCORS['left'][0], y = BOXCORS['left'][1], w = BOXSIZE, h = BOXSIZE, pw = 12, fill = False)
cuescr['right'].draw_rect(x = BOXCORS['right'][0], y = BOXCORS['right'][1], w = BOXSIZE, h  =BOXSIZE, pw = 12, fill = False)



# Criando as telas de alvo (sendo 2 dicts com o total de 4 respostas)
tarscr = {}
tarscr['left'] = {}
tarscr['left']['F'] = Screen()
tarscr['left']['J'] = Screen()
tarscr['right'] = {}
tarscr['right']['F'] = Screen()
tarscr['right']['J'] = Screen()

# Copiar as configurações da tela de fixação para as novas telas de alvo
tarscr['left']['F'].copy(fixscr)
tarscr['left']['J'].copy(fixscr)
tarscr['right']['F'].copy(fixscr)
tarscr['right']['J'].copy(fixscr)


# Calcular a posição do alvo
tarpos = {}
tarpos['left'] = (BOXCORS['left'][0] + BOXSIZE/2, BOXCORS['left'][1] + BOXSIZE/2)
tarpos['right'] = (BOXCORS['right'][0] + BOXSIZE/2, BOXCORS['right'][1] + BOXSIZE/2)


# Desenhar todos os possíveis alvos na tela de alvo
tarscr['left']['F'].draw_text(text = 'F', pos = tarpos['left'], fontsize = 35)
tarscr['left']['J'].draw_text(text = 'J', pos = tarpos['left'], fontsize = 35)

tarscr['right']['F'].draw_text(text = 'F', pos = tarpos['right'], fontsize = 35)
tarscr['right']['J'].draw_text(text = 'J', pos = tarpos['right'], fontsize = 35)

# Criando feedback (0 = errado, 1 = correto)
fbscr = {}
fbscr[0] = Screen()
fbscr[0].draw_text(text = 'Errou', colour = (255,0,0), fontsize = 24)
fbscr[1] = Screen()
fbscr[1] = Screen()
fbscr[1].draw_text(text = 'Certo!', colour = (0,255,0), fontsize = 24)


'''
Loop FOR para criar
- uma lista com os ensaios
- Criar as condições parâmetros
'''

alltrials = [] #Lista vazia para os ensaios

# Loop para todos os parâmetros
for cueside in CUELOCS: #lado que ocorrerá a dica (Cue)
    for tarside in TARLOCS: #Para o lado que aparecerá o alvo F e J
        for soa in SOAS: # Para gerar a dessincronização através da diferença de tempo SOAS
            for tar in TARGETS: # Para identificar os alvos F e J

                # Criar uma dict para os ensaios que devem ser executados:
                trial = {'cueside': cueside, \
                        'tarside': tarside, \
                         'target': tar, \
                         'soa': soa}

                #alltrials.append(trial) #Adicionar a dict 'trial' dentro da lista 'alltrials'
                alltrials.extend(TRIALREPEATS * [trial]) #Vinculando a constante TRIALREPEATS
                
random.shuffle(alltrials) # RANDOMIZAR A ORDEM DOS ENSAIOS





'''
Apresentação das instruções
o voluntário deverá apertar a barra de espaço
'''

disp.fill(instscr)
disp.show()
kb.get_key(keylist = 'space', timeout = None)
#timer.pause(20000)



'''
Loop para realizar a tarefa N ensaiios
'''

for trial in alltrials:


    '''
    Apresentação da tela de fixação
    '''
    disp.fill(fixscr)
    fixonset = disp.show()

    timer.pause(FIXTIME)

    '''
    Apresentação da tela de Cue
    '''

    disp.fill(cuescr[trial['cueside']]) # Para fazer referência ao dict Cue (lado) do trial - alltrials
    cueonset = disp.show()

    timer.pause(CUETIME)

    '''
    Apresentar novamente a tela de fixação
    Criar a instância para indicar o final da Cue
    '''

    disp.fill(fixscr)
    cueoffset = disp.show()

    timer.pause(trial['soa'] - CUETIME) # SOA menos o CUETIME


    '''
    Apresentação da tela de alvo
    Respostas (teclas F e J)
    '''

    disp.fill(tarscr[trial['tarside']][trial['target']])
    taronset = disp.show()

    response, presstime = kb.get_key(keylist = ['f','j'], timeout = None)
    response = response.upper() # Para tornar as letras maiúsculas

    # Checando se a resposta foi correta ou não

    if response == trial['target']:
        correct = 1
    else:
        correct = 0

    # Calculando o tempo de reação (TR) - Reaction Time (RT)
    RT = presstime - taronset

    # Inserção da validade (cue e target) para cada ensaio no experimento
    # Definindo se a Cue é válida:
    if trial['cueside'] == trial['tarside']:
        validity = 1
    else:
        validity = 0



    '''
    Apresentar o feedback 
    '''

    disp.fill(fbscr[correct])
    disp.show()
    timer.pause(FEEDBACKTIME)

    # Construindo o arquivo de Logfile dos dados

    # Definindo um cabeçalho
    header = ['fixonset', 'cueonset', 'cueoffset', \
              'taronset', 'cueside', 'tarside', 'valid', \
              'soa', 'target', 'response', 'correct', 'RT']

    # Adicionar o cabeçalho ao logfile
    log.write(header)

    # Iniciar o armazenamento de todos os logs dos ensaios realizados:
    log.write([fixonset, cueonset, cueoffset, taronset,\
              trial['cueside'], trial['tarside'], validity,\
               trial['soa'], trial['target'], response, \
               correct, RT])



# Fechar o logfile
log.close()




# Fechar o experimento
disp.close()



