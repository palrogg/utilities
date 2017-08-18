# Memento

In progress, a list of handy commands.

## CRON

* To use a virtual environment:
`/Users/paul/.virtualenvs/dataanalysis/bin/python`

* To use UTF-8 and avoid problems with non-UTF8 chars:
`LANG=fr_FR.UTF-8`

Example:

```
5,25,55 * * * * LANG=fr_FR.UTF-8 /Users/paul/.virtualenvs/dataanalysis/bin/python /Users/paul/Notebooks/somescraper.py
```


## Useful Pandas commands

### Open non-UTF8 files

`df = pd.read_csv('thefile.csv', encoding=u'Windows 1252')`

### Show duplicates

```
df[df.duplicated()]

df[df.duplicated(subset=('col1', 'col2'))]

df[df['column'].duplicated()]

df.reset_index(inplace=True)
```

### Strings

`df[df['Textcolumn'].str.contains('Hey')]`

`df[df['Textcolumn'].str.match('^A')]`

### Resample, group by date

`df.groupby([lambda x: x.hour]).size().plot()`

`mdata = df.groupby([lambda x: x.month]).size()`

or

`mdata = df.groupby(by=df.index.month).size()`

## Current date
```
today_str = datetime.now().strftime("%Y-%m-%d")
2017-10-02
```


## Cartojs

### Load map with carto.js

//columbialibraries.carto.com/u/paulrong/**api/v2/viz**/aac3e918-6b3e-4e21-8235-b3bdb82d1b3e/**viz.json**
