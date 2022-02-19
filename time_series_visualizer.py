import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
path = 'fcc-forum-pageviews.csv'
df = pd.read_csv(path).set_index('date')
print(df)

# Clean data
df = df.drop(df[(df['value'] > df['value'].quantile(0.975)) 
    | (df['value'] < df['value'].quantile(0.025))].index)
print(df)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(24, 8))
    ax.plot(df, color= 'red', linewidth = 1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = 24)
    ax.set_xlabel("Date", fontsize = 18)
    ax.set_ylabel("Page Views", fontsize = 18)
    plt.setp(ax, xticks = range(0, 1238, 155))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
draw_line_plot()

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
