countries=["India","Pakistan","Nepal","Indonesia","Iran","Ireland"]
count=0
for country in countries:
    if country.startswith("I"):
        count=count+1
        print(country,end=", ")
print("\n",count)
