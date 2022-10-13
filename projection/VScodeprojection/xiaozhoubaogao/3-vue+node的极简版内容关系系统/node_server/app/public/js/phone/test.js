
<script src="../public/js/jquery.js"></script>
$(function () {
    $("a .word").css("color", "rgb(255, 255, 255)");
    $("a").on("click", ".word", function () {

        //$("#selOld dd").on(click,function(){
        if ($(this).css("background-color") == "rgb(255, 255, 255)") {
            $(this).css("background-color", "#87CEFA")
        } else if ($(this).css("background-color") == "rgb(135, 206, 250)") {
            $(this).css("background-color", "#FFFFFF");
        }
        //})
    })
}); 
