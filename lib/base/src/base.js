define(function(require) {

    var Class = require('class');
    var Events = require('events');
    var Attrs = require('./attrs');
    var Options = require('./options');


    return Class.create({
        Implements: [Events, Attrs, Options],

        initialize: function(config) {
            this.initAttrs(config);
            this.initOptions(config);
        },

        destroy: function() {
            for (var p in this) {
                if (this.hasOwnProperty(p)) {
                    delete this[p];
                }
            }
        }
    });

});
