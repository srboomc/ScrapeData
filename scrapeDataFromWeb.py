from bs4 import BeautifulSoup
import requests
import pandas

r = requests.get("https://www.advice.co.th/search?keyword=mesh+tp")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Div = soup.find_all("div", {"class", "product-content product-content-font"})
product_list = []


for i in Div:
    product_dict = {}
    product_dict["Name"] = i.find_all("div", {"class","product-name product-name-font"})[0].text.strip()
    product_dict["Price"] = i.find_all("div", {"class","sale sale-font"})[0].text.strip()
    product_dict["Views"] = i.find_all("div", {"class","product_view"})[0].text.strip()
    product_list.append(product_dict)
print(product_list)



# df = pandas.DataFrame(product_list)
# df.to_csv("meshttp.csv")
# print(soup.prettify())