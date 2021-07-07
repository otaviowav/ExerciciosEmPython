# Resolução

diaSemana = str(input()) 
prazoEntrega = int(input())

if prazoEntrega == 0:
    print('chega hoje!')
elif prazoEntrega == 1:
    if diaSemana == 'domingo':
        print('sera entregue segunda')
    elif diaSemana == 'segunda':
        print('sera entregue terca')
    elif diaSemana == 'terca':
        print('sera entregue quarta')
    elif diaSemana == 'quarta':
        print('sera entregue quinta')
    elif diaSemana == 'quinta':
        print('sera entregue sexta')
    elif diaSemana == 'sexta':
        print('sera entregue sabado')
    elif diaSemana == 'sabado':
        print('sera entregue domingo')
elif prazoEntrega == 2:
    if diaSemana == 'domingo':
        print('sera entregue terca')
    elif diaSemana == 'segunda':
        print('sera entregue quarta')
    elif diaSemana == 'terca':
        print('sera entregue quinta')
    elif diaSemana == 'quarta':
        print('sera entregue sexta')
    elif diaSemana == 'quinta':
        print('sera entregue sabado')
    elif diaSemana == 'sexta':
        print('sera entregue domingo')
    elif diaSemana == 'sabado':
        print('sera entregue segunda')
elif prazoEntrega == 3:
    if diaSemana == 'domingo':
        print('sera entregue quarta')
    elif diaSemana == 'segunda':
        print('sera entregue quinta')
    elif diaSemana == 'terca':
        print('sera entregue sexta')
    elif diaSemana == 'quarta':
        print('sera entregue sabado')
    elif diaSemana == 'quinta':
        print('sera entregue domingo')
    elif diaSemana == 'sexta':
        print('sera entregue segunda')
    elif diaSemana == 'sabado':
        print('sera entregue terca')
elif prazoEntrega == 4:
    if diaSemana == 'domingo':
        print('sera entregue quinta')
    elif diaSemana == 'segunda':
        print('sera entregue sexta')
    elif diaSemana == 'terca':
        print('sera entregue sabado')
    elif diaSemana == 'quarta':
        print('sera entregue domingo')
    elif diaSemana == 'quinta':
        print('sera entregue segunda')
    elif diaSemana == 'sexta':
        print('sera entregue terca')
    elif diaSemana == 'sabado':
        print('sera entregue quarta')
elif prazoEntrega == 5:
    if diaSemana == 'domingo':
        print('sera entregue sexta')
    elif diaSemana == 'segunda':
        print('sera entregue sabado')
    elif diaSemana == 'terca':
        print('sera entregue domingo')
    elif diaSemana == 'quarta':
        print('sera entregue segunda')
    elif diaSemana == 'quinta':
        print('sera entregue terca')
    elif diaSemana == 'sexta':
        print('sera entregue quarta')
    elif diaSemana == 'sabado':
        print('sera entregue quinta')
else:
    if diaSemana == 'domingo':
        print('sera entregue sabado')
    elif diaSemana == 'segunda':
        print('sera entregue domingo')
    elif diaSemana == 'terca':
        print('sera entregue segunda')
    elif diaSemana == 'quarta':
        print('sera entregue terca')
    elif diaSemana == 'quinta':
        print('sera entregue quarta')
    elif diaSemana == 'sexta':
        print('sera entregue quinta')
    elif diaSemana == 'sabado':
        print('sera entregue sexta') 
