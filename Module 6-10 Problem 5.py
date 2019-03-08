def categorize_study(p_value, requirements):
  bs_factor = 1
  if requirements >= 6:
       bs_factor = 1
  elif requirements == 5:
       bs_factor = 2
  elif requirements == 4:
       bs_factor = 4
  elif requirements <= 3:
       bs_factor = 8
  elif p_value * bs_factor < .05:
        return 'Fine'
  elif p_value * bs_factor >= .05 and p_value * bs_factor <= .15:
        return 'Needs review'
  elif p_value * bs_factor > .15:
        return 'Pants on fire'
  elif requirements == 0:
        return 'Needs review'

print(categorize_study(.01,3))