import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

total_matches_played= [50,60,70,80,90,100,110]
total_matches_played= [50,60,70,80,90,100,110]
average_scores = [1000,2000,3000,4000,5000,6000,7000]
average_scores_ipl = [1500,2000,2500,3000,3500,4000,4500]

plt.plot(total_matches_played,average_scores,label="icc tournaments")
plt.plot(total_matches_played,average_scores_ipl,label="ipl tournament")
plt.plot(total_matches_played,average_scores)
plt.show()