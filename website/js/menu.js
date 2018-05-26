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
    var nameMenu = document.querySelector('[value="'+ idMenu +'"]').textContent;
    var newNameMenu = document.querySelector("#editNameMenu").value;
    var backgroundMenu = document.querySelector("#editBackgroudMenu").value;
    
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

function GetMenus(id){
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
            var background = list[i]['background'];  

            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);                
            newlink.setAttribute('onclick','valuesMenus("'+ background + '")');     
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            document.getElementById(id).appendChild(newlink);
          
        ;}
    });
}

function valuesMenus(bac){
    
    if ( bac == "null" ){
        bac = "";
    }
    document.querySelector("#editBackgroudMenu").value = bac ;
    var idMenu = document.querySelector("#editSelectMenu").value;
    reloadEntries(idMenu);
    var element = document.querySelector("#divFinalMenu");
    element.classList.remove("d-none");
    //divFinalMenu
}

$( function() {
    var entryInitialPos = null;
    var entryNewPos = null;

    $( "#sortable" ).sortable({
        
        stop: function( event, ui ) {
            entryInitialPos = ui.item.data('initial-position');
            entryNewPos = ui.item.index()
            var idMenu = document.querySelector("#editSelectMenu").value;
            
            $.ajax({
                type: "PUT",
                url: config() + "/menu/" + idMenu + "/entry/" + entryInitialPos,
                data : {'new_position': entryNewPos},
                
                
                }).done(function (response) {
                    var answer = response.response;
                    functionAlert(answer);
                    reloadEntries()
            });
            
        }
    })
    $( "#sortable" ).disableSelection();
   } );

function typeMenu(divvisible){
    var options = ["#divItemsIdImages","#divItemsContent"];    
    for ( var i = 0; i < options.length; i++ ){
        var element = document.querySelector(options[i]);
        element.classList.add("d-none");
    }
    var element = document.querySelector(divvisible);
    element.classList.remove("d-none");
}

function hiddeMenuTypes(){
    var options = ["#divItemsIdImages","#divItemsContent"];
    for ( var i = 0; i < options.length; i++ ){
        var element = document.querySelector(options[i]);
        element.classList.add("d-none");
    }
}



function addItem(){
    postItem();
    var idMenu = document.querySelector("#editSelectMenu").value;
    reloadEntries(idMenu);       
}


function postItem(){
    var type = document.querySelector("#selectTypeItemMenu").value;
    var imageId = document.querySelector("#selectIdImage").value;
    var content = document.querySelector("#divItemsIdContent").value;
    var idMenu = document.querySelector("#editSelectMenu").value;

    if ( type == "image"){
        var data = {'type': type, 'image_id': imageId}
    } else if ( type == "separator" ){
        var data = {'type': type, 'content': content}
    }
    
    $.ajax({
        type: "POST",
        // TODO: Change the post position to the last one
        url: config() + "/menu/" + idMenu + "/entry/0",
        data : data}

            ).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
};

function reloadEntries(menuId) {
    if (menuId !== undefined) {
        
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": config() + "/menu/" + menuId,   
            "method": "GET",
            "headers": {}
        }
    
        $.ajax(settings).done(async function (response) {
    
            var list = response.response.entries;
            var len = response.response.entries.length;
    
            $('#sortable').empty()
            for (var i = 0; i < len; i++ ) {
                newlink = document.createElement('a');
                if (list[i]['type'] == "image") {
                    newlink.setAttribute('class',"list-group-item list-group-item-action list-group-item-warning");     
                    var t = document.createTextNode(image);
                } else if (list[i]['type'] == "separator") {
                    newlink.setAttribute('class',"list-group-item list-group-item-action list-group-item-info");     
                }
                newlink.setAttribute('href',"#");                
                newlink.setAttribute('id', 'sortable-entry-' + i);
                newlink.setAttribute('data-initial-position', i) 
                document.getElementById("sortable").appendChild(newlink);
    
                newlink = document.createElement('p');
                if (list[i]['type'] == "image") {
                    var image = await imageGetTitle(list[i]['image_id']);
                    var t = document.createTextNode(image);
                } else if (list[i]['type'] == "separator") {
                    var t = document.createTextNode(list[i]['content']);
                }
                newlink.appendChild(t);
                document.getElementById('sortable-entry-' + i).appendChild(newlink);
    
                newlink = document.createElement('small')
                var t = document.createTextNode(list[i]['type']);
                newlink.appendChild(t);
                document.getElementById('sortable-entry-' + i).appendChild(newlink)
            }
    
        
        });
    }
}

async function imageGetTitle(id){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/image/" + id,
        "method": "GET",
        "headers": {}
    }

    const ajaxGetImage = () => {
        return $.ajax(settings).done(function (response) {     
            return response.response;
        });
    }
    var abc = await ajaxGetImage()
    return abc.response['title'];
}
