from bs4 import BeautifulSoup
import requests

# собираем ссылки на банки из списка
bank_links = {}
response = requests.get("https://kuap.ru/banks/")
soup = BeautifulSoup(response.content, "html.parser")
for tag in soup.select(".bank-item-row a[href*='/banks/'][href*='/balances/']"):
    bank_name = tag.text.strip().split(": ")[-1]
    link = f"https://kuap.ru{tag['href']}"
    bank_links[bank_name] = link

# выбираем банки для сбора данных
chosen_banks = []
while True:
    chosen_bank = input("Введите номер банка (или 'стоп' для завершения): ")
    if chosen_bank.lower() == "стоп":
        break
    try:
        bank_name = list(bank_links.keys())[int(chosen_bank)-1 if chosen_bank.isdigit() else None]
        chosen_banks.append(bank_name)
        print(f"Банк '{bank_name}' добавлен")
    except:
        print("Банк с таким номером не найден, попробуйте еще раз")

# собираем данные по каждому выбранному банку
results = []
for bank_name in chosen_banks:
    print(f"Собираем данные для банка '{bank_name}'")
    bank_data = {}
    link = bank_links[bank_name]
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    # Собственные средства
    own_funds_tag = soup.find("span", text="Собственные средства")
    if own_funds_tag is not None:
        own_funds = own_funds_tag.find_next("td").text.strip().replace(" ", "")
        bank_data["own_funds"] = own_funds
    else:
        bank_data["own_funds"] = "Недоступно"
    # Актив
    active_tag = soup.find("span", text="Актив")
    if active_tag is not None:
        active = active_tag.find_next("td").text.strip().replace(" ", "")
        bank_data["active"] = active
    else:
        bank_data["active"] = "Недоступно"
    # Высоколиквидные активы
    liquid_assets_tag = soup.find("span", text="Высоколиквидные активы")
    if liquid_assets_tag is not None:
        liquid_assets = liquid_assets_tag.find_next("td").text.strip().replace(" ", "")
        bank_data["liquid_assets"] = liquid_assets
    else:
        bank_data["liquid_assets"] = "Недоступно"
    # Чистая прибыль
    profit_link = link.replace("/balances/", "/profit/")
    response = requests.get(profit_link)
    soup = BeautifulSoup(response.content, "html.parser")
    net_profit_tag = soup.find("span", text="Чистая прибыль")
    if net_profit_tag is not None:
        net_profit = net_profit_tag.find_next("td").text.strip().replace(" ", "")
        bank_data["net_profit"] = net_profit
    else:
        bank_data["net_profit"] = "Недоступно"
    # Добавляем данные банка в список результатов
    results.append(bank_data)

# выводим результаты сбора данных
for i, bank_name in enumerate(chosen_banks, start=1):
    print(f"{i}. Банк '{bank_name}':")
    print(f"   - Собственные средства: {results[i-1]['own_funds']}")
    print(f"   - Актив: {results[i-1]['active']}")
    print(f"   - Высоколиквидные активы: {results[i-1]['liquid_assets']}")
    print(f"   - Чистая прибыль: {results[i-1]['net_profit']}")