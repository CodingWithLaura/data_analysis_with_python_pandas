import numpy as np
import pandas as pd

#creating a series by passing a list of values, panda creates a default and changeable integer index
series = pd.Series(["cake", "cookies", "icecream"])

#customize indices
series = pd.Series(["cake", "cookies", "icecream"], index=["I like:", "I love:", "I'm addicted to:"])
print(series)
