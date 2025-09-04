# Make aan empty list for storing aliens
aliens = []

## make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

## Show the firsts 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("....")

## show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


for alien in aliens[:8]:
    print(alien)
print("....")