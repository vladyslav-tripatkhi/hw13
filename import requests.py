import requests
import datetime

n= int(input('Введіть кількість параграфів: '))
url = f'https://baconipsum.com/api?type=meat-and-filler&paras={n}'
response = requests.get(url)
paragraphs = response.json()[0]
count = 0 
for p in paragraphs:
    if "Pancentta" in p:
        count += 1      
paragraphs = paragraphs[::-1]          
with open('output.txt', 'w') as f:
    f.write(f'Ім\'я: Ваше ім\'я\n')
    f.write(f'Дата запуску програми: {datetime.datetime.now()}\n')
    f.write(f'Кількість параграфів зі словом "Pancetta": {count}\n')
    f.write('\n'.join(paragraphs))       

print(f'Кількість параграфів зі словом "Pancetta": {count}')
print('Параграфи:\n' + '\n'.join(paragraphs))

Test Some Stuff
