import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
path = 'fcc-forum-pageviews.csv'
df = pd.read_csv(path)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')

# Clean data
df = df.drop(df[(df['value'] > df['value'].quantile(0.975)) 
    | (df['value'] < df['value'].quantile(0.025))].index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(24, 8))
    ax.plot(df, color= 'red', linewidth = 1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = 24)
    ax.set_xlabel("Date", fontsize = 18)
    ax.set_ylabel("Page Views", fontsize = 18)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame()
    df_bar['year'] = pd.DatetimeIndex(df.index).year
    df_bar['month'] = pd.DatetimeIndex(df.index).month
    df_bar.index = df.index
    df_bar['views'] = df['value']

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 7))
    sns.barplot(x="year", hue="month", y = 'views',
        data = df_bar, ci = None, palette = 'husl')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc = 'upper left', labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        , title = 'Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    #-------First box plot-------
    fig, ax = plt.subplots(1, 2)
    plt.subplot(1, 2, 1)
    sns.boxplot(x = 'year', y = 'value', data = df_box)
    plt.xlabel('Years')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    #-------Second box plot-------
    plt.subplot(1, 2, 2)
    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x = 'month', y = 'value', data = df_box, order = order)
    plt.xlabel('Months')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
draw_box_plot()