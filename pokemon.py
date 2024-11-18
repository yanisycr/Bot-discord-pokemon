import requests
from bs4 import BeautifulSoup

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None
    
def get_pixelmon_info(pokemon_name):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
              }
    url = "https://pixelmonmod.com/wiki/" + pokemon_name
    page = requests.get(url, headers=headers)
    print(page)

    soup = BeautifulSoup(page.text, 'html.parser')

    spawn_location = soup.find(class_='roundytop')

    if spawn_location:
        table = spawn_location.find_next('table')

        if table:
            land_elements = table.find_all('tr')

            sRet = ""

            if land_elements:
                for row in land_elements:
                    cells = row.find_all('td')

                    if len(cells) > 2:
                        cell_0 = cells[0].get_text(strip=True)
                        cell_2 = cells[2].get_text(strip=True)
                        row_text = f"spawn : {cell_0} | time : {cell_2}"
                        sRet += row_text + '\n'
                return sRet

    return None

def trad_pokemon(pokemon_name):

    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
              }
    
    url = "https://tyradex.vercel.app/api/v1/pokemon/" + pokemon_name

    page = requests.get(url)
    print(page)

    data = page.json()
    
    # Récupérer le nom en anglais
    name_en = data.get("name", {}).get("en")

    return get_pixelmon_info(name_en)








trad_pokemon("evoli")


            #return (f"Spawn: {land_element.get_text(strip=True)}")
 #       else:
  #          print("Impossible de trouver l'information 'Land'.")
   # else:
    #    print("Impossible de trouver 'Spawn location'.")
 
#get_pixelmon_info("kyogre")
#print(get_pokemon_info("pikachu"))