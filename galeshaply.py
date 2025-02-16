
def stable_match(men_prefs, women_prefs):  # Initialize all men and women as free
  
    free_men = list(men_prefs.keys())
    engagements = {}  # While there are free men
  
    while free_men:
        man = free_men.pop(0)   # Get the preferences of the man
        man_pref = men_prefs[man]  # Propose to the first woman in the man's preference list 
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)  # If the woman is not engaged, engage her with the current man
      
        if not fiance:
            engagements[woman] = man
        else:       
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance): # If the woman prefers the current man over her fiance
                engagements[woman] = man
                free_men.append(fiance)
            else:             
                free_men.append(man)  # The woman rejects the proposal
    return engagements


n = int(input("Enter the number of men/women: "))
men_prefs = {}
women_prefs = {}

print("Enter men's preferences:")
for i in range(n):
    man = input(f"Enter name of man {i+1}: ")
    prefs = input(f"Enter {man}'s preferences (space separated): ").split()
    men_prefs[man] = prefs

print("Enter women's preferences:")
for i in range(n):
    woman = input(f"Enter name of woman {i+1}: ")
    prefs = input(f"Enter {woman}'s preferences (space separated): ").split()
    women_prefs[woman] = prefs


stableMatches = stable_match(men_prefs, women_prefs)
print("Stable Marriages:")
for woman, man in stableMatches.items():
    print(f"{man} engaged to {woman}")


