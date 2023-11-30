import pyautogui as muz
import time
import keyboard


# Initialisation de quelques variables primordiales
Temps = None
TempsInTimeStamp = None
Nombre = 0


# Initialisation de la variable SpamScriptBroke
SpamScriptBroke = False

#Fonction de déboguage
def getAndShowSpeed(Nombre,Finsish,Start):
    TimeElasped=Finish-Start
    SpeedVariable=Nombre/TimeElasped
    print("Le script à envoyé ",Nombre," en ",TimeElasped," seconde(s) soit :",SpeedVariable," message(s)/secondes.")

# Fonction de coupure d'urgence appelée lorsqu'une touche est pressée
def BrokeRun(e):
    global SpamScriptBroke
    if e.name == 'esc' and e.event_type == keyboard.KEY_DOWN:
        print("Touche Echap pressée.")
        SpamScriptBroke = True


# Fonction pour le script de spam
def SpamScript(Iteration, Nombre):
    for i in range(Iteration):
        if SpamScriptBroke is True:
            print("Le script a été interrompu.")
            break
        Nombre += 1
        muz.keyDown("ctrl")
        time.sleep(0.001)
        muz.keyDown("v")

        time.sleep(0.001)

        muz.keyUp("ctrl")
        time.sleep(0.001)
        muz.keyUp("v")

        muz.typewrite(" ")
        muz.typewrite(str(Nombre))

        muz.press('Enter')

    return Nombre


def TempsIntoTimeStamp(Temps):
    return Temps * 60


def minutor(TempsInTimeStamp):
    Depart = int(time.time())

    while True:
        Hour = int(time.time())
        T2 = Hour - Depart

        if T2 >= TempsInTimeStamp:
            RunWithDefaultConfig = True
            return RunWithDefaultConfig  # Cette ligne est suffisante pour retourner la valeur et sortir de la fonction
        time.sleep(1)

# Point d'entrée du script
print("Placez le curseur dans le bon emplacement dans le logiciel où vous voulez spam.")
time.sleep(0.5)
print("Sachez que le logiciel ayant été développé en duspee, soyez indulgents s'il-vous-please.")

while True:
    # Demande à l'utilisateur d'utiliser le programme
    Default = input("Utilisez le script ? (y/n): ").lower()
    if Default == "y":
        ProgrammerEnvoi = True
        break
    elif Default == "n":
        ProgrammerEnvoi = False
        print("Au revoir.")
        input("Faites Entrée pour fermer...")
        quit()
    else:
        print("La valeur entrée ne correspond pas.")


print("Voulez-vous programmer l'envoi des messages ?")
print("Si vous ne voulez pas, le spam sera instantané. ")
print("Vous pourrez l'arrêter à tout moment en appuyant sur Echap.")


# Validation de la réponse de l'utilisateur au sujet de la programmation du spam
while True:
    ProgramToMardi = input("(y/n): ")
    if ProgramToMardi == "y":
        ProgrammerEnvoi = True
        break
    elif ProgramToMardi == "n":
        ProgrammerEnvoi = False
        break
    else:
        print("La valeur entrée ne correspond pas.")

if ProgrammerEnvoi:
    while True:
        try:
            Temps = int(input("Entrez le nombre de minutes avant de spam (il doit s'agir d'un entier) : "))
            TempsInTimeStamp = TempsIntoTimeStamp(Temps)
            break
        except ValueError:
            print("Une erreur est survenue. Assurez-vous d'entrer un nombre entier.")

Iterations = int(input("Veuillez indiquer le nombre d'envoi de message : "))


# Exécution du script avec les paramètres choisis
if not ProgrammerEnvoi:
    print("Vous avez 2 secondes pour retourner sur le bon logiciel.")
    time.sleep(2)
    keyboard.hook(BrokeRun)  # Enregistrement de la fonction de gestion des événements pour la touche 'Esc'
    Start=time.time()
    Nombre=SpamScript(Iterations, Nombre)
    Finish=time.time()
    keyboard.unhook_all()  # Désenregistrement de la fonction de gestion des événements après le script

    if SpamScriptBroke:
        print("Vous avez interrompu le script.")
        input("Faites Entrée pour fermer...")

# Exécution du script avec les paramètres par défaut
elif ProgrammerEnvoi:
    print("L'exécution du script aura bien lieu dans", str(Temps), "minute(s).")
    minutor(TempsInTimeStamp)
    keyboard.hook(BrokeRun)  # Enregistrement de la fonction de gestion des événements pour la touche 'Esc'
    Start=time.time()
    Nombre=SpamScript(Iterations, Nombre)
    Finish=time.time()
    keyboard.unhook_all()  # Désenregistrement de la fonction de gestion des événements après le script

    if SpamScriptBroke:
        print("Vous avez interrompu le script.")
        input("Faites Entrée pour fermer...")


print("")
getAndShowSpeed(Nombre,Finish,Start)