def main():
    year = int(input("enter a year "))
    animals = ["dog", "cat", "goat"]
    print(year, "chinese year has animal", animals[year % 3],sep = ' ')

main()

