import requests
from bs4 import BeautifulSoup

# renseigner quoiqui et ou
quoiqui = "entreprise+de+plomberie"
ou = "Saint+Laurent+du+Maronie"
login_url = f"https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={quoiqui}&ou={ou}+%2897320%29&univers=pagesjaunes&idOu="
# login_url = f"https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=entreprise+de+plomberie&ou=Saint+Laurent+du+Maroni+%2897320%29&univers=pagesjaunes&idOu="
result_url = f"https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={quoiqui}&ou={ou}+%2897320%29&univers=pagesjaunes&idOu="

# # Création d'une session pour conserver les cookies
session = requests.session()

# # Obtenir la page de connexion pour récupérer les cookies et éventuellement des tokens CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")

headers = {
    "Referer": login_url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

get_response = session.post(login_url, headers=headers)

result_response = session.get(result_url)
print(result_response.text[5000:])
