import pandas as pd
import io
import  requests
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ardianugraha/datasets/master/olympics.csv"
download = requests.get(url).content

src = pd.read_csv(io.StringIO(donwload.decode('UTF-8')) )

print(src[0:5])


