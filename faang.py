# add a shebang line.
#! /usr/bin/ python

# import
import yfinance as yf
from datetime import datetime
import os 
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# create a function as per https://www.geeksforgeeks.org/python/python-functions/ 
def get_data():

    # Access multiple tickers as per documentation (https://ranaroussi.github.io/yfinance/reference/index.html).
    # adapted code on importing historical data from here: https://rowzero.io/blog/yfinance 
    # specific valid intervals found here: https://medium.com/@anjalivemuri97/day-4-fetching-historical-stock-data-with-yfinance-f45f3bd8b9c6 
    data = yf.download("META AAPL AMZN NFLX GOOG", period="5d", group_by= 'Ticker', interval='1h')

    # flatten the multi-level columns so the csv is very easy to read for analysis (see old files for errors). 
    # Adapted from: https://stackoverflow.com/questions/63107594/how-to-deal-with-multi-level-column-names-downloaded-with-yfinance/63107801#63107801
    data = data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

    #create the time stamp that can dynamically name the file (tested above).
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

    # convert the output into a string so we can use it in a file name.
    current_datetime_str = str(current_datetime)

    # name the file with .csv extension so it saves as a csv file.
    file_name = current_datetime_str + ".csv"

    file_path = "data/"

    # save df to a csv: https://www.geeksforgeeks.org/pandas/saving-a-pandas-dataframe-as-a-csv/ 
    data.to_csv(file_path + file_name)

    # return the DataFrame for further use
    return data

# code adapted from this youtube video on how to get files based on cration or modification time https://www.youtube.com/watch?v=Fbv5Y337DdM&t=105s  
# Get a list of all CSV files in the 'data' folder.
# The '*.csv' pattern ensures only CSV files are included
def plot_data():
    list_of_files = glob.glob('data/*.csv')

    # get the latest file created using max.
    latest_file = max(list_of_files, key=os.path.getctime)

    #open the latest file by reading as csv https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html 
    df = pd.read_csv(latest_file)

    # Convert to datetime and keep only the date part. see https://www.askpython.com/python/examples/extracting-date-from-datetime 
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    # set the size of the figure: https://how.dev/answers/how-to-change-the-figure-size-in-seaborn
    width = 10
    height = 6
    sns.set_theme(rc = {'figure.figsize':(width, height)})

    # adjust the font: https://www.geeksforgeeks.org/data-visualization/how-to-change-label-font-sizes-in-seaborn/ 
    sns.set_theme(font_scale=1.0)

    # plot the line setting date on the x axis, close prices on y, and use hue to include all tickers. see: https://seaborn.pydata.org/generated/seaborn.lineplot.html 
    ax = sns.lineplot(data=df, x="Date", y="Close", hue='Ticker')
    
    # move the legend outside the plot to avoid overlap: https://seaborn.pydata.org/generated/seaborn.move_legend.html 
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

    # get whatever today's date is and make it a string: https://www.programiz.com/python-programming/datetime/strftime 
    today = datetime.now().strftime("%Y-%m-%d")  # or any format you prefer
    
    # then set the title https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
    ax.set_title(today, fontsize=14, fontweight='bold')

    #create the time stamp that can dynamically name the file (tested above).
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

    # convert the output into a string so we can use it in a file name.
    current_datetime_str = str(current_datetime)

    # name the file with .png extension so it saves as a csv file.
    file_name = current_datetime_str + ".png"

    # define the file path. its the plots folder at the same level as my notebook.
    file_path = "plots/"
    # see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html 

    # produce the figure
    fig = ax.get_figure()

    # save it with predefined name and path
    fig.savefig(file_path + file_name)

# run the functions
get_data()
plot_data()