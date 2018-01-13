



function fssilde() {
    var mheader = document.getElementById('m-header'),
        mcontainer = document.getElementById('m-container'),
        showLeftPush = document.getElementById('showLeftPush');
    showLeftPush.onclick = function () {
        classie.toggle(mheader, 'm-header-open');
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