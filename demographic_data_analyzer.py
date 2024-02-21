import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # print(df['age'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_labels = df['race'].unique()
    total_list = []
    for race in race_labels:
        count = df['race'].value_counts()[race]
        total_list.append(count)
    race_count = pd.Series(total_list, index=race_labels)
    
    # What is the average age of men?
    ages_male = df[df['sex'] == 'Male']['age']
    average_age_men = round(ages_male.mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df['education'].value_counts()['Bachelors']    
    percentage_bachelors = (bachelors_count / df.shape[0]) * 100
    percentage_bachelors = round(percentage_bachelors, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts()['>50K']
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts()['>50K']
    higher_total_education = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    lower_total_education = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    # print(total_education)
    # percentage with salary >50K
    higher_education_rich = (higher_education / higher_total_education) * 100 
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = (lower_education / lower_total_education) * 100
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['salary'].value_counts()['>50K']
    min_workers_total = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = (num_min_workers / min_workers_total) * 100
    rich_percentage = round(rich_percentage, 1)
    
    # What country has the highest percentage of people that earn >50K?
    plus50 = df[df['salary'] == '>50K']['native-country']
    plus50_countries = plus50.unique()
    plus50_count = {}
    for country in plus50_countries:
        count = plus50.value_counts()[country]
        plus50_count[country] = count
    countries = df['native-country'].unique()
    countries_count = {}
    for country in countries:
        count = df['native-country'].value_counts()[country]
        countries_count[country] = count
    percentages_dic = {}
    for k in countries_count:
        if k in plus50_count:
            percentages_dic[k] = (plus50_count[k] / countries_count[k]) * 100
    highest_earning_country = max(percentages_dic, key=percentages_dic.get)
    highest_earning_country_percentage = round(percentages_dic[highest_earning_country], 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    occupation_IN = df[df['native-country'] == 'India'][df['salary'] == '>50K']['occupation']
    occupations = occupation_IN.unique()
    occupations_count = {}
    for occupation in occupations:
        count = occupation_IN.value_counts()[occupation]
        occupations_count[occupation] = count
    top_IN_occupation = max(occupations_count, key=occupations_count.get)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
