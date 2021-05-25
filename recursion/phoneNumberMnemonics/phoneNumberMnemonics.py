def phoneNumberMnemonics(number):
	currCombination = ["0"] * len(number)
	combinations = []
	helper(0, number, currCombination, combinations)
	return combinations
	
def helper(idx, number, currCombination, combinations):
	if idx == len(number):
		currWord = "".join(currCombination)
		combinations.append(currWord)
		return
	digit = number[idx]
	letters = DIGIT_LETTERS[digit]
	for letter in letters:
		currCombination[idx] = letter
		helper(idx + 1, number, currCombination, combinations)
	
	
DIGIT_LETTERS = {
	"0": ["0"],
	"1": ["1"],
	"2": ["a", "b", "c"],
	"3": ["d", "e", "f"],
	"4": ["g", "h", "i"],
	"5": ["j", "k", "l"],
	"6": ["m", "n", "o"],
	"7": ["p", "q", "r", "s"],
	"8": ["t", "u", "v"],
	"9": ["w", "x", "y", "z"],
}

