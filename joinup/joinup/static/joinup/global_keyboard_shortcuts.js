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
                focus_search_box();
                ev.preventDefault();
            }
    }
});

function focus_search_box() {
    document.querySelector('#event_search_box').focus();
}

})();