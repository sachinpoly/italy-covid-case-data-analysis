#!/usr/bin/env python
# coding: utf-8

# In[128]:


from urllib.request import urlretrieve


# In[129]:


italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urlretrieve(italy_covid_url,'italy-covid-daywise.csv')


# In[130]:


import os


# In[132]:


import pandas as pd


# In[133]:


covid_df = pd.read_csv('./italy-covid-daywise.csv')


# In[134]:


covid_df


# In[135]:


type(covid_df)


# In[136]:


type(covid_df.new_cases)


# In[137]:


type(covid_df['new_cases'])


# In[138]:


covid_df['new_cases'][245]


# In[139]:


covid_df.at[245, 'new_cases']


# In[140]:


covid_df.new_cases


# In[141]:


covid_df['new_cases']


# In[142]:


cases_df  =covid_df[['date','new_cases']]


# In[143]:


cases_df


# In[144]:


covid_df_copy = covid_df.copy()


# In[145]:


covid_df_copy


# In[146]:


covid_df.loc[245]


# In[147]:


covid_df.loc[245:246]


# In[148]:


covid_df.loc[109:112]


# In[149]:


covid_df.new_tests.first_valid_index()


# In[150]:


covid_df.sample(5)


# In[151]:


total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

        


# In[152]:


print('total cases is {} and total deaths {}'.format(int(total_cases),int(total_deaths)))


# In[153]:


death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
death_rate


# In[154]:


print('death rate is {:.2f} %'.format(death_rate*100))


# In[155]:


initial_tests = 935310
tota_tests  = initial_tests + covid_df.new_tests.sum()
tota_tests


# In[156]:


positive_rate  = total_cases/tota_tests


# In[157]:


positive_rate


# In[158]:


print('positive rate is {:.3f} %'.format(positive_rate*100))


# In[159]:


high_new_cases = covid_df.new_cases > 1000
high_new_cases


# In[160]:


covid_df[high_new_cases]


# In[161]:


high_cases_df = covid_df[covid_df['new_cases'] > 1000]
high_cases_df


# In[162]:


high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]


# In[163]:


high_ratio_df.shape


# In[164]:


covid_df.new_cases / covid_df.new_tests


# In[165]:


covid_df['postive_rate'] = covid_df.new_cases/ covid_df.new_tests


# In[166]:


covid_df


# In[167]:


covid_df.drop(columns=['postive_rate'],inplace=True)


# In[168]:


covid_df


# In[169]:


covid_df.sort_values('new_cases', ascending=False).head(10)


# In[170]:


covid_df.sort_values('new_deaths',ascending=False).head(10)


# In[171]:


covid_df.sort_values('new_cases',ascending=True).head(10)


# In[172]:


covid_df.loc[168:174]
            


# In[173]:


covid_df.at[172,'new_cases'] = (covid_df.at[171,'new_cases']+covid_df.at[173,'new_cases'])/2


# In[174]:


covid_df.loc[168:174]


# In[175]:


covid_df.date


# In[177]:


covid_df['date'] = pd.to_datetime(covid_df.date)


# In[178]:


covid_df.date


# In[179]:


covid_df['year'] = pd.DatetimeIndex(covid_df.date).year


# In[180]:


covid_df


# In[181]:


covid_df['month'] = pd.DatetimeIndex(covid_df.date).month


# In[182]:


covid_df


# In[183]:


covid_df['day'] = pd.DatetimeIndex(covid_df.date).day


# In[184]:


covid_df


# In[185]:


covid_df['weekday']  = pd.DatetimeIndex(covid_df.date).weekday


# In[186]:


covid_df


# In[187]:


covid_df_may = covid_df[covid_df.month == 5]


# In[188]:


covid_df_may


# In[190]:


covid_df_may_metrics = covid_df_may[['new_cases','new_deaths','new_tests']]


# In[191]:


covid_df_may_metrics


# In[192]:


covid_df_may_total = covid_df_may_metrics.sum()


# In[193]:


covid_df_may_total


# In[197]:


type(covid_df_may_total)


# In[198]:


covid_df[covid_df.month == 5][['new_cases','new_deaths','new_tests']].sum()


# In[199]:


covid_df.new_cases.mean()


# In[201]:


covid_df.new_cases[covid_df.weekday == 6].mean()


# In[203]:


covid_df[covid_df.weekday == 6].new_cases.mean()


# In[214]:


covid_df_month = covid_df.groupby('month')[['new_cases','new_tests','new_deaths']].sum()
covid_df_month


# In[215]:


covid_df_mean_month = covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].mean()


# In[216]:


covid_df_mean_month


# In[217]:


covid_df['total_cases'] = covid_df.new_cases.cumsum()


# In[218]:


covid_df


# In[219]:


covid_df['total_deaths'] = covid_df.new_deaths.cumsum()


# In[220]:


covid_df


# In[221]:


covid_df['total_tests'] = covid_df.new_tests.cumsum()
covid_df


# In[222]:


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')


# In[223]:


location_df = pd.read_csv('./locations.csv')


# In[224]:


location_df


# In[225]:


location_df[location_df.location == 'Italy']


# In[226]:


covid_df['location']  =  'Italy'


# In[227]:


covid_df


# In[228]:


merged_df = covid_df.merge(location_df,on='location')


# In[229]:


merged_df


# In[230]:


merged_df['total_ceses_per_million'] = merged_df.total_cases* 1e6 /merged_df.population


# In[231]:


merged_df


# In[232]:


merged_df['total_deaths_per_million'] = merged_df.total_deaths*1e6/merged_df.population
merged_df['total_tests_per_million'] = merged_df.total_tests*1e6/merged_df.population


# In[233]:


merged_df


# In[234]:


results_df = merged_df[['date','new_cases','total_cases','new_tests','total_tests','new_deaths','total_deaths',
                       'total_deaths_per_million',
                       'total_tests_per_million',
                       'total_ceses_per_million']]


# In[235]:


results_df


# In[238]:


results_df.to_csv('result1.csv')


# In[239]:


results_df.new_cases.plot()


# In[240]:


results_df.set_index('date',inplace=True)


# In[241]:


results_df


# In[242]:


results_df.new_cases.plot()


# In[244]:


results_df.loc['2020-09-02']


# In[245]:


results_df.new_cases.plot()
results_df.new_deaths.plot();


# In[246]:


results_df.total_cases.plot()
results_df.total_deaths.plot();


# In[247]:


death_rate = results_df.total_deaths/results_df.total_cases


# In[248]:


death_rate.plot(title="Death Rate")


# In[252]:


positive_rate = results_df.total_cases/results_df.total_tests


# In[253]:


positive_rate.plot(title='po_rate')


# In[254]:


covid_df_month.new_cases.plot(kind='bar')


# In[255]:


covid_df_month.new_tests.plot(kind='bar')


# In[ ]:




