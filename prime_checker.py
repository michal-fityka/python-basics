def prime_checker(number):
  if number == 1:
    print (f"It is not a prime number")
  if number > 1:
    for i in range(2,number):
      if number % i == 0:
        print (f"It is not a prime number")
        break
    else:
      print (f"It is a prime number")
