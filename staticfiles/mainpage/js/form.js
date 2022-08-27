
var fields = {};

document.addEventListener("DOMContentLoaded", function() {
 fields.userName = document.getElementById('userName');
 fields.userSubject = document.getElementById('userSubject');
 fields.userEmail = document.getElementById('userEmail');
 fields.userPhone = document.getElementById('userPhone');
 fields.userMessage = document.getElementById('userMessage');
})

function isNotEmpty(value) {
 if (value == null || typeof value == 'undefined' ) return false;
 return (value.length > 0);
}

function isNumber(num) {
 return (num.length > 0) && !isNaN(num);
}

function isEmail(email) {
 let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
 return regex.test(String(email).toLowerCase());
}

function fieldValidation(field, validationFunction) {
 if (field == null) return false;

 let isFieldValid = validationFunction(field.value)
 if (!isFieldValid) {
 field.userName = 'placeholderRed';
 } else {
 field.userName = '';
 }

 return isFieldValid;
}

function isValid() {
 var valid = true;
 
 valid &= fieldValidation(fields.userName, isNotEmpty);
 valid &= fieldValidation(fields.userSubject, isNotEmpty);
 valid &= fieldValidation(fields.userEmail, isEmail);
 valid &= fieldValidation(fields.userPhone, isNumber);
 valid &= fieldValidation(fields.userMessage, isNotEmpty);

 return valid;
}

class User {
 constructor(userName, userSubject, userEmail, userPhone, userMessage) {
 this.userName = userName;
 this.userSubject = userSubject;
 this.userEmail = userEmail;
 this.userPhone = userPhone;
 this.userMessage = userMessage;
 }
}

function sendContact() {
	if (isValid()) {
		let usr = new User(userName.value, userSubject.value, userEmail.value, userPhone.value, userMessage.value);

		alert("Thanks for registering interest in the fund.")
	} else {
		alert("There was an error processing your message")
	}
}



