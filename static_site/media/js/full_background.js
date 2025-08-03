/**
* Full Size Backgrounded
* 
* @version 1.0
* @author Vaska 
*/
function bg_img_resize() 
{
    var w = $(window).width();
    var h = $(window).height() - 42; 
    var iw = $('#the-background img').attr('width');
    var ih = $('#the-background img').attr('height');
    var rw = iw / ih;
    var rh = ih / iw;
    var sc = h * rw;
    if (sc >= w) {
        nh = h;
        nw = sc;
    } else {
        sc = w * rh;
        nh = sc;
        nw = w;
    }

    $('#the-background img').css({height: nh, width: nw});
}

$(document).ready(function(){ bg_img_resize(); });
$(window).resize(function(){ bg_img_resize(); });

$(window).resize(function(){ 
    bg_img_resize(); 
    $('#the-background').css({ 'top' : 43, 'left' : 0 }); 
});
$(window).scroll(function(){ 
    bg_img_resize(); 
    $('#the-background').css({ 'top' : 43, 'left' : 0 }); 
});

/* http://jonraasch.com/blog/a-simple-jquery-slideshow */
function slideSwitch() {
    var $active = $('#the-background IMG.active');

    if ( $active.length == 0 ) $active = $('#the-background IMG:last');

    var $next =  $active.next().length ? $active.next()
        : $('#the-background IMG:first');

    $active.addClass('last-active');

    $next.css({opacity: 0.0})
        .addClass('active')
        .animate({opacity: 1.0}, 2000, function() {
            $active.removeClass('active last-active');
        });
}

$(function() {
    setInterval( "slideSwitch()", 5000 );
});