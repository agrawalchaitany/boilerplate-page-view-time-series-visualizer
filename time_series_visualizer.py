import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
 
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=['date']  )

# Clean data


lower_bound= df['value'].quantile(0.025)
upper_bound= df['value'].quantile(0.975)


df = df.loc[(df['value'] <= upper_bound) & (df['value'] >= lower_bound)].copy()

def draw_line_plot():
    # Draw line plot
    fig , ax= plt.subplots(figsize=(18,6))
    df.plot(kind="line" ,ax=ax)
    ax.set_title(f"Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['Year']=df.index.year
    df['Month']=df.index.month

    df_bar = df.groupby(['Year','Month'], as_index=False)['value'].mean()

    month_labels = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    df_bar['Month']=df_bar['Month'].apply(lambda x: month_labels[x-1])
    # Draw bar plot
    fig , ax = plt.subplots(figsize=(8,8))
    df_bar.pivot(index="Year" , columns="Month", values="value").plot(kind="bar" , ax=ax, colormap="tab10")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months" ,labels=month_labels )

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
    fig , ax = plt.subplots(1,2,figsize=(14,6))
    sns.boxplot(data=df_box, x="Year" ,y ="value", hue= "Year",ax=ax[0])
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box, x="Month" , y="value" ,hue= "Month", ax=ax[1], order=month_order)
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
