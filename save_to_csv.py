import csv


def save_to_csv(heros):
  
  # select the files
  file = open('heros.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['NAME', 'DESCRIPTION'])
  
  # for each hero in the received list write 1 line
  for hero in heros:
    writer.writerow(list(hero.values()))
  
f = open('heros.csv')