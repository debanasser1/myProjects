import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','washington', 'new york city']
months=['january','february','march','april','may', 'june','all']
<<<<<<< HEAD
  
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    
=======

days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities=['chicago','washington', 'new york city']
    months=['january','february','march','april','may', 'june','all']
<<<<<<< HEAD
  
    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    
=======

    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city=input("enter a city you want to explore \'chicago or new york or washington\' ").strip().lower()
        if city in cities :
          break

    # TO DO: get user input for month (all, january, february, ... , june)

<<<<<<< HEAD
   
    month=input("enter a month : ").strip().lower()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    day=input("enter a day or \"all\"to say all days data : ").strip().lower()
        
    print('-'*40)  
=======

    month=input("enter a month : ").strip().lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day=input("enter a day or \"all\"to say all days data : ").strip().lower()

    print('-'*40)
>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
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



 # filtered by the city
    df = pd.read_csv(CITY_DATA[city])

  #convert start and end from str to dates
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['End Time'] = pd.to_datetime(df['End Time'])

<<<<<<< HEAD
                                
=======

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
   #extract day and month into separate column

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    df['month'] = pd.to_datetime(df['Start Time']).dt.month

<<<<<<< HEAD
                                
                                
=======


>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
   #filter by month
    if month!='all':
        month=months.index(month)+1
        df=df[df['month'] == month]
<<<<<<< HEAD
    
                                
   #filter by day
    if day!='all':
        df=df[df['day_of_week'] == day.title()]
    
    return df
   
            
=======


   #filter by day
    if day!='all':
        df=df[df['day_of_week'] == day.title()]

    return df


>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
<<<<<<< HEAD
    
    # TO DO: display the most common month  
    df['month']=df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("most common month is:\n{} \n".format(most_common_month))
   
   
=======

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("most common month is:\n{} \n".format(most_common_month))


>>>>>>> b001de863adb9bb4496249306951b30fa2327f44


    # TO DO: display the most common day of week #df['day']=df['Start Time']
    common_day=df['day_of_week'].mode()[0]
    print("most common day is:\n{} \n".format(common_day))


    # TO DO: display the most common start hour
    df['hour']=df['Start Time']
    popular_hour=df['hour'].mode()[0]
    print("most common start hour is:\n{} \n".format(popular_hour))

<<<<<<< HEAD
   
=======

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
<<<<<<< HEAD
    
    print("the most commonly used start station is :",common_start_station)

    # TO DO: display most commonly used end station
    
=======

    print("the most commonly used start station is :",common_start_station)

    # TO DO: display most commonly used end station

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
    common_end_station=df['End Station'].mode()[0]
    print("the most commonly used end station is :",common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+"to"+ df['End Station']
    most_frq_route=df['route'].mode()[0]
    print("the  most frequent combination of start station and end station trip is:",most_frq_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

<<<<<<< HEAD
          
=======

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
    # TO DO: display total travel time
    total=df['Trip Duration'].sum()

    # TO DO: display mean travel time
    total=df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_type=df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
     gender=df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest=df['Birth Year'].min()
        print("the earliest year of birth is :",earliest)
<<<<<<< HEAD
        
        recent=df['Birth Year'].max()
        print("the most recent year of birth is :",recent)
          
=======

        recent=df['Birth Year'].max()
        print("the most recent year of birth is :",recent)

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
        common_year=df['Birth Year'].mode()[0]
        print("the most cpommon  year of birth is :",common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
<<<<<<< HEAD
        
        city, month, day = get_filters()
        df = load_data(city, month ,day) 
        
        
              
=======

        city, month, day = get_filters()
        df = load_data(city, month ,day)



>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
        want_raw_data= input("would you like see raw data?").strip().lower()
        start=0
        end=5
        while(want_raw_data=="yes"):
<<<<<<< HEAD
            print(df.iloc[start:end]) 
            start+=5
            end +=5
            want_raw_data=input("would you like see more of raw data?").strip().lower()
        
=======
            print(df.iloc[start:end])
            start+=5
            end +=5
            want_raw_data=input("would you like see more of raw data?").strip().lower()

>>>>>>> b001de863adb9bb4496249306951b30fa2327f44
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' :
            break


if __name__ == "__main__":
	main()
