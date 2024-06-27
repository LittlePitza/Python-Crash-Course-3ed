# Exercise 3.10 Every Function

def main():
    car_list = ['bmw', 'audi', 'toyota', 'subaru']
    motorbike_list = ['honda', 'yamaha', 'suzuki', 'ducati']
    mountains = ['everest', 'kilimanjaro', 'k2', 'kangchenjunga']
    rivers = ['nile', 'amazon', 'yangtze', 'mississippi']
    countries = ['china', 'india', 'united states', 'indonesia']
    cities = ['tokyo', 'delhi', 'shanghai', 'sao paulo']

    # Print car list
    print(f'Car list: {car_list}')
    # Access the first element of the car list
    print(f'First car in the list: {car_list[0].title()}')
    # Access the last element of the car list
    print(f'Last car in the list: {car_list[-1].title()}')
    # Modify the first element of the motorbike list
    print(f'Motorbike list: {motorbike_list}')
    motorbike_list[0] = 'kawasaki'
    print(f'New motorbike list: {motorbike_list}')
    # Append a new element to the mountains list
    print(f'Mountains list: {mountains}')
    mountains.append('mount everest')
    print(f'New mountains list: {mountains}')
    # Insert a new element to the rivers list
    print(f'Rivers list: {rivers}')
    rivers.insert(0, 'ganges')
    print(f'New rivers list: {rivers}')
    # Remove an element from the countries list
    print(f'Countries list: {countries}')
    countries.remove('united states')
    print(f'New countries list: {countries}')
    # Pop an element from the countries list
    print(f'Countries list: {countries}')
    popped_country = countries.pop()
    print(f'Popped country: {popped_country.title()}')
    print(f'New countries list: {countries}')
    # Delete an element from the countries list
    print(f'Countries list: {countries}')
    del countries[1]
    print(f'New countries list: {countries}')
    # Temporary sort the cities list
    print(f'Cities list: {cities}')
    print(f'Sorted cities list: {sorted(cities)}')
    print(f'Original cities list: {cities}')
    # Sort the cities list permanently
    cities.sort()
    print(f'Permanently sorted cities list: {cities}')
    # Reverse the cities list
    cities.reverse()
    print(f'Reversed cities list: {cities}')
    # Find the length of the cities list
    print(f'Length of the cities list: {len(cities)}')


if __name__ == '__main__':
    main()
