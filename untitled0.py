# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14LK-cZYEjkZrPfDInejgxl6CnTtimsp8
"""

import numpy as np

# 1.Massiv yaratish
array_1d=np.array([1,2,3,4,5])
array_2d=np.array([[1,2,3],[4,5,6]])

# 2.Matematik operatsiyalar
sum_array = np.sum(array_1d)
mean_array=np.mean(array_1d)
product_array=np.prod(array_1d)

print("1D Massiv: ", array_1d)
print("2D Massiv:\n",array_2d)
print("Massivlar yig'indisi: ",sum_array)
print("O'rtacha: ",mean_array)
print("Ko'paytma: ", product_array)

sum2_array = np.sum(array_2d)
mean2_array=np.mean(array_2d)
product2_array=np.prod(array_2d)

print("1D Massiv: ", array_1d)
print("2D Massiv:\n",array_2d)
print("Massivlar yig'indisi: ",sum2_array)
print("O'rtacha: ",mean2_array)
print("Ko'paytma: ", product2_array)

import pandas as pd

# 1. DataFrame yaratish
data = {
    'ism': ['Ali', 'Vali', 'Sardor', 'Muhammadsodiq', 'Diyorjon', 'Munisbek', 'Azizbek', 'Muhammadtoir', 'Firdavs', 'Asadbek'],
    'Yoshi': [25, 30, 22, 18, 19, 20, 21, 23, 24, 28],
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Surxandaryo', 'Fargona', 'Andijon', 'Namangan', 'Fargona', 'Jizzax', 'Toshkent']
}

df = pd.DataFrame(data)

# 2. Ma'lumotlarni ko'rish
print(df)

# 3. Filtirlash: 20 yoshdan kichiklar
young_people = df[df['Yoshi'] < 20]
print("20 yoshdan kichiklar:\n", young_people)

# 4. Yoshi ustunini yangilash
df['Yoshi'] += 1
print("Yangilangan DataFrame:\n", df)

# 5. Fargonada yashaydiganlarni chiqarish
fargona_people = df[df['Shahar'] == 'Fargona']
print("Fargonada yashaydiganlar:\n", fargona_people)