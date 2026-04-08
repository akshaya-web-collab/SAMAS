# WEEK 11: Pandas Basics

import pandas as pd

data = {
    "Crop": ["Rice", "Wheat"],
    "Moisture": [40, 35]
}

df = pd.DataFrame(data)

print(df)