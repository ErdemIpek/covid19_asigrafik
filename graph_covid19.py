from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from bs4 import BeautifulSoup
from selenium import webdriver

path = r'C:\Users\Erdem\Desktop\proje\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get('https://covid19asi.saglik.gov.tr/')
soup_file=driver.page_source




x_data, y_data = [], []

figure = pyplot.figure(num="Aşı Grafiği")
line, = pyplot.plot_date(x_data, y_data, '-')

pyplot.xlabel("Zaman")
pyplot.ylabel("Aşı olan kişi")

def update(frame):
    driver.get('https://covid19asi.saglik.gov.tr/')
    soup_file = driver.page_source
    soup = BeautifulSoup(soup_file, features="lxml")
    data = soup.find('strong',attrs={"class":"count-nums1"}).get_text()
    x_data.append(datetime.now())
    y_data.append(float(data))
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=120000)

pyplot.show()
