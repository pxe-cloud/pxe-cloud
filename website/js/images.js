// post images --------------------------------------------------------------
function postImages(){
    
    var titleImage = document.querySelector("#postNameImage").value;
    var typeImage = document.querySelector("#postTypeImage").value;
    var imageSource = document.querySelector("#postImageSource").value;
    var kernelSource = document.querySelector("#postKernelSource").value;
    var repositoryUrl = document.querySelector("#postRepositoryUrl").value;
    var bootArgs = document.querySelector("#postBootArgs").value;
    
    $.ajax({
        type: "POST",
        url: config() + "/images",
        data : {'title':titleImage, 
                'type': typeImage, 
                'image_source': imageSource,
                'kernel_source': kernelSource,
                'repository_url': repositoryUrl,
                'boot_args': bootArgs },
        
        
            }).done(function (response) {
                var answer = response.response;
                functionAlert(answer);
                    
    });
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
    var repositoryUrl = document.querySelector("#putRepositoryUrl").value;
    var bootArgs = document.querySelector("#putBootArgs").value;
    
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
                'repository_url': repositoryUrl,
                'boot_args': bootArgs },
        
        
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
            newlink.setAttribute('href', '#');
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

            var itemList = ["type","image_source","kernel_source","repository_url","boot_args"];
                        
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
        };        
    });
};

// select post options 

var options = ["#divImageSource","#divKernelSource","#divRepositoryUrl","#divBootArgs",
            "#divPutImageSource","#divPutKernelSource","#divPutRepositoryUrl","#divPutBootArgs"];

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
            var repository_url = list[i]['repository_url'];  
            var kernel_source = list[i]['kernel_source'];  
            var image_source = list[i]['image_source']; 
            var boot_args = list[i]['boot_args'];  
            
            newlink = document.createElement('option');
            newlink.setAttribute('value',list[i]['id']);          
            newlink.setAttribute('onclick','valuesImages("'+ type + '","'+repository_url+'","'+ kernel_source +'","'+ image_source +'","'+ boot_args +'")');         
            var t = document.createTextNode(list[i]['title']);
            newlink.appendChild(t);
            
            document.getElementById(id).appendChild(newlink);
            
            
        ;}
    });
}

function valuesImages(type, repository_url, kernel_source, image_source, boot_args){
    
    
    if ( type == "iso" ){
        isoOptions('#divPutImageSource');
    } else if ( type == "kernel_initrd" ){
        imgOptions('#divPutImageSource');
    }

    document.querySelector("#putTypeImage").value = type ;
    document.querySelector("#putImageSource").value = image_source ;
    document.querySelector("#putKernelSource").value = kernel_source ;
    document.querySelector("#putRepositoryUrl").value = repository_url ;
    document.querySelector("#putBootArgs").value = boot_args ;

    
}



