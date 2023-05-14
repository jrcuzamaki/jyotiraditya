import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the data
data = pd.read_csv('Betel.csv')
stack = sns.histplot(data, x="Qty (in Kgs)", hue="newqtyinkgs",multiple="stack",palette="light:m_r",edgecolor=".4",linewidth=.5,log_scale=True)
stack = sns.histplot()