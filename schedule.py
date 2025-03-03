def display_planning(schedule):
    print("\nPlanning :")
    for day, tasks in schedule.items():
        print(day + ":")
        for task in tasks:
            print("- " + task)
    print("\n")

def get_valid_day(jours):
    while True:
        day = input(f"quel jour voulez-vous planifier ? ({', '.join(jours)}) : ").strip().lower()
        if day in jours:
            return day
        print("jour invalide. Veuillez entrer un jour correct\n")
    
def main():
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    schedule = {jour: [] for jour in jours}
    
    while True:
        print("\n******** Bienvenue ********")
        print("1. afficher le planning : ")
        print("2. ajouter une tache : ")
        print("3. quitter")
        
        choix = input("votre choix : ")
        
        if choix == '1':
            display_planning(schedule)
        elif choix == '2':
            day = get_valid_day(jours)
            #demander la tache
            task = input(f"entrer la tache pour {day.capitalize()} : ").strip()
            if task:
                schedule[day].append(task)
                print(f"tache ajoutée pour {day}")
            else:
                print("tache vide, rien n'a été ajouté")
        elif choix == '3':
            print("merci d'avoir utilisé ce programme !")
            break
        else:
            print("choix inexistant. Essayez encore")
            
if __name__ == "__main__":
    main()
                