function check(){
	n=document.getElementById("number").value;
	if(!NaN(n)){
		if(n%3==0 && n%7==0){
			document.getElementById("result").innerHTML=n+" is divisible by both 3 and 7";
		}
		else if(n%3==0){
			 document.getElementById("result").innerHTML=n+" is divisible by 3";
		}
		else if(n%7==0){
			 document.getElementById("result").innerHTML=n+" is divisible by 7";
		}
	}
		else{
			 document.getElementById("result").innerHTML="Please enter a valid number";
		}
}