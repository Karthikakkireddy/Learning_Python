# -------- Tuple Basics --------

south_ipl_teams = ("CSK", "RCB", "SRH", "MI")

# Length of tuple
number_of_teams = len(south_ipl_teams)
print(f"Number of IPL teams: {number_of_teams}")

# Accessing elements (0-based index)
print(f"Team A: {south_ipl_teams[0]}")
print()


# -------- Tuple Unpacking --------

# Manual assignment
team_a = south_ipl_teams[0]
team_b = south_ipl_teams[1]
team_c = south_ipl_teams[2]
team_d = south_ipl_teams[3]

print(f"Teams (manual): {team_a}, {team_b}, {team_c}, {team_d}")

# Pythonic unpacking
team_a, team_b, team_c, team_d = south_ipl_teams
print(f"Teams (unpacked): {team_a}, {team_b}, {team_c}, {team_d}")
print()


# -------- Multiple Assignment & Swapping --------

# Standard assignment
home_matches = 3
away_matches = 2
print(f"Before swap → Home: {home_matches}, Away: {away_matches}")

# Pythonic assignment
home_matches, away_matches = 3, 2

# Swap values (no temp variable needed)
home_matches, away_matches = away_matches, home_matches
print(f"After swap  → Home: {home_matches}, Away: {away_matches}")
print()


# -------- Tuple Concatenation --------

t1 = ("CSK", "RCB")
t2 = ("SRH", "MI")

# Combine tuples (creates new tuple)
t1 = t1 + t2
print(f"Combined tuple (t1): {t1}")
print(f"Original tuple (t2): {t2}")

# Adding a single element (must be a tuple → comma is important)
t1 = t1 + ("KTK",)
print(f"After adding KTK: {t1}")
print()


# -------- Membership Testing --------

more_than_one_trophy_teams = ("CSK", "MI", "KKR")

# Case-sensitive checks
print(f"Did CSK win more than one trophy? {'CSK' in more_than_one_trophy_teams}")
print(f"Did csk win more than one trophy? {'csk' in more_than_one_trophy_teams}")
print(f"Did RCB win more than one trophy? {'RCB' in more_than_one_trophy_teams}")