import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Write a city name: Chicago, New York City or Washington!").lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue   
        else:
            break

    while True:
        time = input("Do you want to filter as month, day, all or none?").lower()               
        if time == 'month':
            month = input("Which month? January, Feburary, March, April, May or June?").lower()
            day = 'all'
            break
                    
        elif time == 'day':
            month = 'all'
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
                    
        elif time == 'all':
            month = input("Which month? January, Feburary, March, April, May or June?").lower()           
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break       
        elif time == 'none':
            month = 'all'
            day = 'all'
            break       
        else:
            input("You wrote the wrong word! Please type it again. month, day, all or none?")
            break
    
    print(city)
    print(month)
    print(day)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most popular monthh: ", common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most most popular day of week for start time: ", common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most popular hour of the day for bike ridesy: ", common_hour)

    total_time = (time.time() - start_time) 
    print("\nThis took %s seconds." % round(total_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most popular start station: ", common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station: ", common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print("The the most popular trip from start to end: ", common_combination)

    total_time = (time.time() - start_time) 
    print("\nThis took %s seconds." % round(total_time, 2))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is: ", round(total_travel))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("THe avaerage travel time is: ", round(mean_travel))

    total_time = (time.time() - start_time) 
    print("\nThis took %s seconds." % round(total_time, 2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Types of users: subscribers, customers, others",user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("This is the breakdown of gender among users: ", gender)
    else:
        print("There is no gender information in this city.")
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print("The earliest year of birth is: ", earliest)
        recent = df['Birth_Year'].max()
        print("The latest year of birth is: ", recent)
        common_birth = df['Birth Year'].mode()[0]
        print("The most frequent year of birth is: ", common_birth)
    else:
        print("There is no birth year information in this city.")
    
    total_time = (time.time() - start_time) 
    print("\nThis took %s seconds." % round(total_time, 2))
    print('-'*40)


def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No. ").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No. ").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No. ").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return

def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()