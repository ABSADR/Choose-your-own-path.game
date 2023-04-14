name1= input("Type your name: ")
print('Welcome' ,name1 , 'to this adventure!')
#ASA CUM AM FOLOSIT NAME CA O VARIABILA DEFINITA POT FOLOSII OPTIUNILE JUCATORULUI PENTRU DECIZIILE DE MAI JOS

answer = input(
    'You are on a dirt road, it has to come to an end and you can go left or right.Wich way will you go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it and swim to swim across.Wich one will it be? ')

    if answer == 'swim':
        print('You swim across and you are eaten by a aligator')
    elif answer == 'walk':
        print('You ran for many hours and you ran out of water and you DIEDD')
    else:
        print('Not a valid decision.You looooose.')



elif answer == 'right':
    answer = input('You came to bridge it looks scary,you wanna cross it or back??')

    if answer == 'cross':
        answer = input('You cross good ideea .yOU MEET A STRANGER ACROSS the bridge!You wanna talk to them? yes or no? ')


        if answer == 'yes':
            answer = input('You talk to the stranger.They gave you drugs.yOU throw them away or take it?THROW/TAKE ')
        elif answer == 'no':
            print('Stranger takes a gun out and kills you!!')
        else:
            print('Not a valid answer.You loooose!!!')

        if answer == 'throw':
            print('You keep walkin and eventually you run out of energy and die...')

        elif answer == 'take':
            print('You took it and wake up in another world..You ask yourself...where you actually are..')

            print("I will tell you", name1, 'You are now in Apoline..')

            apoline = input('Do you remeember it? Say Y or N ').lower()

            if apoline == 'y':
                apoline=input('It was the city you used to play with your sister when you were both in fiesta..What class you choose '
                              'now?MAGE ,Cleric, Fighter or Archer? ').lower()

                if apoline == 'mage':
                    answer= input('You WON AND ONE LAST QUUESTION, are you ENJOYINGG PYTHON SO FAR .YUP/NOpe?? ').lower()
                    print(name1 , 'I will miss you hehe')

                    if answer == 'yup':
                        print('THATS MY BOYY GOOD NIGHTTT')
                        print(name1 , 'LOve YAAA<3')

                elif answer == 'NOpe':
                    print('Well i still think youre cool lol')

                else:
                    print('WRONGGGGGGG !!!GOODBYEEE WORLDDDDD.PYTHON')












            elif('N'):
                print('Then our road ends here and you re dying in the void..So Sad ..')

            else:
                print("Not a valid answer.YOU LOOOSEEEE")





    elif answer == 'back':
        print('You went back and died againnn')
    else:
        print('Not a valid decision.You looooose.')

else:
    print('Not a valid decision.You looooose.')

print('thankss for tryingg!!')
