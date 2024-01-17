import time

def introduzione():
    print("Benvenuto in un'avventura testuale!")
    time.sleep(1)
    print("Ti trovi in una foresta misteriosa, con tre percorsi davanti a te.")
    time.sleep(1)
    print("Il tuo obiettivo è raggiungere il tesoro nascosto. Scegli saggiamente!")

def scegli_percorso():
    print("\nScegli il percorso:")
    print("1. Percorso della montagna")
    print("2. Sentiero nel bosco")
    print("3. Ponte sospeso")

    scelta = input("Inserisci il numero del percorso scelto: ")
    return scelta

def affronta_sfida(percorso):
    print("\nTi avventuri nel", percorso)

    if percorso == "1":
        print("Affronti una scalata difficile sulla montagna.")
        time.sleep(1)
        print("Riesci a raggiungere la cima e scorgi il tesoro lontano!")

    elif percorso == "2":
        print("Cammini attraverso il sentiero boscoso e incontri una creatura magica.")
        time.sleep(1)
        print("Dopo una breve conversazione, la creatura ti mostra il tesoro nascosto.")

    elif percorso == "3":
        print("Attraversi un ponte sospeso, oscillante nel vento.")
        time.sleep(1)
        print("Raggiungi l'altra parte e trovi il tesoro nascosto tra gli alberi.")

def avventura_testuale():
    introduzione()

    while True:
        scelta = scegli_percorso()

        if scelta in ["1", "2", "3"]:
            affronta_sfida(scelta)
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    avventura_testuale()
