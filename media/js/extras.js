/**
* Extra stuff
* 
* @version 1.0
* @author
*/
/* prevent right click's to avoid image downloads */
$(document).ready(function(){
    $(document).bind("contextmenu",function(e){
        return false;
    });
});

/* pevent dragging to avoid image downloads */
document.ondragstart = function () { return false; }; 

