// post images --------------------------------------------------------------
async function postImages(){
    
    var titleImage = document.querySelector("#postNameImage").value;
    var typeImage = document.querySelector("#postTypeImage").value;
    var imageSource = document.querySelector("#postImageSource").value;
    var kernelSource = document.querySelector("#postKernelSource").value;

    var argument = document.querySelector("#postArg").value;
    var argValue = document.querySelector("#postValue").value;
    
    $.ajax({
        type: "POST",
        url: config() + "/images",
        data : {'title':titleImage, 
                'type': typeImage, 
                'image_source': imageSource,
                'kernel_source': kernelSource,
                },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });

    if ( ! isBlank(argument)){
        var imageId = await imageGetId(titleImage);
        
        $.ajax({
            type: "POST",
            url: config() + "/image/" + imageId + "/boot-args",
            data : {'arg':argument, 'value': argValue },
            
            
                }).done(function (response) {
                    var answer = response.response;
                    functionAlert(answer);
        }); 
    }
}

async function imageGetId(title){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/images",
        "method": "GET",
        "headers": {}
    }

    const ajaxGetImageId = () => {
        return $.ajax(settings).done(function (response) {     
            return response.response;        
        });
    }
    var abc = await ajaxGetImageId()
    
    for ( var i = 0; abc.response.length; i++ ){
        if ( abc.response[i]['title'] == title ){
            return abc.response[i]['id'];
        }
    }
}


// delete image----------------------------------------------------

function deleteImage(){
    
    var idImage = document.querySelector("#deleteSelectImage").value;
            
    $.ajax({
        type: "DELETE",
        url: config() + "/image/" + idImage,
             
        }).done(function (response) {
            var answer = response.response;
            functionAlert(answer);

         });

};


// Edit images --------------------------------------------------------------
function putImages(){
    
    var idImage = document.querySelector("#putSelectImage").value;
    var titleImage = document.querySelector('[value="' + idImage + '"]').textContent;
    var NewtitleImage = document.querySelector("#putNewNameImage").value;
    var typeImage = document.querySelector("#putTypeImage").value;
    var imageSource = document.querySelector("#putImageSource").value;
    var kernelSource = document.querySelector("#putKernelSource").value;
    
    // if newgroup exist add newgroup at name group.
    if ( NewtitleImage.length > 1 ){
        titleImage = NewtitleImage
    }

    $.ajax({
        type: "PUT",
        url: config() + "/image/" + idImage,
        data : {'title':titleImage, 
                'type': typeImage, 
                'image_source': imageSource,
                'kernel_source': kernelSource,
                },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
}


// get Images -----------------------------------------------------

function isBlank(str) {
    return (!str || /^\s*$/.test(str));
}

function getImages(){
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/images",
        "method": "GET",
        "headers": {}
    }
    
    $.ajax(settings).done(function (response) {
  

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
                        
            var imageTitle = list[i]['title'];

            newlink = document.createElement('a');
            newlink.setAttribute('class',"list-group-item list-group-item-info mb-2");
            //newlink.setAttribute('href', '#');
            newlink.setAttribute('id', imageTitle);
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            document.getElementById("listImages").appendChild(newlink);
                 
                    
            newlink = document.createElement('a');
            newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
            newlink.setAttribute('id', "items" + imageTitle);
            var t = document.createTextNode("Items");
            newlink.appendChild(t);
            document.getElementById(imageTitle).appendChild(newlink);    
            
            // items images
            var itemList = ["type","image_source","kernel_source"];
                        
            for ( var x = 0; x < itemList.length; x++ ){
                var text = list[i][itemList[x]];
                
                if ( ! isBlank(text) ){
        
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-warning ");                
                    newlink.setAttribute('id', "items"+ itemList[x] + imageTitle);
                    var t = document.createTextNode(itemList[x]);
                    newlink.appendChild(t);
                    document.getElementById("items" + imageTitle).appendChild(newlink); 
                    
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-action ");                                        
                    var t = document.createTextNode(text);
                    newlink.appendChild(t);
                    document.getElementById("items" + itemList[x] + imageTitle).appendChild(newlink);

                }

            };

            // items boot args
            var keyBootArgs = Object.keys(list[i]["boot_args"]);
            if ( ! keyBootArgs.length == 0 ){
                for ( z in keyBootArgs){

                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-warning ");                
                    newlink.setAttribute('id', "itemsBootArgs" + imageTitle);
                    var t = document.createTextNode("Boot_args");
                    newlink.appendChild(t);
                    document.getElementById("items" + imageTitle).appendChild(newlink); 
                    
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-action "); 
                    //newlink.setAttribute('id', "itemsBootArgs" + keyBootArgs[z] + imageTitle);                                       
                    var t = document.createTextNode(keyBootArgs[z]);
                    newlink.appendChild(t);
                    document.getElementById("itemsBootArgs" + imageTitle).appendChild(newlink);

                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-action "); 
                    //newlink.setAttribute('id', "itemsBootArgs" + keyBootArgs[z] + imageTitle);                                       
                    var t = document.createTextNode(list[i]["boot_args"][keyBootArgs[z]]);
                    newlink.appendChild(t);
                    document.getElementById("itemsBootArgs" + imageTitle).appendChild(newlink);
                }
            }

        };        
    });
};

// select post options 

var options = ["#divImageSource","#divKernelSource","#divArg","#divValue",
            "#divPutImageSource","#divPutKernelSource"];

function isoOptions(divvisible){
    for ( var i = 0; i < options.length; i++ ){
        var element = document.querySelector(options[i]);
        element.classList.add("d-none");
    }
    var element = document.querySelector(divvisible);
    element.classList.remove("d-none");
}

function imgOptions(){
    for ( var i = 0; i < options.length; i++ ){
        var element = document.querySelector(options[i]);
        element.classList.remove("d-none");
    }
}

function hideOptions(){
    for ( var i = 0; i < options.length; i++ ){
        var element = document.querySelector(options[i]);
        element.classList.add("d-none");
    }
}

// otions images -------------------------
function GetImages(id){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": config() + "/images",
        "method": "GET",
        "headers": {}
    }

    $.ajax(settings).done(function (response) {

        var list = response.response;
        var len = response.response.length;
        
        for (var i = 0; i < len; i++ ) {
            var type = list[i]['type'];  
            var kernel_source = list[i]['kernel_source'];  
            var image_source = list[i]['image_source']; 
            
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);          
            newlink.setAttribute('onclick','valuesImages("'+ type + '","'+ kernel_source +'","'+ image_source +'")');         
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            
            document.getElementById(id).appendChild(newlink);
            
            
        ;}
    });
}

function valuesImages(type, kernel_source, image_source){
    
    
    if ( type == "iso" ){
        isoOptions('#divPutImageSource');
    } else if ( type == "kernel_initrd" ){
        imgOptions('#divPutImageSource');
    }

    document.querySelector("#putTypeImage").value = type ;
    document.querySelector("#putImageSource").value = image_source ;
    document.querySelector("#putKernelSource").value = kernel_source ;
    
}



