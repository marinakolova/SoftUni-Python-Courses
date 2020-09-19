def decrypt_team(encrypted_team, key):
    beginning = encrypted_team.index(key) + len(key)
    decrypted_team = encrypted_team[beginning:]
    end = decrypted_team.index(key)
    decrypted_team = decrypted_team[:end]
    return decrypted_team


inp_key = input()

league_standings = {}
scored_goals = {}

while True:
    inp = input()

    if inp == "final":
        break

    inp_tokens = inp.split(" ")

    team_a = decrypt_team(inp_tokens[0], inp_key)[::-1].upper()
    team_b = decrypt_team(inp_tokens[1], inp_key)[::-1].upper()

    score_a = int(inp_tokens[2].split(":")[0])
    score_b = int(inp_tokens[2].split(":")[1])

    if team_a not in league_standings:
        league_standings[team_a] = 0
    if team_b not in league_standings:
        league_standings[team_b] = 0

    if score_a > score_b:
        league_standings[team_a] += 3
    elif score_b > score_a:
        league_standings[team_b] += 3
    elif score_a == score_b:
        league_standings[team_a] += 1
        league_standings[team_b] += 1

    if team_a not in scored_goals:
        scored_goals[team_a] = 0
    if team_b not in scored_goals:
        scored_goals[team_b] = 0

    scored_goals[team_a] += score_a
    scored_goals[team_b] += score_b

print("League standings:")
for place, kvp in enumerate(sorted(league_standings.items(), key=lambda kv: (-kv[1], kv[0])), start=1):
    print(f"{place}. {kvp[0]} {kvp[1]}")

print("Top 3 scored goals:")
for team, goals in sorted(scored_goals.items(), key=lambda kv: (-kv[1], kv[0]))[:3]:
    print(f"- {team} -> {goals}")
