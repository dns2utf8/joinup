(function() {
'use strict';

var input = document.querySelector('#event_search_box');
var button = document.querySelector('.event_search_box > button[type=submit]');

input.onkeyup = function(ev) {
    if (ev.keyCode === 13) {
        run_search();
    }
};

button.onclick = function(ev) {
    run_search();
    ev.preventDefault();
};

function run_search() {
    var query = input.value;
    query = query.trim()
                .split('/')[0]; // TODO correctly encode the query
    location.pathname = '/search/'+input.value;
}

})();