

// get Groups -----------------------------------------------------
function getGroup(){

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
            console.log(list[i]['name']);
                        
            var groupname = list[i]['name'];
     

            newlink = document.createElement('a');
            newlink.setAttribute('class',"list-group-item list-group-item-info mb-2");
            newlink.setAttribute('href', '#');
            newlink.setAttribute('id', groupname);
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.getElementById("listGroups").appendChild(newlink);

                        
            var groupList = list[i]['menu_id'].length;
            if ( groupList > 1 ){
                console.log(list[i]['menu_id']);

                
                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
                newlink.setAttribute('id', "menu" + groupname);
                var t = document.createTextNode("Menus");
                newlink.appendChild(t);
                document.getElementById(groupname).appendChild(newlink);    
            
                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item list-group-item-action ");                
                var t = document.createTextNode(list[i]['menu_id']);
                newlink.appendChild(t);
                document.getElementById("menu" + groupname ).appendChild(newlink);
            };
            

        };
    });
};



// post group --------------------------------------------------------------
function postGroup(){
    
    var nameGroup = document.querySelector("#postNameGroup").value;
    var descriptionGroup = document.querySelector("#postInputdescriptionGroup").value;
    var idMenu = document.querySelector("#postInputMenuidGroup").value;
    
    $.ajax({
        type: "POST",
        url: "http://10.252.2.2:8001/groups",
        data : {'name':nameGroup, 'description': descriptionGroup, 'menu_id': idMenu },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
    });
}

function postGroupSelectMenus(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/menus",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            document.getElementById("postInputMenuidGroup").appendChild(newlink);
            //document.getElementById("putInputMenuidGroup").appendChild(newlink);
        ;}
    });
}



// delete group ----------------------------------------------------

function deleteGroup(){
    
    var group = document.querySelector("#deleteSelectGroup").value;
        
    $.ajax({
        type: "DELETE",
        url: "http://10.252.2.2:8001/group/" + group,
             
        }).done(function (response) {
            var answer = response.response;
            functionAlert(answer);

         });

};

function deleteGroupSelectGroup(){
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
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            
            document.getElementById("deleteSelectGroup").appendChild(newlink);
            //document.getElementById("putSelectGroup").appendChild(newlink);
            
        ;}
    });
}


// put group --------------------------------------------------------------
function putGroup(){
    
    var idGroup = document.querySelector("#putSelectGroup").value;
    var nameGroup = document.querySelector('[value="'+ idGroup +'"]').textContent;
    var newNameGroup = document.querySelector("#putNameGroup").value;
    var descriptionGroup = document.querySelector("#putInputdescriptionGroup").value;
    var idMenu = document.querySelector("#putInputMenuidGroup").value;
    // if newgroup exist add newgroup at name group.
    if ( newNameGroup.length > 1 ){
        nameGroup = newNameGroup
    }
    
    $.ajax({
        type: "PUT",
        url: "http://10.252.2.2:8001/group/" + idGroup,
        data : {'name':nameGroup, 'description': descriptionGroup, 'menu_id': idMenu },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
    });
}
function putGroupSelectMenus(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://10.252.2.2:8001/menus",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            //document.getElementById("postInputMenuidGroup").appendChild(newlink);
            document.getElementById("putInputMenuidGroup").appendChild(newlink);
        ;}
    });
}
function putGroupSelectGroup(){
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
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            
            //document.getElementById("deleteSelectGroup").appendChild(newlink);
            document.getElementById("putSelectGroup").appendChild(newlink);
            
        ;}
    });
}