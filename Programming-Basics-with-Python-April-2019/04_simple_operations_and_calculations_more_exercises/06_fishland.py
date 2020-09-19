skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = 1.6 * skumria_price
safrid_price = 1.8 * caca_price
midi_price = 7.50

total_price = palamud_kg * palamud_price + safrid_kg * safrid_price + midi_kg * midi_price

print(f"{total_price:.2f}")
