require 'date'
# a date

puts Date.today

#comparison

puts Date.parse("2010-10-2") < Date.today

#this also works

puts Date.parse("5-3-2014") == Date.today

puts Date.today.day
puts Date.today.month
puts Date.today.year

