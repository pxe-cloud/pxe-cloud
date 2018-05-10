

// get menus -----------------------------------------------------
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

            var groupList = list[i]['menu'].length;
            for ( var x = 0; x < groupList; x++){
                console.log(list[i]['menu'][x]);

                if ( x == 0 ){
                    newlink = document.createElement('a');
                    newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
                    newlink.setAttribute('id', "menu" + groupname);
                    var t = document.createTextNode("Menus");
                    newlink.appendChild(t);
                    document.getElementById(groupname).appendChild(newlink);    
                };
                newlink = document.createElement('a');
                newlink.setAttribute('class',"list-group-item list-group-item-action ");                
                var t = document.createTextNode(list[i]['menu'][x]);
                newlink.appendChild(t);
                document.getElementById("menu" + groupname ).appendChild(newlink);
            };
            
            
            // var organizationList = list[i]['organizations'].length;
            // for ( var z = 0; z < organizationList; z++){
            //     console.log(list[i]['organizations'][z]);

            //     if ( z == 0 ){
            //         newlink = document.createElement('a');
            //         newlink.setAttribute('class',"list-group-item  list-group-item-success ");                
            //         newlink.setAttribute('id', "organization" + username);
            //         var t = document.createTextNode("Organizations");
            //         newlink.appendChild(t);
            //         document.getElementById(username).appendChild(newlink);    
            //     };

            //     newlink = document.createElement('a');
            //     newlink.setAttribute('class',"list-group-item list-group-item-action ");                
            //     var t = document.createTextNode(list[i]['organizations'][z]);
            //     newlink.appendChild(t);
            //     document.getElementById("organization" + username).appendChild(newlink);
            // }
        };
    });
};
