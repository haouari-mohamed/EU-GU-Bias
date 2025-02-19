import pandas as pd

# Calculate correlation between EUR/USD and GBP/USD
def calculate_correlation(eurusd, gbpusd):
    return eurusd['Close'].corr(gbpusd['Close'])

# Identify FVGs (Fair Value Gaps) for a given currency pair (based on 1% price change)
def calculate_fvg(data):
    fvg = []
    for i in range(1, len(data)):
        if abs(data['Close'][i] - data['Close'][i-1]) > data['Close'][i-1] * 0.01:
            fvg.append(i)  # Save the index where a FVG occurs
    return fvg

# Calculate the daily bias based on correlation and FVGs
def calculate_bias(correlation, eurusd_fvg, gbpusd_fvg):
    if correlation > 0.8:  # High correlation
        if eurusd_fvg and gbpusd_fvg:
            return "Strong Bias - Buy both EUR/USD and GBP/USD"
        elif eurusd_fvg:
            return "Bias - Buy EUR/USD"
        elif gbpusd_fvg:
            return "Bias - Buy GBP/USD"
        else:
            return "Neutral Bias"
    else:
        return "Weak Correlation - Avoid trading both"
