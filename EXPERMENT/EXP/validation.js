function validation() {
    // Regex to check valid
    // VisaCard_Number 
    let CCNO = document.getElementById('CNo');
    let regex = new RegExp(/^4[0-9]{12}(?:[0-9]{3})?$/);
    
    // if VisaCard_Number
    // is empty return false
    if (CCNO == null) {
    return "false";
    }
    
    // Return true if the VisaCard_Number
    // matched the ReGex
    if (regex.test(CCNO) == true) {
    return "true";
    }
    else {
    return "false";
    }

    // card Exp.date format
    let CCEXP = document.getElementById('ExpDate');
    let ExpRegex = new ExpRegex(/\b(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})\b/);

    if (CCEXP == null) {
        return "false";
    } 

    if (ExpRegex.test(CCEXP) == true) {
        return "true";
    }
    else {
        return"false";
    }

}