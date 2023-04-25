import bs4
import requests

html_text = requests.get('https://calendar.zoznam.sk/school-sksk.php').text
soup = bs4.BeautifulSoup(html_text, 'lxml')

months = soup.find_all('div', class_='calendar3')

school_days = []

for month in months:
    days = month.find_all('td', class_='')
    school_days.append(days)


print(school_days)






