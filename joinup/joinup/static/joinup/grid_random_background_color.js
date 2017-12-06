(function() {
'use strict'

var tags = document.querySelectorAll('.grid > *');
for (var i = 0; i < tags.length; ++i) {
    var tag = tags[i];
    tag.style.background = '#'+random_color_part(0xa0, 0xf0)
                                +random_color_part(0xa0, 0xf0)
                                +random_color_part(0xa0, 0xf0);
}

/// Output two signs as a Hex String
function random_color_part(min, max) {
    var r = Math.random() * (max - min) + min;
    r = (r |0).toString(16);
    if (r.length === 1) {
        r = '0'+r;
    }
    return r;
}
})();