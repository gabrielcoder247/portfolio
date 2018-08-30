$(document).ready(function(){
    $('.close-nav').click(function(){
        document.getElementById("sideNav").style.width = "0";
    })

    $('.open-nav').click(function(){
        document.getElementById('sideNav').style.width = "290px";
    })

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 54
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 50) {
            // $("#mainNav").removeClass("no-display");
            $("#mainNav").addClass("navbar-shrink");
        } else {
            // $("#mainNav").addClass("no-display");
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})

$(document).ready(function() {
$(".down").click(function() {
     $('html, body').animate({
         scrollTop: $(".up").offset().top
     }, 1500);
 });
});

