// Simple navigation toggler
var togMenu = false;
function show() {
    togMenu = !togMenu;
    var menu =  document.getElementById("menu");
    if (togMenu == true) {
        menu.style.height = "100%";
    }
    else {
        menu.style.height = "0";
    }
} 