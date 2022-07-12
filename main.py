from bs4 import BeautifulSoup
import requests
from levenFunc import calcDictDistance


def getRole():
    roles = ["top", "jungle", "support", "adc", "middle"]

    role = input("role\n")
    role = role.lower()
    if role == "exit":
        return quit(0)
    while (role not in roles):
        role = input("you wrote it wrong, write it again\n")

    champion = input("what champ are you playing, or if you'd like to change your role type back\n")
    champion = champion.lower()
    if champion == "exit":
        return quit(0)
    if champion == "back":
        return getRole()

    return role, champion

EXIT = False
print("this will eventually get a somewhat decent gui")
while (EXIT != True):
    role, champion = getRole()

    with open('new_champions.txt', 'r') as file:
        name = file.readlines()
        p = []
        for line in name:
            p.append(line.strip())
        while champion not in p:
            possible_champs = calcDictDistance(champion, 1)
            for x in possible_champs:
                print(f"did you mean {x}?")
            champion = input("write champion name again\n")

    page = requests.get(f"https://u.gg/lol/champions/{champion}/build?role={role}")

    if page.status_code == 200:

        soup = BeautifulSoup(page.text, 'html.parser')

        soup.prettify()

        text = soup.find_all('img', alt=True)
        runes = soup.find_all(class_='perk keystone perk-active')
        mini_runes = soup.find_all(class_='perk perk-active')
        main_runes = soup.find_all(class_='perk-style-title')

        main_rune_list = []
        for result in main_runes:
            main_rune_list.append(result.text)
        rune_to_show = ""
        mini_rune_to_show = []

        for rune in text:
            if (str(rune['alt']) in str(runes[0])):
                rune_to_show = rune['alt']
            if (str(rune['alt']) in str(mini_runes)):
                mini_rune_to_show.append(rune['alt'])

        mini_rune_to_show = mini_rune_to_show[:-5]
        second_rune_page = mini_rune_to_show[-2:]
        first_rune_page = mini_rune_to_show[:-2]
        print("Runes to choose")
        print(f"{main_rune_list[0]}\t\t\t\t\t\t{main_rune_list[1]}\n{rune_to_show}")
        for i in range(0, len(first_rune_page)):
            if i >= len(second_rune_page):
                print(first_rune_page[i])
            else:
                print(f"{first_rune_page[i]}\t\t\t\t{second_rune_page[i]}")
        page.close()
        choice = input("rerun? y/n\n")
        if choice == "yes" or choice == "y":
            EXIT = False
        else:
            EXIT = True