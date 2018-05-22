

// get Groups -----------------------------------------------------
function getGroup(){

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/groups",
        "method": "GET",
        "headers": {}
    }
    
    $.ajax(settings).done(async function (response) {
  

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
                //
                console.log(list[i]['menu_id']);
                var text = await groupGetMenus(list[i]['menu_id']);
                var t = document.createTextNode(text);
                //var t = document.createTextNode(list[i]['menu_id']);
                newlink.appendChild(t);
                document.getElementById("menu" + groupname ).appendChild(newlink);
            };
            

        };
    });
};

async function groupGetMenus(id){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/menu/" + id,
        "method": "GET",
        "headers": {}
    }

    const ajaxGetMenus = () => {
        return $.ajax(settings).done(function (response) {     
            return response.response;
        });
    }
    var abc = await ajaxGetMenus()
    return abc.response['title'];
}




// post group --------------------------------------------------------------
function postGroup(){
    
    var nameGroup = document.querySelector("#postNameGroup").value;
    var descriptionGroup = document.querySelector("#postInputdescriptionGroup").value;
    var idMenu = document.querySelector("#postInputMenuidGroup").value;
    
    $.ajax({
        type: "POST",
        url: config() + "/groups",
        data : {'name':nameGroup, 'description': descriptionGroup, 'menu_id': idMenu },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
    });
}




// delete group ----------------------------------------------------

function deleteGroup(){
    
    var group = document.querySelector("#deleteSelectGroup").value;
        
    $.ajax({
        type: "DELETE",
        url: config() + "/group/" + group,
             
        }).done(function (response) {
            var answer = response.response;
            functionAlert(answer);

         });

};



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
        url: config() + "/group/" + idGroup,
        data : {'name':nameGroup, 'description': descriptionGroup, 'menu_id': idMenu },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
    });
}

function GetGroups(id){
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
            var description = list[i]['description'];
            var menu_id = list[i]['menu_id'];

            var groupList = list[i]['name'].length;  
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);      
            newlink.setAttribute('onclick','valuesGroup("'+ description + '","'+ menu_id +'")');              
            var t = document.createTextNode(list[i]['name']);
            newlink.appendChild(t);
            document.getElementById(id).appendChild(newlink);
        ;}
    });
}


async function valuesGroup(descript,menu_id){
    
    if ( descript == "null" ){
        descript = "";
    }
    document.querySelector("#putInputdescriptionGroup").value = descript ;

    if ( menu_id != "null" ){
        document.querySelector("#currentGroup").value = await groupGetMenus(menu_id);
        
    }
}


