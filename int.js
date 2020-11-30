//formula (interest/no. of payments)*loan principal = interest

function interest(interestRate, payments, principal){
	var rate = interestRate / 100;
	var finalAmount = (rate/payments) * principal;
	return finalAmount;
}

console.log(interest(3, 12, 5000));
