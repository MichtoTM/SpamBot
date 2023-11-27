import pyautogui as muz
import time
import keyboard

TimeStamp=1701161843
# Initialisation de la variable SpamScriptBroke
SpamScriptBroke = False

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
        Nombre += 1

# Point d'entrée du script
print("Placez le curseur dans le bon emplacement dans le logiciel où vous voulez spam.")
time.sleep(0.5)
print("Sachez que le logiciel ayant été développé en duspee, Soyez indulgents s'il-vous-please.")

# Demande à l'utilisateur d'utiliser les paramètres par défaut ou non
Defaulft = input("Utilisez le script ? (y/n): ").lower()



# Validation de la réponse de l'utilisateur
while True:
    if Defaulft == "y":
        RunWithDefaultConfig = True
        break
    elif Defaulft == "n":
        RunWithDefaultConfig = False
        print("Au revoir.")
        time.sleep(3)
        quit()
    else:
        print("La valeur entrée ne correspond pas.")


print("Voulez-vous programmer l'envoi des messages à 28/11/2023 9:57:23 ?")
print("Si vous ne voulez pas, le spam sera instantané. ")
print("Vous pourrez l'arrêter à tout moment en appuyant sur Echap.")
while True:
    ProgramToMardi=input("(y/n): ")
    if ProgramToMardi == "y":
        RunWithDefaultConfig = True
        break
    elif ProgramToMardi == "n":
        RunWithDefaultConfig = False
        break
    else:
        print("La valeur entrée ne correspond pas.")


Iterations = int(input("Veuillez indiquez le nombre d'envoi de message : "))
Nombre = 1

# Exécution du script avec les paramètres choisis
if RunWithDefaultConfig is False:
    print("Vous avez 2 secondes pour retourner sur le bon logiciel.")
    time.sleep(2)
    keyboard.hook(BrokeRun)  # Enregistrement de la fonction de gestion des événements pour la touche 'x'
    SpamScript(Iterations, Nombre)
    keyboard.unhook_all()  # Désenregistrement de la fonction de gestion des événements après le script
    if SpamScriptBroke is True:
        print("Vous avez interrompu le script.")
        time.sleep(3)

# Exécution du script avec les paramètres par défaut
elif RunWithDefaultConfig:
    print("L'éxécution du script aura bien lieu le 28/11/2023 9:57:23.")
    while True:
        Hour = int(time.time())
        if Hour>=TimeStamp:
            break
        time.sleep(1)
    keyboard.hook(BrokeRun)  # Enregistrement de la fonction de gestion des événements pour la touche 'x'
    SpamScript(Iterations, Nombre)
    keyboard.unhook_all()  # Désenregistrement de la fonction de gestion des événements après le script
    if SpamScriptBroke is True:
        print("Vous avez interrompu le script.")
        time.sleep(3)