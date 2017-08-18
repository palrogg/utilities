# CRON

* To use a virtual environment:
`/Users/paul/.virtualenvs/dataanalysis/bin/python`

* To use UTF-8 and avoid problems with non-UTF8 chars:
`LANG=fr_FR.UTF-8`

Example:

`5,25,55 * * * * LANG=fr_FR.UTF-8 /Users/paul/.virtualenvs/dataanalysis/bin/python /Users/paul/Notebooks/somescraper.py`


# Useful Pandas commands

```
df[df.duplicated()]
df[df['column'].duplicated()]

df.reset_index(inplace=True)
```


# Current date
```today_str = datetime.now().strftime("%Y-%m-%d")
2017-10-02```
