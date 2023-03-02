import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from matplotlib import cm
from datetime import datetime
import glob
import os
import json
import pickle
import six

sns.set() #sets the theme of graphs
pd.set_option('display.max_columns', None) #set the value of max columns to unlimited
pd.set_option('display.max_rows', None) #set the value of max rows to unlimited
pd.options.mode.chained_assignment = None #

AllCSV = [i for i in glob.glob('*.{}'.format('.csv'))]
AllCSV

#link to dataset
#https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download&select=CA_category_id.json