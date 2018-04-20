$(document).ready(function () {
        var small={width: "300px"};
        var large={width: "800px"};
        var count=1; 

        $("#enlargebutton").on('click',function () { 
            $(toggleimage).animate((count==1)?large:small);
            count = 1-count;
        });
    });