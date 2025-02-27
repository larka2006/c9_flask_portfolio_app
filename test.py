@app.route('/guess_number', methods=['GET','POST'])
def guess_number_post():
	if request.method == 'GET':
	  	return render_template('guess_number.html')
	elif request.method == 'POST':
  	     secretNumber = random.randint(1, 30)
             print('I am thinking of a number between 1 and 30.')
	     print(request.form['text'])
# Ask the player to guess 6 times.
         for guessesTaken in range(1, 7):
	    print('Take a guess.')
	    guess = int(input())
	    if guess < secretNumber:
	        print('Your guess is too low.')
    	    elif guess > secretNumber:
		print('Your guess is too high.')
            else:
                break    # This condition is the correct guess!
            if guess == secretNumber:
                 print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
            else:
                 print('Nope. The number I was thinking of was ' + str(secretNumber))
