
function FunctionLogin(){
        $(document).ready(function(){
            $("#myBtn").click(function(){
                $("#myModal").modal();
            });
        });
}

function functionPass(){
    window.location.assign("./web.html");
}


// registry user page registry -----------------------------------------

function functionRegistry(){
    
    var pass = document.querySelector("[name=password]").value;
    var confirm = document.querySelector("[name=confirmPasswors]").value;
        

    if ( pass == confirm ){ 
        
        var user = document.querySelector("[name=username]").value;
        var email = document.querySelector("#registrytEmail").value;
        
        $.ajax({
            type: "POST",
            url: config() + "/users",
            data : {'username':user,
                    'password': pass,
                    'email': email
                    },
            
            
             }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);

        });
    
    } else {
        var answer =  "Error, password does not match";
        functionAlert(answer);
    }

}

function functionAlert(answer){
    if (answer.indexOf("Succes") > -1 ){
        var tipe = "alert alert-success";
        var alert = answer;
    } else if ( answer.indexOf("Error") > -1 ){
        var tipe = "alert alert-danger";
        var alert = answer;
    }
    
	var newlink = document.createElement('div');
    newlink.setAttribute('class', tipe);                  
	newlink.setAttribute('id', "Alert");  
	document.querySelector("#demoAlert").appendChild(newlink);
                  
	var newlink = document.createTextNode(alert);
	document.querySelector("#Alert").appendChild(newlink);
}