nome = input("Inserisci il nome del tuo personaggio: ")


Introuduzione = ["\nINTRODUZIONE",
                 "Ti trovi in volo sul tuo caccia interplanetario.",
                 "E'stato un lungo viaggio quello che ti ha portato fino a qui, sulla luna boscosa di Molok",
                 "Stai ammirando il panorama che ti circonda quando improvvisamente si accende la spia che segnala una comunicazione in ingresso;",
                 "Cosa fai?\n",
                 "1. Rispondo",
                 "2. Ignoro la chiamata"
                 ]
atto1 = [
        "\nDecidi di rispondere alla chiamata;",
        "Il segnale è molto disturbato ma riesci a capire che è il tuo capo missione.",
        f"{nome} inverti immediatm...grrr...fschhhh...rotta!. SEI IN PERICOLO!",
        "<...fff..shsssss...tai sorvolando una zona nemica!>",
        "Cosa fai?\n",
        "1. Inverto la rotta",
        "2. Proseguo per la mia strada"
        ]


atto2 = ["\nAll'improvviso vedi un lampo nella fitta boscaglia sottostante.",
         "Il rilevatore termico ti segnala che sei seguito da un razzo terra aria.",
         "Cosa fai?\n",
         "1. Tenti una manovra elusiva per schivare il razzo",
         "2. Ti lanci con il paracadute"
         ]

atto3 = ["il missile si avvicina pericolosamente al tuo velivolo.",
         "Non ti rimane nessuna alternativa; con presa salda afferri la leva di espulsione e la tiri.",
         "In un attimo ti ritrovi fuori dal tuo areo, sospeso in aria con il tuo paracadute.",
         "E'questione di pochi attimi prima che il tuo aereo venga colpito dal razzo. L'esplosione è così forte e vicina che perdi i sensi.\n",
         "PREMI INVIO PER PROVARE A SVEGLIARTI",
         "........apri gli occhi e ti rendi conto di essere vivo.",
         "E'notte, non sai esattamente in quale punto del pianeta ti trovi, ma per ora poco importa",
         "al momento il tuo problema è riuscire a scendere dall'albero a cui il tuo paracadute è rimasto impigliato.",
         "Quello che succederà dopo lo scoprirete solo nella prossima puntata.",
         "TO BE CONTINUED..."
         ]

for i in range(len(Introuduzione)):
  print(f"{Introuduzione[i]}")

risposta1 = input()

if risposta1 == "1":

  for i in range(len(atto1)):
    print(f"{atto1[i]}")

  risposta2 = input()
  
  if risposta2 == "1":
    print("Decidi di invertire la rotta.")
  else:
    print("Dopo una valutazione attenta decidi di aumentare il livello di guardia ma di continuare sulla tua rotta.")

for i in range(len(atto2)):
  print(f"{atto2[i]}")

risposta3 = input()
if risposta3 == "1":
  print("Fiducioso nelle tue capacità di pilota militare decidi di tentare alcune manovre elusive")
  print("Nonostante i tuoi sforzi")

for i in range(len(atto3)):
  print(f"{atto3[i]}")