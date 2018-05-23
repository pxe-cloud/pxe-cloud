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
}



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
    postItem()
    reloadEntries()
    // var element = document.querySelector("#divFinalMenu");
    // element.classList.remove("d-none");

    // var type = document.querySelector("#selectTypeItemMenu").value;
    // var imageId = document.querySelector("#selectIdImage").value;
    // var content = document.querySelector("#divItemsIdContent").value;

    // if ( type == "image"){
    //     myfunction(type,imageId);
    // } else if ( type == "separator" ){
    //     myfunction(type,content);
    // }
}








// function myfunction(type,data){

//     newlink = document.createElement('li');
//     newlink.setAttribute('class',"list-group-item");                
//     newlink.setAttribute('id',data);
//     //newlink.setAttribute('onclick','valuesMenus("'+ background + '")');     
//     var t = document.createTextNode(type);
//     newlink.appendChild(t);
//     document.getElementById("sortable").appendChild(newlink);

//     newlink = document.createElement('span');
//     //newlink.setAttribute('class',"list-group-item");                
//     //newlink.setAttribute('onclick','valuesMenus("'+ background + '")');     
//     var t = document.createTextNode(data);
//     newlink.appendChild(t);
//     document.getElementById(data).appendChild(newlink);

// }






function postItem(){
    var type = document.querySelector("#selectTypeItemMenu").value;
    var imageId = document.querySelector("#selectIdImage").value;
    var content = document.querySelector("#divItemsIdContent").value;

    if ( type == "image"){
        var data = {'type': type, 'image_id': imageId}
    } else if ( type == "separator" ){
        var data = {'type': type, 'content': content}
    }
    
    $.ajax({
        type: "POST",
        // TODO: Change the post position to the last one
        url: config() + "/menu/8620f308-f431-4568-9196-6f61c687067e/entry/0",
        data : data}

            ).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
};

function reloadEntries() {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/menu/8620f308-f431-4568-9196-6f61c687067e",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response.entries;
        var len = response.response.entries.length;

        $('#sortable').empty()
        for (var i = 0; i < len; i++ ) {
            newlink = document.createElement('li');
            newlink.setAttribute('class',"list-group-item");                
            newlink.setAttribute('id', i);
            newlink.setAttribute('data-initial-position', i) 
            document.getElementById("sortable").appendChild(newlink);

            newlink = document.createElement('p');
            if (list[i]['type'] == "image") {
                var t = document.createTextNode(list[i]['image_id']);
            } else if (list[i]['type'] == "separator") {
                var t = document.createTextNode(list[i]['content']);
            }
            newlink.appendChild(t);
            document.getElementById(i).appendChild(newlink);          

            newlink = document.createElement('small')
            var t = document.createTextNode(list[i]['type']);
            newlink.appendChild(t);
            document.getElementById(i).appendChild(newlink)
        }

        // Sort the li items using their DB position
        // https://stackoverflow.com/questions/21600802/jquery-sort-list-based-on-data-attribute-value/21600865
        // $("#sortable li").sort(sort_li).appendTo('#sortable');
        // function sort_li(a, b){
        //     return ($(b).data('database-position')) < ($(a).data('database-position')) ? 1 : -1;    
        // }


    });
}