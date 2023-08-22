
visited_cities = str(input('Enter with a space the cities in which you have been in the past 10 years: ')).lower().split()
future_cities = str(input('Now enter the cities you want to visit in the next 10 years: ')).lower().split()

common_cities = set(visited_cities) & set(future_cities)
if common_cities:
    print("\nYou probably liked the following cities:", ", ".join(common_cities))
else:
    print("\nYou are open to something new")
