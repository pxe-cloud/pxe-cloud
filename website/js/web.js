$(document).ready(() => {

// var itemMenus = ["userGet","userPost","userEdit","userDelete","Home"];

// for ( var i = 0; i < itemMenus.length; i++){
//     document.getElementById(itemMenus[i]).style.display = "none";
// };
// document.getElementById("Home").style.display = "block";

// -------------------------------------
    
// -----------------------------------------------------------
 
});

// delete user ----------------------------------------------------

function deleteUser(){
    
    var user = document.querySelector("#deleteInputUser").value;
        
    $.ajax({
        type: "DELETE",
        url: "http://10.252.2.2:8001/user/" + user,
             
        }).done(function (response) {
                //document.getElementById("demo").innerHTML =  response.response;
                console.log(response.response);

         });

};


// edit users ----------------------------------------------------
// TODO poner bonita la respuesta
function editUser(){
    
    var pass = document.querySelector("#putInputPassword").value;
    var user = document.querySelector("#putInputUser").value;
    var group = document.querySelector("#inputGroupPut").value;
    var organization = document.querySelector("#inputOrganizationPut").value;
    
    $.ajax({
        type: "PUT",
        url: "http://10.252.2.2:8001/user/" + user,
        data : {'password': pass, 'organization': organization, 'group': group},
        
        
        }).done(function (response) {
                //document.getElementById("demo").innerHTML =  response.response;
                console.log(response.response);
                
            });

    
    

};

function putGroupUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/groups",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            var groupList = list[i]['name'].length;  
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.getElementById("inputGroupPut").appendChild(newlink);
        ;}
    });
}

function putOrganizationUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/organizations",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            var groupList = list[i]['name'].length;  
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.getElementById("inputOrganizationPut").appendChild(newlink);
        ;}
    });
}

// ---------------------------------------------------------------------------

// post users --------------------------------------------------------------
function postUser(){
    
    var pass = document.querySelector("#postInputPassword").value;
    var confirm = document.querySelector("#postInputConfirm").value;
        

    if ( pass == confirm ){ 
        
        var user = document.querySelector("#postInputUser").value;
        var group = document.querySelector("#postInputGroup").value;
        var organization = document.querySelector("#postInputOrganization").value;
        
        // TODO no coge grupos y orgasnizaciones
        $.ajax({
            type: "POST",
            url: "http://10.252.2.2:8001/users",
            data : {'username':user, 'organization': organization, 'password': pass, 'group': organization},
            
            
             }).done(function (response) {
                     document.getElementById("demo").innerHTML =  response.response;
                     
        });
    
    } else {
        
        document.getElementById("demo").innerHTML =  "password does not match";

    }

}

function postGroupUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/groups",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            var groupList = list[i]['name'].length;  
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.querySelector("#postInputGroup").appendChild(newlink);
        };
    });
}

function postOrganizationUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/organizations",
        "method": "GET",
        "headers": {}
    };

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            var groupList = list[i]['name'].length;  
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.querySelector("#postInputOrganization").appendChild(newlink);
        };
    });
}

//------------------------------------------------------



// get users -----------------------------------------------------
function getUsers(){

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/users",
        "method": "GET",
        "headers": {}
    }
    
    $.ajax(settings).done(function (response) {
  

        var list = response.response;
        var len = response.response.length;
        for (var i = 0; i < len; i++ ) {
            console.log(list[i]['username']);
            
            
            var username = list[i]['username'];
     

            newlink = document.createElement('a');
            newlink.setAttribute('class',"list-group-item list-group-item-info mb-2");
            newlink.setAttribute('href', '#');
            newlink.setAttribute('id', username);
            var t = document.createTextNode(list[i]['username']);
            newlink.appendChild(t);
            document.getElementById("listUsers").appendChild(newlink);

            var groupList = list[i]['groups'].length;
            for ( var x = 0; x < groupList; x++){
                console.log(list[i]['groups'][x]);

                if ( x == 0 ){
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
                    newlink.setAttribute('id', "group" + username);
                    var t = document.createTextNode("Groups");
                    newlink.appendChild(t);
                    document.getElementById(username).appendChild(newlink);    
                };
                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item list-group-item-action ");                
                var t = document.createTextNode(list[i]['groups'][x]);
                newlink.appendChild(t);
                document.getElementById("group" + username ).appendChild(newlink);
            };
            
            
            var organizationList = list[i]['organizations'].length;
            for ( var z = 0; z < organizationList; z++){
                console.log(list[i]['organizations'][z]);

                if ( z == 0 ){
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
                    newlink.setAttribute('id', "organization" + username);
                    var t = document.createTextNode("Organizations");
                    newlink.appendChild(t);
                    document.getElementById(username).appendChild(newlink);    
                };

                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item list-group-item-action ");                
                var t = document.createTextNode(list[i]['organizations'][z]);
                newlink.appendChild(t);
                document.getElementById("organization" + username).appendChild(newlink);
            }
        

        }; 

    
   
    });

};





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
                     console.log(response);
                    //  document.getElementById("demo").innerHTML =  response.response;
        
        });
    
    } else {
        
        document.getElementById("demo").innerHTML =  "password does not match";

    }

}



// change to menus in web.html

// var itemMenus = ["userGet","userPost","userEdit","userDelete","groupGet","groupPost","groupEdit","groupDelete",
// "organizationGet","organizationPost","organizationPut","organizationDelete","Home"];
var itemMenus = ["groupGet","userGet","userPost","userEdit","userDelete","Home"];


function functionGroupGet() {
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("groupGet").style.display = "block";
    getGroup();
};

function functionHome() {
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("Home").style.display = "block";
};

function functionUserPost() {
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("userPost").style.display = "block";
    postGroupUsers();
    postOrganizationUsers();
};

function functionUserEdit() {
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("userEdit").style.display = "block";
    putGroupUsers();
    putOrganizationUsers();
    
};

function functionUserGet() {
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("userGet").style.display = "block";
    getUsers();
};

function functionUserDelete() {
    
    for ( var i = 0; i < itemMenus.length; i++){
        document.getElementById(itemMenus[i]).style.display = "none";
    };
    document.getElementById("userDelete").style.display = "block";
};


