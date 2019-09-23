import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inputExcelFile = 'C://Exception//jack0608_Record.xlsx'

data = pd.read_excel(inputExcelFile)
count = data['purpose']
print(count)
test = data[count == '16']
test.sample(10)