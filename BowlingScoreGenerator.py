import sys
from prettytable import PrettyTable


def generate_score(name, rolls):
	for r in rolls:
		assert r.isdigit(), "Rolls contains something other than a positive integer."
		r = int(r)
		assert r <= 10 and r >= 0, "Rolls contains an impossible roll."

	score = 0
	frames = [0] * 10

	for x in range(0, 10):
		assert len(rolls) != 0, "Not enough rolls given."
		first_roll = int(rolls.pop(0))

		if first_roll == 10:
			assert len(rolls) >= 2, "Not enough rolls given."
			score += 10 + int(rolls[0]) + int(rolls[1])
			frames[x] = (('X',' '), score)
		else:
			assert len(rolls) != 0, "Not enough rolls given."
			second_roll = int(rolls.pop(0))

			assert first_roll + second_roll <= 10, "Impossible frame - sum of a frame is greater than 10 pins."
			if first_roll + second_roll == 10:
				assert len(rolls) >= 1, "Not enough rolls given."
				score += 10 + int(rolls[0])
				first_roll = first_roll if first_roll > 0 else '-'
				frames[x] = ((first_roll, '/'), score)
			else:
				score += first_roll + second_roll
				first_roll = first_roll if first_roll > 0 else '-'
				second_roll = second_roll if second_roll > 0 else '-'
				frames[x] = ((first_roll, second_roll), score)


	bonus_one = ' '
	bonus_two = ' '
	#case where last frame is a strike
	if frames[9][0][0] == 'X':
		assert len(rolls) == 2, "Too many rolls inputted."
		bonus_one = int(rolls.pop(0)) 
		bonus_two = int(rolls.pop(0)) 
		if bonus_one != 10:
			assert bonus_one + bonus_two <= 10, "Impossible bonus frame inputted."
		bonus_one = 'X' if bonus_one == 10 else bonus_one
		bonus_one = '-' if bonus_one == 0 else bonus_one
		bonus_two = 'X' if bonus_two == 10 else bonus_two
		bonus_two = '-' if bonus_two == 0 else bonus_two

	#case where last frame is a spare
	elif frames[9][0][1] == '/':
		assert len(rolls) == 1, "Too many rolls inputted."
		bonus_one = int(rolls.pop(0)) 
		bonus_one = 'X' if bonus_one == 10 else bonus_one
		bonus_one = '-' if bonus_one == 0 else bonus_one

	assert len(rolls) == 0, "Too many rolls inputted."
	frames.append(((bonus_one, bonus_two), ' '))
	
	t = PrettyTable(['Frame', 'Roll_One', 'Roll_Two', 'Score'])
	for frame in frames:
		t.add_row([(frames.index(frame) + 1) if (frames.index(frame) + 1) <= 10 else '*', frame[0][0], frame[0][1], frame[1]])
	return [score, t]

if __name__ == "__main__":
	name = sys.argv[1]
	rolls = sys.argv[2:]
	result = generate_score(name, rolls)
	print name + "s final score: " + str(result[0])
	print result[1]



