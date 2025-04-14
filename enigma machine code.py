from reflector_rotor_eni import *
def return_list (name_rotor):
    if name_rotor=='rotor1':
        return rotor1   
    if name_rotor=='ro2':
        return rotor2    
    if name_rotor=='ro3':
        return rotor3    
    if name_rotor=='ro4':
        return rotor4    
    if name_rotor=='ro5':
        return rotor5    
    if name_rotor=='refB':
        return reflectorB    
    if name_rotor=='refC':
        return reflectorC

def letter_to_number(letter):
    return alphabet[letter]

def number_to_letter(number):
    for letter in alphabet.keys():
        if alphabet[letter]==number:
            return letter
        else:
            pass

def path_in_rotor (rotor_reflector,number):
    return rotor_reflector[number]

def backpath_in_rotor (rotor, number):
    for start_number in rotor.keys():
        if rotor[start_number]==number:
            return start_number


def enigma (code, rotorA, rotorB, rotorC, reflector):
    counter_rotorA=0
    counter_rotorB=0
    counter_rotorC=0
    final_chain=''
    for letter in code:
        path_number=letter_to_number (letter)

        counter_rotorA+=1
        path_number=((counter_rotorA + path_number - 1) % 26) + 1
        print (path_number,'before')        
        path_number=path_in_rotor(rotorA,path_number)
        print (path_number,'1rot')

        if counter_rotorA==26:
            counter_rotorA=0
            counter_rotorB+=1        
        path_number=((counter_rotorB + path_number - 1) % 26) + 1
        path_number=path_in_rotor(rotorB,path_number)
        print (path_number,'2rot')

        if counter_rotorB==26:
            counter_rotorB=0
            counter_rotorC+=1        
        path_number=((counter_rotorC + path_number - 1) % 26) + 1
        path_number=path_in_rotor(rotorC,path_number)
        print (path_number,'3rot')

        if counter_rotorC==26:
            counter_rotorA=0
            counter_rotorB=0
            counter_rotorC=0
        path_number=path_in_rotor(reflector,path_number)
        print (path_number,'ref')

        path_number=backpath_in_rotor (rotorC,path_number)
        print (path_number,'1rotorback')

        path_number=backpath_in_rotor (rotorB,path_number)
        print (path_number,'2rotorback')

        path_number=backpath_in_rotor (rotorA,path_number)
        print (path_number,'3rotorback')

        final_chain+=number_to_letter (path_number)
    return final_chain

while True:
    code=input('Your code:')
    rotorA=return_list(input ('First rotor:(ro1|ro2|ro3|ro4|ro5)'))
    rotorB=return_list(input ('Second rotor:(ro1|ro2|ro3|ro4|ro5)'))
    rotorC=return_list(input ('Third rotor:(ro1|ro2|ro3|ro4|ro5)'))
    reflector=return_list(input ('Reflector(refB|refC)'))
    print(enigma(code,rotorA, rotorB,rotorC,reflector))#rotor1,rotor2,rotor3,reflectorB


