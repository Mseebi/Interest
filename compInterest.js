function compound(principal, intRate, noOfPay){
	var inter = intRate / 100;
	console.log(inter);
	var finalAmount = principal * (Math.pow(1 + (inter / noOfPay), noOfPay));
	return finalAmount;
}
console.log(compound(5000, 5, 12));
