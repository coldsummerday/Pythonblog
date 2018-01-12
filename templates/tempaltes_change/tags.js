



function fssilde() {
    var mheader = document.getElementById('m-header'),
        menuLeft = document.getElementById('m-nav'),
        mcontainer = document.getElementById('m-container'),
        mfooter = document.getElementById('m-footer'),
        showLeftPush = document.getElementById('showLeftPush');
    showLeftPush.onclick = function () {
        classie.toggle(mheader, 'm-header-open');
        classie.toggle(menuLeft, 'm-nav-open');
        classie.toggle(mcontainer, 'm-container-open');
        classie.toggle(mfooter, 'm-footer-open');
        disableOther('showLeftPush');
    };
}

$(document).ready(function () {
    fssilde();
    TagCanvas.Start('mycanvas', '', {
        textColour: '#000',
        outlineColour: '#16a085',
        outlineThickness: 1,
        maxSpeed: 0.03,
        depth: 0.75,
        wheelZoom: false
    });
});