$(document).ready(() => {

// var itemMenus = ["userGet","userPost","userEdit","userDelete","Home"];

// for ( var i = 0; i < itemMenus.length; i++){
//     document.getElementById(itemMenus[i]).style.display = "none";
// };
// document.getElementById("Home").style.display = "block";

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
            url: "http://10.252.2.2:8001/users",
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

function functionImagesGet() {
    var test = document.getElementById("imagesGet").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("imagesGet").style.display = "block";
        getImages();
    }
};

function functionImagesEdit() {
    var test = document.getElementById("imagesPut").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("imagesPut").style.display = "block";
        putImageSelect();
    }
};

function functionImagesDelete() {
    var test = document.getElementById("imageDelete").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("imageDelete").style.display = "block";
        deleteImageSelect();
    }
};

function functionImagesPost() {
    var test = document.getElementById("imagesPost").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("imagesPost").style.display = "block";
    }
};

function functionMenuEdit() {
    var test = document.getElementById("menuPut").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("menuPut").style.display = "block";
        putSelectMenus();
    }
};

function functionMenuDelete() {
    var test = document.getElementById("menuDelete").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("menuDelete").style.display = "block";
        deleteSelectMenus();
    }
};

function functionMenuGet() {
    var test = document.getElementById("menuGet").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("menuGet").style.display = "block";
        getMenus();
    }
};

function functionMenuPost() {
    var test = document.getElementById("menuPost").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("menuPost").style.display = "block";
    }
};

function functionOrganizationEdit() {
    var test = document.getElementById("organizationEdit").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("organizationEdit").style.display = "block";
        putOrganizationSelect();
    }
};

function functionOrganizationDelete() {
    var test = document.getElementById("organizationDelete").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("organizationDelete").style.display = "block";
        deleteOrganizationSelect();
    }
};

function functionOrganizationPost() {
    var test = document.getElementById("organizationsPost").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("organizationsPost").style.display = "block";
    }
};

function functionOrganizationGet() {
    var test = document.getElementById("organizationsGet").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("organizationsGet").style.display = "block";
        getOrganization();
    }
};

function functionGroupEdit() {
    var test = document.getElementById("groupPut").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("groupPut").style.display = "block";
        putGroupSelectGroup();
        putGroupSelectMenus();
    }
};

function functionGroupDelete() {
    var test = document.getElementById("groupDelete").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("groupDelete").style.display = "block";
        deleteGroupSelectGroup();
    }
};

function functionGroupPost() {
    var test = document.getElementById("groupPost").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("groupPost").style.display = "block";
        postGroupSelectMenus();
    }
};

function functionGroupGet() {
    var test = document.getElementById("groupGet").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("groupGet").style.display = "block";
        getGroup();
    }
};

function functionHome() {
    
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("Home").style.display = "block";
    
};

function functionUserPost() {
    var test = document.getElementById("userPost").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("userPost").style.display = "block";
        postGroupUsers();
        postOrganizationUsers();
    }
};

function functionUserEdit() {
    var test = document.getElementById("userEdit").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("userEdit").style.display = "block";
        putGroupUsers();
        putOrganizationUsers();
        editUserSelect();
    }
};

function functionUserGet() {
    var test = document.getElementById("userGet").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("userGet").style.display = "block";
        getUsers();
    }
};

function functionUserDelete() {
    var test = document.getElementById("userDelete").style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById("userDelete").style.display = "block";
        deleteUserSelectGroup();
    }
};


