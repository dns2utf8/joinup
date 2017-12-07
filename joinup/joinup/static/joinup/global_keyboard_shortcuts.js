(function() {
'use strict'

window.addEventListener('keyup', function(ev) {
    if (ev.defaultPrevented) {
        return; // Should do nothing if the default action has been cancelled
    }

    switch (ev.key || ev.keyCode) {
        case 's':
        case 83:
            if (ev.isComposing === false) {
                focus_search_box(ev);
            }
    }
});

function focus_search_box(ev) {
    var current = document.activeElement;

    switch (current.type) {
        case 'text':
        case 'textarea':
        case 'select-one':
        case 'select-multiple':
        case 'password':
        case 'email':
            break;

        default:
            document.querySelector('#event_search_box').focus();
            ev.preventDefault();
    }
}

})();