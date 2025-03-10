import pandas as pd
import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def load_data():
    file_path = "../data/BrentOilPrices.csv"
    df = pd.read_csv(file_path)
    df.columns = ['Date', 'Price']
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)
    df = df.dropna().sort_values(by='Date')
    return df

def save_cleaned_data(df):
    df.to_csv("../data/cleaned_BrentOilPrices.csv", index=False)

def plot_price_trends(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df['Date'], y=df['Price'])
    plt.xlabel('Year')
    plt.ylabel('Brent Oil Price (USD)')
    plt.title('Brent Oil Price Over Time')
    plt.grid()
    plt.show()

def detect_change_points(df):
    with pm.Model() as model:
        switchpoint = pm.DiscreteUniform("switchpoint", lower=0, upper=len(df) - 1)
        mu1 = pm.Normal("mu1", mu=df['Price'].mean(), sigma=df['Price'].std())
        mu2 = pm.Normal("mu2", mu=df['Price'].mean(), sigma=df['Price'].std())
        
        tau = switchpoint
        price = pm.math.switch(tau >= np.arange(len(df)), mu1, mu2)
        
        sigma = pm.HalfNormal("sigma", sigma=df['Price'].std())
        obs = pm.Normal("obs", mu=price, sigma=sigma, observed=df['Price'])
        
        trace = pm.sample(2000, return_inferencedata=True, cores=2)
        
    return trace, switchpoint

def main():
    df = load_data()
    save_cleaned_data(df)
    plot_price_trends(df)
    trace, switchpoint = detect_change_points(df)
    pm.plot_posterior(trace)
    plt.show()

if __name__ == "__main__":
    main()
