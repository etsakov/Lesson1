def get_answer(greetings):
	answers={
	    "привет": "И тебе привет!",
	    "как дела": "Лучше всех",
	    "пока": "Увидимся"
	}
	
	return answers.get(greetings)
print(get_answer('привет').lower())