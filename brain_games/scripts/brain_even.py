def even_game():
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name?')
    print('Hello, {}'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = randint(1, 10)
    print('Question: {}'.format(question))
