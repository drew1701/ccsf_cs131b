#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 04: Task:
Show what portion of the global population has permanent
representation on the UN Security Council, show citations.
"""

# Source: UN.org: Security Council members
citation_p5 = 'https://www.un.org/securitycouncil/content/current-members'

# Source: data.worldbank.org: 2020 World Population Data
citation_pop = 'https://data.worldbank.org/indicator/SP.POP.TOTL'

# Set variables with population data from worldbank
pop_world = 7753000000
pop_china = 1402112000
pop_france = 67391582
pop_rus_fed = 144104080
pop_uk = 67215293
pop_us = 329484123

# Derive population of the permanent members, called p5
pop_p5 = pop_china + pop_france + pop_rus_fed + pop_uk + pop_us

# Find percent of global population with permanent representation
# added two decimal places to the rounded percent, per TA
perm_rep_pct = str(round((pop_p5 / pop_world) * 100, 2))

# Display Output with citations
print('\nThe United Nations Security Council currently has 15 members.')
print('Five of the members are permanent, and often called the P5.')
print('The five are: China, France, Russian Federation, the UK, and the US.\n')
print('In 2020, the P5 combined population was {:,}.'.format(pop_p5))
print('In 2020, the est. global population was {:,}.'.format(pop_world))
print('\nThereby, only ' + perm_rep_pct + '% of the world\'s population has permanent')
print('representation on the United Nations Security Council.')
print('\nUN Security Council data from un.org at:\n' + citation_p5)
print('\nPopulation numbers from data.worldbank.com at:\n' + citation_pop)
