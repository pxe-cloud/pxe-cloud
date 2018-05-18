
// delete user ----------------------------------------------------

function deleteUser(){
    
    var user = document.querySelector("#deleteSelectUser").value;
        
    $.ajax({
        type: "DELETE",
        url: config() + "/user/" + user,
             
        }).done(function (response) {

            var answer = response.response;
            console.log(answer);
            functionAlert(answer);

         });

};
function deleteUserSelectGroup(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/users",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['username']);                
            var t = document.createTextNode(list[i]['username']);
            newlink.appendChild(t);
            document.getElementById("deleteSelectUser").appendChild(newlink);
        ;}
        
    });
}

// edit users ----------------------------------------------------

function editUser(){
    
    var user = document.querySelector("#inputUserEdit").value;
    var pass = document.querySelector("#putInputPassword").value;
    var group = document.querySelector("#inputGroupPut").value;
    var organization = document.querySelector("#inputOrganizationPut").value;
        
    $.ajax({
        type: "PUT",
        url: config() + "/user/" + user,
        data : {'password': pass, 'organization': organization, 'group': group},
        
        
        }).done(function (response) {
            var answer = response.response;
            functionAlert(answer);
                
            });

};

function editUserSelect(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/users",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['username']);                
            var t = document.createTextNode(list[i]['username']);
            newlink.appendChild(t);
            document.getElementById("inputUserEdit").appendChild(newlink);
        ;}
    });
}


function putGroupUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/groups",
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
        "url": config() + "/organizations",
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
                
        $.ajax({
            type: "POST",
            url: config() + "/users",
            data : {'username':user, 'organization': organization, 'password': pass, 'group': organization},
            
            
             }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                     
        });
    
    } else {
        var answer = "Error, password does not match";
        functionAlert(answer);

    }

}

function postGroupUsers(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/groups",
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
        "url": config() + "/organizations",
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
        "url": config() + "/users",
        "method": "GET",
        "headers": {}
    }
    
    $.ajax(settings).done(async function (response) {
  

        var list = response.response;
        var len = response.response.length;
        for (var i = 0; i < len; i++ ) {          
            
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
                if (  list[i]['groups'][0] != null ){
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
                                
                    var texts = await uerGetGroups(list[i]['groups'][x]);
                    //var texts = await uerGetGroups(list[i]['group']);
                    //  cambiar group y groups
                    var t = document.createTextNode(texts);
                    //var t = document.createTextNode(list[i]['groups'][x]);
                    newlink.appendChild(t);
                    document.getElementById("group" + username ).appendChild(newlink);
                };
            };
            
            
            var organizationList = list[i]['organizations'].length;
            for ( var z = 0; z < organizationList; z++){

                if (  list[i]['organizations'][z] != null ){
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
                    var text = await uerGetOrganization(list[i]['organizations'][z]);
                    var t = document.createTextNode(text);
                    
                    newlink.appendChild(t);
                    document.getElementById("organization" + username).appendChild(newlink);
                   
                }
            }
        

        }; 

    
   
    });

};

async function uerGetOrganization(id){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/organization/" + id,
        "method": "GET",
        "headers": {}
    }

    const ajaxGetUsers = () => {
        return $.ajax(settings).done(function (response) {     
            return response.response;
        });
    }
    var abc = await ajaxGetUsers()
    return abc.response['name'];
}
 
async function uerGetGroups(id){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/group/" + id,
        "method": "GET",
        "headers": {}
    }

    const ajaxGetUsers = () => {
        return $.ajax(settings).done(function (response) {     
            return response.response;
        });
    }
    var abc = await ajaxGetUsers()
    return abc.response['name'];
}
