import bs4
import requests

html_text = requests.get('https://calendar.zoznam.sk/school-sksk.php').text
soup = bs4.BeautifulSoup(html_text, 'lxml')

months = soup.find_all('div', class_='calendar3')
actual_month = soup.find('div', class_='calendar3 actual')

months_left = months[months.index(actual_month):10]
school_days = []

for month in months_left:
    days = month.find_all('td', class_='')
    for day in days:
        school_days.append(day)


print(len(school_days)-2*(len(months_left)))






