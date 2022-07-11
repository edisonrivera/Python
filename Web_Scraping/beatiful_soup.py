import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    website = "https://subslikescript.com/movie/The_Lost_Future-1615091"
    result = requests.get(website)
    content = result.text
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())


    #? Buscar elemento por el atributo 'class'
    print("-------------- class = \'main-article\' -------------------")
    box = soup.find('article', class_='main-article')
    print(box.text)

    #? Buscar elemento por el nombre de etiqueta
    print("-------------- title -------------------")
    title = soup.find('h1').get_text(strip=True, separator=' ')
    print('Movie title:', title)