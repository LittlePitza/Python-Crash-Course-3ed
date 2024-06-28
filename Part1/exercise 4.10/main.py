# Exercise 4.10 Slices.

def main():
    tech_companies = ['google', 'apple', 'microsoft', 'amazon', 'facebook', 'ibm', 'oracle', 'intel', 'twitter',
                      'netflix', 'paypal', 'uber', 'airbnb', 'lyft', 'snapchat', 'slack', 'pinterest', 'spotify',]
    print(f'The first three items in the list are: {tech_companies[:3]}')
    print(f'Three items from the middle of the list are: {tech_companies[8:11]}')
    print(f'The last three items in the list are: {tech_companies[-3:]}')
    print(f'The complete list of companies on the list are: ', end='')
    for company in tech_companies:
        print(company, end=', ')


if __name__ == '__main__':
    main()

