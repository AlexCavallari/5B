Tavolo=[]
Piatti=[]
Dati_cliente= []
def main_menu():
    scelta=-1
    while scelta!=5:
        print("                              ")
        print("Ristorante - Menu principale")
        print("1. Dati cliente")
        print("2. Listino portate")
        print("3. Listino tavoli")
        print("4. Riassunto Ordine")
        print("5. Invia ordine")
        print("                              ")
        scelta = input("Scelta: ")
        if scelta == "1":
            cliente()
        elif scelta == "2":
            menu()
        elif scelta == "3":
            Tavoli()
        elif scelta =="4":
            print ("i dati del cliente sono ",Dati_cliente)
            print ("i piatti scelti sono ",Piatti)
            print ("Il tavolo scelto è ",Tavolo)
        elif scelta == "5":
            print("Prenotazione eseguita con successo")
            break
        else:
            print("Scelta non valida.")
            main_menu()
def cliente():
    nome=input("inserisci il nome del cliente: ")
    cognome=input("inserisci il cognome del cliente: ")
    num_tel=input("inserisci il numero di telefono del cliente: ")
    Dati_cliente.append(nome)
    Dati_cliente.append(cognome)
    Dati_cliente.append(num_tel)
    main_menu()
def menu():
    choice=-1
    print("                              ")
    print("Ristorante - Listino portate")
    print("1. Pasta alla Carbonara €11 ")
    print("2. Ravioli al Branzino €13 ")
    print("3. Spaghetti cacio e pepe €11")
    print("4. Indietro")
    print("                              ")
    while choice!=4:
        choice = input("Scelta: ")
        if choice == "1":
            Piatti.append("Pasta carbonara")
            print("pasta carbonara aggiunta")
        elif choice == "2":
            Piatti.append("Ravioli Branzino")
            print("Ravioli aggiunti")
        elif choice == "3":
            Piatti.append("Spaghetti cacio e pepe")
            print("Spaghetti cacio e pepe aggiunti")
        elif choice == "4":
            main_menu()
        else:
            print("Scelta non valida.")
            menu()

def Tavoli():
    print("                              ")
    print("Ristorante - Listino tavoli")
    print("1. Tavolo 3 posti |NO FUMATORI!|")
    print("2. Tavolo 4 posti |SI FUMATORI!|")
    print("3. Tavolo 3 posti |SI FUMATORI!|")
    print("4. Tavolo 4 posti |NO FUMATORI!|")
    print("5. Indietro")
    print("                              ")
    
    choice = input("Scelta: ")
    if choice == "1":
        Tavolo.append("Tavolo 3 posti |NO FUMATORI!|")
        print("Tavolo n.1 scelto")
    elif choice == "2":
        Tavolo.append("Tavolo 4 posti |SI FUMATORI!|")
        print("Tavolo n.2 scelto")
    elif choice == "3":
        Tavolo.append("Tavolo 3 posti |SI FUMATORI!|")
        print("Tavolo n.3 scelto")
    elif choice == "4":
        Tavolo.append("Tavolo 4 posti |NO FUMATORI!|")
        print("Tavolo n.4 scelto")
    elif choice == "5":
        main_menu()
    else:
        print("Scelta non valida.")
        Tavoli()
def Cameriere():
    print("                              ")
    print("Ristorante - Camerieri")
    print("1. Carlo Rossi |Anni Servizio=7| Disponibilità=NO")
    print("2. Maria Bianchi |Anni Servizio=3| Disponibilità=SI")
    print("3. Matteo Gallo |Anni Servizio=6| Disponibilità=SI")
    print("4. Indietro")
    print("                              ")
    
    choice = input("Scelta: ")
    if choice == "1":
        print("Cameriere n.1 NON DISPONIBILE")
    elif choice == "2":
        Tavolo.append("Maria Bianchi |Anni Servizio=3| Disponibilità=SI")
        print("Cameriere n.2 scelto")
    elif choice == "3":
        Tavolo.append("Matteo Gallo |Anni Servizio=6| Disponibilità=SI")
        print("Cameriere n.3 scelto")
    elif choice == "4":
        main_menu()
    else:
        print("Scelta non valida.")
        Cameriere()

# Avvio del menu principale
main_menu()
