from cmath import sqrt
import requests
import io
import pandas as pd

url = "https://raw.githubusercontent.com/dennisblaufuss/FS_MADS/main/Semester%202/Finance/Sp500.csv"
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')), sep=";")
df["return"] = df["Close"].pct_change()
# df["an return"] = (1 + df["return"]) ** (1/250) - 1

mu = df["return"].mean()
sigma = sqrt(df["return"].var())

mu_ann = (1 + mu) ** (1/250) - 1
sigma_ann = sigma * sqrt(250)


print('ass')
