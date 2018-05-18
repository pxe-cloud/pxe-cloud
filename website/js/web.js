$(document).ready(() => {
    

// -------------------------------------
for ( var i = 0; i < itemMenus.length; i++){
    document.getElementById(itemMenus[i]).style.display = "none";
};
document.getElementById("Home").style.display = "block";

    
// -----------------------------------------------------------


});




// registry user page registry -----------------------------------------

function functionRegistry(){
    
    var pass = document.querySelector("[name=password]").value;
    var confirm = document.querySelector("[name=confirmPasswors]").value;
        

    if ( pass == confirm ){ 
        
        var user = document.querySelector("[name=username]").value;
        
        $.ajax({
            type: "POST",
            url: config() + "/users",
            data : {'username':user,
                    'password': pass},
            
            
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

// change to menus in web.html

var itemMenus = ["imagesGet","imagesPut","imageDelete","imagesPost","menuPut","menuDelete","menuGet","menuPost","organizationEdit","organizationDelete","organizationsPost","organizationsGet","groupPut","groupDelete","groupPost","groupGet","userGet","userPost","userEdit","userDelete","Home"];


function get(idItemToOpen) {  
    var test = document.getElementById(idItemToOpen).style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById(idItemToOpen).style.display = "block";
        getImages();
        putImageSelect();
        deleteImageSelect();
        putSelectMenus();
        deleteSelectMenus();
        getMenus();
        putOrganizationSelect();
        deleteOrganizationSelect();
        getOrganization();
        putGroupSelectGroup();
        putGroupSelectMenus();
        deleteGroupSelectGroup();
        postGroupSelectMenus();
        getGroup();
        postGroupUsers();
        postOrganizationUsers();
        putGroupUsers();
        putOrganizationUsers();
        editUserSelect();
        getUsers();
        deleteUserSelectGroup();
    }
};

window.onload = function() {
    var reloading = sessionStorage.getItem("reloading");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        var idItemToOpen = sessionStorage.getItem('destination');
        this.sessionStorage.removeItem('destination')
        get(idItemToOpen);
    }
}


function reloadAndOpen(idItemToOpen) {
    sessionStorage.setItem("reloading", "true");
    sessionStorage.setItem('destination', idItemToOpen)
    document.location.reload();
}




