import random

def adivina_numero():
    intentos = 5
    nro_a_adivinar = random.randint(0, 100)
    print("nro_a_adivinar:", nro_a_adivinar)
 
    while intentos > 0:
        input_intento = input("Adivina el nro. Tienes {} intentos".format(intentos))
        input_intento = int(input_intento)
        intentos = intentos - 1
 
        if input_intento == nro_a_adivinar:
            print("adivinaste")
            # LED
            break
        elif input_intento < nro_a_adivinar:
            print("equivocado. Elige un numero mas alto")
            # LED
        elif input_intento > nro_a_adivinar:
            print("equivocado. Elige un numero mas bajo")
            # LED
 
    print("El numero era:", nro_a_adivinar)
 
adivina_numero()