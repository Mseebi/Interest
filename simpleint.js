

function int(principal, interestRate, numOfYears){
	var rate = interestRate/100;
	var a = principal * (1 + rate*numOfYears);
	return a;
}

console.log(int(5000, 5, 1)); 
