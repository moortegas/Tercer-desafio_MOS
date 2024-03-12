print("Primeros Auxilios: Qué hacer ante una emergencia.\n")

resp=str(input("¿La persona responde a estimulos?. Responda [Si ó No] : ")).lower()

# respuesta1 = []
# for respuesta1 in resp:

if resp == "si":
        print("Si su respuesta es SI Evalue el traslado al hospital \n")
     
else:
    print("ABRA LA VIA AEREA")

    resp_1=input(" ¿RESPIRA? ").lower()

    if resp_1 == "si":
        print("Permita posición de suficiente respiración")
    else:
        print("DAR respiración boca a boca por 5 veces y llamar a la ambulancia")
        
        resp_2=input("¿SIGNOS DE VIDA? ").lower()
        if resp_2 == "si":
            print("Reevaluar a la espera de la ambulacia")
        else: 
            print("ADMINISTRAR COMPRESIONES Torácicas hasta que llegue la ambulancia")
        
        resp_3=str(input("¿LLEGO LA AMBULANCIA?: ")).lower()
        if resp_3 == "no":
            resp_3=input("¿SIGNOS DE VIDA? ").lower()
        if resp_3 == "si":
            print("TRANSFIERA AL ACCIDENTADO al personal médico de la ambulacia")
        else: 
            print("ADMINISTRAR COMPRESIONES Torácicas hasta que llegue la ambulancia")