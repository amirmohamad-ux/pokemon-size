import requests
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def PokemonList():

    url=f"https://pokeapi.co/api/v2/pokemon/"
    respons=requests.get(url)

    if respons.status_code == 404 :
        print("Warning : Page Addres Is Not True")

    elif respons.status_code == 200 :
        data = respons.json()
        ResData=data["results"]
        num =0
        print(colorama.Fore.WHITE+"Pokemon List : ")

        for i in ResData :
            num += 1
            print(colorama.Fore.LIGHTCYAN_EX+f"    {num}.{i["name"]} ")

    elif respons.status_code == 429 :
        print("Warning : You Are So Speed Pleaes Wait And Try Again...")

    elif respons.status_code == 500 :
        print("Error : Error From Server Side... ")

    else :
        print(f"Search This In Your Browser : code {respons.status_code}")

while True:
    try :

        PokemonList()

        EnterNamePokemon=int(input(colorama.Fore.WHITE+"Enter 1 of 20 number for give detail: "))
        if EnterNamePokemon > 20 or EnterNamePokemon < 1 :
            print(colorama.Fore.YELLOW+"WARNING : Pleas Select Between 1 of 20")

        else :

            url=f"https://pokeapi.co/api/v2/pokemon/{str(EnterNamePokemon)}"
            respons=requests.get(url)
            if respons.status_code == 200 :
                data = respons.json()

                print(colorama.Fore.LIGHTRED_EX+f"name : {data['name']} \nheight : {data['height']}  \nweight : {data['weight']}")
            elif respons.status_code == 404 :
                print("Warning : Page Addres Is Not True")

            elif respons.status_code == 429 :
                print("Warning : You Are So Speed Plaes Wait And Try Again...")

            elif respons.status_code == 500 :
                print("Error : Error From Server Side... ")

            else :
                print(f"Search This In Your Browser : code {respons.status_code}")

    except ValueError:
        print(colorama.Fore.YELLOW+"WARNING : Pleas Enter Number")

    except requests.exceptions.ConnectionError :
        print(colorama.Fore.RED+"Error : Your Don't Have Network ")
        break

    