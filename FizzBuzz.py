#FIZZBUZZ

print '''Hi This is the game FizzBuzz
 In case a number is divisible with 3, the diplay will show "fizz" instead of the number.
 If a number is divisible with 5, it prints "buzz".
 If it's divisible with both 3 and 5, it prints "fizzbuzz".'''

x = 0

while True:

    Number = int(raw_input('Please, enter a number between 1 and 100:'))

    if 1 <= Number <= 100:

        for x in range(Number):
            x += 1
            if x % 3 == 0 and x % 5 == 0:
                print "FizzBuzz"
            elif x % 3 == 0:
                print "Fizz"
            elif x % 5 == 0::
                print "Buzz"
            else:
                print x
    else:
        print "Please, enter a number between 1 and 100"
 
