#Import 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def validate_city(city):
    """
    This function return true or false value to check
    if the input city is correct or not
    """
    # the name of cites avalible
    cites = ['chicago','new york city','washington']

    if city in cites:
            return True
    return False

def validate_month(month):
    """
    This function return true or false value to check
    if the input month is correct or not
    """

    # the  month of the year + string 'all'
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november'  ,'december','all']

    if month in months  :
            return True
    return False


def validate_day(day):
    """
    This function return true or false value to check
    if the input day is correct or not
    """

     # the  month of the year + string 'all'
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',  'sunday','all']

    if day in days:
            return True
    return False


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
  #     try:
           city = input("Enter the name of the city to analyze: ").lower()
           if validate_city(city): break
           else:
#       except ValueError:
             print( "Error: Invalid input.")






    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
#       try:
           month = input("Enter name of the month to filter by, or \"all\" to apply no month filter: ").lower()
           if validate_month(month): break
           else:
#       except ValueError:
             print( "Error: Invalid input.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
#       try:
           day = input("Enter the name of the day of week to filter by, or \"all\" to apply no day filter: ").lower()
           if validate_day(day): break
           else:
#       except ValueError:
             print( "Error: Invalid input.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the  to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november'  ,'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # TO DO: display the most common month
    df['month'] =df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Start month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print('Most Common Start day:', popular_day)


    # TO DO: display the most common start hour

    df['hour'] =df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:',most_common_start_station)




    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:',most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time)


    # TO DO: display mean travel time
    #average travel time
    lenth_travel_time= len(df['Trip Duration'])
    averge= total_travel_time/lenth_travel_time
    print("Mean of travel time:",averge)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types',df['User Type'].value_counts())



    # TO DO: Display counts of gender
    if  'Gender' in df.columns:
         print('Counts of gender',df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if  'Birth Year' in df.columns:
       most_common_year_birth = df['Birth Year'].mode()[0]
       print('The earliest year of birth',int(df['Birth Year'].min()))
       print('The recent year of birth',int(df['Birth Year'].max()))
       print('Most common year of birth',most_common_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_data(df):
    ''' This function displays the rows of data '''

    start = 0
    end = 5
    df_length = len(df.index)

    while True:
        answer= input('Would you like to see  the  data?').lower()
        if answer == 'yes':
            print("\nDisplaying only 5 rows of data.\n")
            if end > df_length:
                end = df_length
            print(df.iloc[start:end])
            start += 5
            end+= 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
