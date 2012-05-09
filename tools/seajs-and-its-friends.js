
// load sea.js
(function(m, o, d, u, l, a, r) {
    if(m[d]) return;
    function f(n, t) { return function() { r.push(n, arguments); return t; } }
    m[d] = a = { args: (r = []), config: f(0, a), use: f(1, a) };
    m.define = f(2);
    u = o.createElement('script');
    u.id = d + 'node';
    u.src = '../../../dist/seajs/1.1.0/sea.js';
    l = o.getElementsByTagName('head')[0];
    l.insertBefore(u, l.firstChild);
})(window, document, 'seajs');


// and its friends
seajs.config({
    alias: {
        'events': 'events/0.9.1/events',
        'class': 'class/0.9.0/class',
        //'base': 'base/0.9.0/base',
        'base': '../../../lib/base/src/base',

        '$': 'jquery/1.7.2/jquery',
        'jquery': 'jquery/1.7.2/jquery',
        'zepto': 'zepto/0.8.0/zepto',

        'json': 'json/1.0.2/json',
        'underscore': 'underscore/1.3.3/underscore',
        'cookie': 'cookie/1.0.2/cookie',
        'moment': 'moment/1.6.2/moment',

        'iframe-shim': 'iframe-shim/0.9.0/iframe-shim',
        'position': 'position/0.9.0/position'
    },
    preload: [this.JSON ? '' : 'json', 'plugin-text']
});
