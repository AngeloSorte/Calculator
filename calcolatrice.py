while True:

    print(''' calcolatrice
              programmer: Angelo
              Operazioni:

              - 1 addizione 
              - 2 sottrazione 
              - 3 divisione
              - 4 moltiplicazione
              ''')
    scelta = input('Scegli:')

    if scelta == '1':
        print('\nHai scelto 1\n')
        a = float(input ('Inserisci il primo num.'))
        b = float(input ('Inserisci il secondo num.'))
        print ('il risultato è ' + str(a + b))
    elif scelta == '2':
        print('\nHai scelto 2\n')
        a = float(input ('Inserisci il primo num.'))
        b = float(input ('Inserisci il secondo num.'))
        print ('il risultato è ' + str(a - b))
    elif scelta == '3':
        print('\nHai scelto 3\n')
        a = float(input ('Inserisci il primo num.'))
        b = float(input ('Inserisci il secondo num.'))
        print ('il risultato è ' + str(a / b))
    elif scelta == '4':
        print('\nHai scelto 4\n')
        a = float(input ('Inserisci il primo num.'))
        b = float(input ('Inserisci il secondo num.'))
        print ('il risultato è ' + str(a * b))
    elif scelta == 'E':
        break
    loop = input('Vuoi continuare?')
    if loop == 's':
        continue
    else:
        break
    

    

    
    
    
