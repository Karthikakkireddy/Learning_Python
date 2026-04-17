# -------- Initial IPL Teams --------

ipl_teams = ["CSK", "MI", "KKR", "RCB", "DC", "RR", "KXIP", "DD"]

# Unpacking list into variables (Pythonic way)
(team1, team2, team3, team4, team5, team6, team7, team8) = ipl_teams
print(f"{team1} : {team2} : {team3} : {team4} : {team5} : {team6} : {team7} : {team8}")


# -------- Sorting --------

ipl_teams.sort()  # Sorts list in-place
print(ipl_teams)  # After sorting


# -------- Adding Elements --------

ipl_teams.append("PWI")  # Syntax: list.append(value) → adds at end
print(f"After adding PWI at the end from IPL : {ipl_teams}")

ipl_teams.insert(0, "KTK")  # Syntax: list.insert(index, value)
print(f"After adding KTK as 0th index in IPL : {ipl_teams}")


# -------- Removing Element --------

ipl_teams.remove('KTK')  
# Removes by value (case-sensitive, error if not found)
print(f"After removing KTK from IPL : {ipl_teams}")


# -------- Replace DC → SRH --------

DC_team_index = ipl_teams.index("DC")  # Find index of "DC"
print(DC_team_index)

ipl_teams[DC_team_index] = "SRH"  # Replace at same index
print(f"After DC changing to SRH (2013) : {ipl_teams}") 


# -------- Pop Last Element --------

last_team = ipl_teams.pop()  
# Syntax: list.pop() → removes last element and returns it
print(f"Last team : {last_team}")
print(f"After removing last ipl team : {ipl_teams}")


# -------- Sorting Again --------

ipl_teams.sort()
print(f"After sorting teams : {ipl_teams}")  # After sorting


# -------- Replace DD → DC --------

DD_team_index = ipl_teams.index("DD")  # Correct index for DD
print(DD_team_index)

ipl_teams[DD_team_index] = "DC"  # FIXED (you used wrong index earlier)
print(f"After DD changing to DC (2019) : {ipl_teams}") 


# -------- Replace KXIP → PBKS --------

ipl_teams[ipl_teams.index("KXIP")] = "PBKS"
print(f"After KXIP changing to PBKS (2021) : {ipl_teams}") 


# -------- Add New Teams --------

new_ipl_teams = ["GT", "LSG"]

ipl_teams.extend(new_ipl_teams)  
# Syntax: list.extend(iterable) → adds multiple elements
print(f"After adding new teams to IPL (2022) : {ipl_teams}") 