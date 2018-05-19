$(document).ready(() => {




// -------------------------------------
for ( var i = 0; i < itemMenus.length; i++){
    document.getElementById(itemMenus[i]).style.display = "none";
};
document.getElementById("Home").style.display = "block";

});


// alert below the navbar with database response
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

var itemMenus = ["imagesGet","imagesPut","imageDelete","imagesPost",
                "menuPut","menuDelete","menuGet","menuPost",
                "organizationEdit","organizationDelete","organizationsPost","organizationsGet",
                "groupPut","groupDelete","groupPost","groupGet",
                "userGet","userPost","userEdit","userDelete","Home"];


function get(idItemToOpen) {  
    var test = document.getElementById(idItemToOpen).style.display;
    if ( test != "block" ){
        for ( var i = 0; i < itemMenus.length; i++){
            document.getElementById(itemMenus[i]).style.display = "none";
        };
        document.getElementById(idItemToOpen).style.display = "block";
    //users -------------------------------
        if ( idItemToOpen == "userGet" ){
            getUsers(); 
        
        } else if ( idItemToOpen == "userPost" ){
            GetOrganizations("postInputOrganization");
            GetGroups("postInputGroup");
        
        } else if ( idItemToOpen == "userEdit" ){
            GetUsers("inputUserEdit");
            GetOrganizations("inputOrganizationPut");
            GetGroups("inputGroupPut");
        
        } else if ( idItemToOpen == "userDelete" ){
            GetUsers("deleteSelectUser");
    // groups ---------------------------------------------------
        } else if ( idItemToOpen == "groupPost" ){
            GetMenus("postInputMenuidGroup");
        
        } else if ( idItemToOpen == "groupPut" ){
            GetGroups("putSelectGroup");
            GetMenus("putInputMenuidGroup");
        
        } else if ( idItemToOpen == "groupDelete" ){
            GetGroups("deleteSelectGroup");
        
        } else if ( idItemToOpen == "groupGet" ){
            getGroup(); 
    // organizations ------------------------
        } else if ( idItemToOpen == "organizationsGet" ){
            getOrganization(); 
        
        } else if ( idItemToOpen == "organizationDelete" ){
            GetOrganizations("deleteSelectOrganization");
        
        } else if ( idItemToOpen == "organizationEdit" ){
            GetOrganizations("putSelectOrganization");
    // menus ------------------------------------------
        } else if ( idItemToOpen == "menuGet" ){
            getMenus();
        
        } else if ( idItemToOpen == "menuDelete" ){
            GetMenus("deleteSelectMenu");
        
        } else if ( idItemToOpen == "menuPut" ){
            GetMenus("editSelectMenu");

    // images -----------------------------------------
        } else if ( idItemToOpen == "imagesGet" ){
            getImages();
    
        } else if ( idItemToOpen == "imagesPut" ){
            GetImages("putSelectImage");
        
        } else if ( idItemToOpen == "imageDelete" ){
            GetImages("deleteSelectImage");
        }
    
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




