#!/usr/bin/env python
# coding: utf-8

# # Чуйкин Никита
# # Минипроект 'Hotel'

# # Задачи:

# 1) Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные.
# 
# 2) Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.
# 
# 3) Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.
# 
# 4) На сколько ночей в среднем бронируют отели разных типов?
# 
# 5) Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?
# 
# 6) Проанализируйте даты запланированного прибытия. – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?– Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов
# 
# 7) Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
# 
# 8) Создайте колонку total_kids, объединив children и babies. Для отелей какого типа среднее значение переменной оказалось наибольшим?
# 
# 9) Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), в противном случае – False. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (метрика - churn rate). Укажите, среди какой группы показатель выше.

# # Задание № 1
# Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные.

# In[2]:


import pandas as pd


# In[3]:


bookings = pd.read_csv('/home/jupyter-n-chujkin/shared/homeworks/python_ds_miniprojects/2/bookings.csv', sep=';')


# In[4]:


bookings_head = bookings.head(7)


# In[5]:


bookings_head


# In[6]:


bookings_head.dtypes


# In[7]:


bookings


# # Задание № 2
# Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.

# In[10]:


bookings.columns


# In[11]:


bookings = bookings.rename(columns={'Hotel': 'hotel',
                         'Is Canceled': 'is_canceled',
                         'Lead Time': 'lead_time',
                         'arrival full date': 'arrival_full_date',
                         'Arrival Date Month': 'arrival_date_month',
                         'Arrival Date Year': 'arrival_date_year',
                         'Arrival Date Week Number': 'arrival_date_week_number',
                         'Stays in Weekend nights': 'stays_in_weekend_nights',
                         'Stays in week nights': 'stays_in_week_nights',
                         'stays total nights': 'stays_total_nights',
                         'Adults': 'adults',
                         'Children': 'children',
                         'Babies': 'babies',
                         'Meal': 'meal',
                         'Country': 'country',
                         'Reserved Room Type': 'reserved_room_type',
                         'Assigned room type': 'assigned_room_type',
                         'customer type': 'customer_type',
                         'Reservation Status': 'reservation_status',
                         'Reservation status_date': 'reservation_status_date',
                         'Arrival Date Day of Month': 'arrival_date_day_of_month'})


# # Задание № 3
# Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.

# In[14]:


bookings['is_canceled']     .value_counts(dropna=False)


# In[15]:


bookings     .query('is_canceled < 1')     .groupby(['country','is_canceled'], as_index=False)     .agg({'is_canceled': 'count'})     .sort_values('is_canceled', ascending=False)


# # Задание № 4
# На сколько ночей в среднем бронируют отели разных типов?

# In[16]:


bookings     .query('is_canceled < 1')     .query("hotel == 'Resort Hotel'")     .groupby(['hotel', 'is_canceled'], as_index=False)     .agg({'stays_total_nights': 'mean'})     .round(2)     .sort_values('is_canceled', ascending=False)


# In[17]:


bookings     .query("hotel == 'Resort Hotel'")     .groupby(['hotel'], as_index=False)     .agg({'stays_total_nights': 'mean'})     .round(2)


# In[18]:


bookings     .query('is_canceled < 1')     .query("hotel == 'City Hotel'")     .groupby(['hotel', 'is_canceled'], as_index=False)     .agg({'stays_total_nights': 'mean'})     .round(2)     .sort_values('is_canceled', ascending=False)


# In[19]:


bookings     .query("hotel == 'City Hotel'")     .groupby(['hotel'], as_index=False)     .agg({'stays_total_nights': 'mean'})     .round(2) 


# # Задание № 5
# Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?

# In[42]:


bookings     .query("reserved_room_type != assigned_room_type")
    


# # Задание № 6
# Проанализируйте даты запланированного прибытия. – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?– Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов

# In[21]:


bookings     .query("arrival_date_year == '2016'")     .groupby(['arrival_date_year', 'arrival_date_month', 'is_canceled'], as_index=False)     .agg({'is_canceled': 'sum'})     .sort_values('is_canceled', ascending=False)


# In[22]:


bookings     .query("arrival_date_year == '2017'")     .groupby(['arrival_date_year', 'arrival_date_month', 'is_canceled'], as_index=False)     .agg({'is_canceled': 'sum'})     .sort_values('is_canceled', ascending=False)


# In[23]:


bookings     .query('is_canceled > 0')     .query("hotel == 'City Hotel'")     .query("arrival_date_year == '2015'")     .groupby(['hotel', 'arrival_date_month', 'is_canceled'], as_index=False)     .agg({'is_canceled': 'sum'})     .sort_values('is_canceled', ascending=False)


# In[24]:


bookings     .query('is_canceled > 0')     .query("hotel == 'City Hotel'")     .query("arrival_date_year == '2016'")     .groupby(['hotel', 'arrival_date_month', 'is_canceled'], as_index=False)     .agg({'is_canceled': 'sum'})     .sort_values('is_canceled', ascending=False)


# In[25]:


bookings     .query('is_canceled > 0')     .query("hotel == 'City Hotel'")     .query("arrival_date_year == '2017'")     .groupby(['hotel', 'arrival_date_month', 'is_canceled'], as_index=False)     .agg({'is_canceled': 'sum'})     .sort_values('is_canceled', ascending=False) 


# # Задание № 7
# Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?

# In[26]:


bookings[['adults', 'children', 'babies']]     .mean()     .idxmax()


# # Задание № 8
# Создайте колонку total_kids, объединив children и babies. Для отелей какого типа среднее значение переменной оказалось наибольшим?

# In[27]:


bookings['total_kids'] = bookings[['children', 'babies']].sum(axis=1)


# In[28]:


bookings     .query("hotel == 'City Hotel'")     .groupby(['hotel'], as_index=False)     .agg({'total_kids': 'mean'})     .round(2)


# In[29]:


bookings     .query("hotel == 'Resort Hotel'")     .groupby(['hotel'], as_index=False)     .agg({'total_kids': 'mean'})     .round(2)


# # Задание № 9
# Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), в противном случае – False. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (метрика - churn rate). Укажите, среди какой группы показатель выше.

# In[30]:


bookings['has_kids'] = bookings['total_kids']


# In[31]:


bookings = bookings.astype({"has_kids": "Int64"})


# In[32]:


bookings.has_kids = bookings.total_kids > 0


# In[33]:


bookings


# In[34]:


bookings     .query('has_kids == True')     .groupby(['has_kids', 'is_canceled'], as_index=False)     .agg({'has_kids': 'count'})


# In[41]:


round((3259 / (3259 + 6073))*100, 2)


# In[36]:


bookings     .query('has_kids == False')     .groupby(['has_kids', 'is_canceled'], as_index=False)     .agg({'has_kids': 'count'})


# In[40]:


round((40965 / (69093+40965))*100, 2)

