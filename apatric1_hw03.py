#!/usr/bin/env python3

"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 03: Task:
Show how Idaho has better representation in the
senate than Florida based on population
"""

# population numbers from us census website
pop_idaho = 1839106
pop_florida = 21538187
pop_compare = round(pop_florida / pop_idaho)

# citations for census data
citation_id = 'https://www.census.gov/quickfacts/fact/table/ID/POP010220'
citation_fl = 'https://www.census.gov/quickfacts/fact/table/FL/POP010220'

# using placeholders in txt strings for number formatting
txt_pop_id = 'In 2020 the population of Idaho was {:,}.'
txt_pop_fl = 'In 2020 the population of Florida was {:,}.'
txt_rep_id = 'In Idaho each senator has to represent {:,} citizens.'
txt_rep_fl = 'In Florida each senator has to represent {:,} citizens.'

print('In the U.S., all states have exactly 2 senators.')
print(txt_pop_id.format(pop_idaho))
print(txt_pop_fl.format(pop_florida))
print('Florida has roughly', pop_compare, 'times more people than Idaho,')
print(' yet they both have the same number of senators.')
print(txt_rep_id.format(pop_idaho/2))
print(txt_rep_fl.format(pop_florida/2))
print('\nThe US Census info for Idaho is available at:')
print(citation_id)
print('\nThe US Census info for Florida is available at:')
print(citation_fl)
