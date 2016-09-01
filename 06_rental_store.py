customer = {
  "name": "martin",
  "rentals": [
    {"movieID": "F001", "days": 3},
    {"movieID": "F002", "days": 1},
  ]
}

movies = {
  "F001": {"title": "Ran",                      "code": "regular"},
  "F002": {"title": "Trois Couleurs: Bleu",     "code": "regular"},
}

def statement(customer, movies):
    totalAmount = 0
    frequentRenterPoints = 0
    result = 'Rental Record for ' + customer['name'] + '\n'

    for i in range(len(customer['rentals'])):
      r = customer['rentals'][i]
      movie = movies[r['movieID']]
      thisAmount = 0
  
      # determine amount for each movie
      if movie['code'] == "regular":
          thisAmount = 2
          if r['days'] > 2:
              thisAmount += (r['days'] - 2) * 1.5
      elif movie['code'] ==  "new":
          thisAmount = r['days'] * 3
      elif movie['code'] == "childrens":
          thisAmount = 1.5
          if r['days'] > 3:
              thisAmount += (r['days'] - 3) * 1.5
          
          break
      
  
      # add frequent renter points
      frequentRenterPoints += 1

      # add bonus for a two day new release rental
      if movie['code'] == "new" and r['days'] > 2: frequentRenterPoints += 1
  
      # print figures for this rental
      result += '\t' + movie['title'] + '\t' + str(thisAmount) + '\n'
      totalAmount += thisAmount
    
    # add footer lines
    result += 'Amount owed is ' + str(totalAmount) + '\n'
    result += 'You earned ' + str(frequentRenterPoints) + ' frequent renter points\n'
  
    return result



print statement(customer, movies)
assert statement(customer, movies) == """Rental Record for martin\n\tRan\t3.5\n\tTrois Couleurs: Bleu	2\nAmount owed is 5.5\nYou earned 2 frequent renter points\n"""
assert statement(customer, movies) == """Rental Record for martin
	Ran	3.5
	Trois Couleurs: Bleu	2
Amount owed is 5.5
You earned 2 frequent renter points
"""
