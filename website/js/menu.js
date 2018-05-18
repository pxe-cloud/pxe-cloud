// ---- add menu ----

function postMenu(){
    var nameMenu = document.querySelector("#postNameMenu").value;
    var backgroungMenu = document.querySelector("#postInputbackgroundMenu").value;
    
    
    $.ajax({
        type: "POST",
        url: config() + "/menus",
        data : {'title':nameMenu, 'background': backgroungMenu },

            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
};

// put menu --------------------------------------------------------------
function putMenu(){
    
    var idMenu = document.querySelector("#editSelectMenu").value;
    // falla value= por inexplicable causa
    var nameMenu = document.querySelector('[value="'+ idMenu +'"]').textContent;
    var newNameMenu = document.querySelector("#editNameMenu").value;
    var backgroundMenu = document.querySelector("#editBackgroudMenu").value;
    
    // if newgroup exist add newgroup at name group.
    if ( newNameMenu.length > 1 ){
        nameMenu = newNameMenu ;
    }
    
    $.ajax({
        type: "PUT",
        url: config() + "/menu/" + idMenu,
        data : {'title':nameMenu, 'background': backgroundMenu },
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
}


function putSelectMenus(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/menus",
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
            
            document.getElementById("editSelectMenu").appendChild(newlink);
        ;}
    });
}

// delete menu ----------------------------------------------------

function deleteMenu(){
    
    var menu = document.querySelector("#deleteSelectMenu").value;
        
    $.ajax({
        type: "DELETE",
        url: config() + "/menu/" + menu,
             
        }).done(function (response) {
            var answer = response.response;
            functionAlert(answer);

         });

};

function deleteSelectMenus(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/menus",
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
            
            document.getElementById("deleteSelectMenu").appendChild(newlink);
        ;}
    });
}


// get menus-----------------------------------------------------
function getMenus(){

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/menus",
        "method": "GET",
        "headers": {}
    }
    
    $.ajax(settings).done(function (response) {
  

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
                        
            var menuName = list[i]['title'];

            newlink = document.createElement('a');
            newlink.setAttribute('class',"list-group-item list-group-item-info mb-2");
            newlink.setAttribute('href', '#');
            newlink.setAttribute('id', menuName);
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            document.getElementById("listmenus").appendChild(newlink);

                        
            var backgroundList = list[i]['background'];
        
            if ( backgroundList  != null ){
                
                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
                newlink.setAttribute('id', "background" + menuName);
                var t = document.createTextNode("Background");
                newlink.appendChild(t);
                document.getElementById(menuName).appendChild(newlink);    



                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item list-group-item-action ");                
                var t = document.createTextNode(backgroundList);
                newlink.appendChild(t);
                document.getElementById("background" + menuName ).appendChild(newlink);

            };
            

        };
    });
};
