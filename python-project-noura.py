from bs4 import BeautifulSoup
import requests
gpu = input("Enter the name of the gpu: ")
url = f"https://www.newegg.com/p/pl?SrchInDesc={gpu}&N=100007709&Order=1"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

gpu_containers = doc.find_all(class_="item-cell")
for gpu in gpu_containers:
    print("-" * 30)
    try:
        print(gpu_containers.index(gpu)+1)
        print(gpu.find(class_="item-info").find_all('a')[-2].string)
        print("$", gpu.find(class_="price-current").strong.string)
    except:
        continue













