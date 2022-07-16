import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date')

# Clean data
df = df[(df['value']>df['value'].quantile(0.025)) & 
         (df['value']<df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig,axes=plt.subplots(1,1,figsize=(10, 5))
    axes.plot(df,color='r')
    axes.xaxis.set_major_locator(MaxNLocator(9))
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    fig=axes.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df2=df.reset_index()
    df2['year'] = pd.to_datetime(df2['date']).dt.year
    df2['month'] = pd.to_datetime(df2['date']).dt.strftime("%B")
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    df2['month'] = pd.Categorical(df2['month'], categories=months, ordered=True)
    df2.sort_values('month',inplace=True)
    df_bar=df2.groupby(['year','month'])['value'].mean().round()

    # Draw bar plot
    fig=df_bar.unstack().plot(kind="bar",figsize=(10, 7))
    fig.set_ylabel('Average Page Views')
    fig.set_xlabel('Years')
    fig=fig.figure




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df3=df.reset_index()
    df3['year'] = pd.to_datetime(df3['date']).dt.year
    df3['month'] = pd.to_datetime(df3['date']).dt.strftime("%b")
    months2=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df3['month'] = pd.Categorical(df3['month'], categories=months2, ordered=True)
    df3.sort_values('month',inplace=True)

    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1, 2, figsize=(15, 5))
    plt.subplot(1,2,1)
    boxplot1=sns.boxplot(x=df3['year'],y=df3['value'])
    boxplot1.axes.set_title("Year-wise Box Plot (Trend)")
    boxplot1.set_ylabel("Page Views")
    boxplot1.set_xlabel("Year")
    plt.subplot(1,2,2)
    boxplot2=sns.boxplot(x=df3['month'],y=df3['value'])
    boxplot2.axes.set_title("Month-wise Box Plot (Seasonality)")
    boxplot2.set_ylabel("Page Views")
    boxplot2.set_xlabel("Month")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
