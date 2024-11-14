from bs4 import BeautifulSoup

#abrir o arquivo html apenas para leitura e apos, e impresso o q esta escrito no arquivo html
#with open("home.html","r") as html_file:
    #content = html_file.read()
    #print(content)

    #imprimirá a mesma coisa que a anterior, mas o lxml e mais eficiente para documentos maiores
    #soup = BeautifulSoup(content,"lxml")
    #print(soup.prettify())

    #print de todos o h5 
    #tags = soup.find_all("h5")
    #print(tags)

    #Imprime o nome dos cursos 
    #courses_html_tags = soup.find_all("h5")
    #for course in courses_html_tags:
        #print(course.text)

    #Encontra todos os elementos <div> com a classe "card" na página HTML
    #course_cards = soup.find_all("div", class_="card")
    #for course in course_cards:
        # Extrai o nome do curso, que está dentro da tag <h5>
        #course_name = course.h5.text
        #Faz a mesma coisa que o anterior, mas divide o texto para pegar o ultimo elemento(neste caso o preco)
        #course_price = course.a.text.split()[-1]

        #print(f"{course_name} costs {course_price}")

import requests
html_text = requests.get("https://www.linkedin.com/search/results/ALL/?keywords=python&origin=SWITCH_SEARCH_VERTICAL&sid=KIB").text
soup = BeautifulSoup(html_text, "lxml")
#jobs = soup.find_all("li", class_="search-results__search-feed-update")
#print(jobs)

job = soup.find_all("li", h2="search-results__cluster-title           earch-results__cluster-title-bar--x-large")
print(job)
company_name = job.find("h2", class_="joblist-comp-name").text
print(company_name)