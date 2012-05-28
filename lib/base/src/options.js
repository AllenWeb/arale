define(function(require, exports) {

    // Options
    // -----------------
    // Thanks to:
    //  - http://mootools.net/docs/core/Class/Class.Extras


    var Util = require('./util');
    var EVENT_PATTERN = /^on[A-Z]/;


    // 根据 config 中传入的 options 参数，和继承过来的父类的 options，构建 this.options
    // options 是实例化时用户传入的配置选项，只读不写
    exports.initOptions = function(config) {
        // Keep existed options.
        if (!this.hasOwnProperty('options')) {
            this.options = {};
        }
        var options = this.options;

        // Only merge all inherited options once.
        if (!options.__defaults) {
            options.__defaults = Util.getInherited(this, 'options');
            Util.merge(options, options.__defaults);
        }

        Util.merge(options, config, true);

        // Parse `onXxx` option to event handler.
        if (this.on) {
            for (var key in options) {
                var value = options[key];
                if (typeof value === 'function' && EVENT_PATTERN.test(key)) {
                    this.on(getEventName(key), value);
                    delete options[key];
                }
            }
        }
    };


    // Helpers
    // -------

    // Convert `onChangeTitle` to `changeTitle`
    function getEventName(name) {
        return name.charAt(2).toLowerCase() + name.substring(3);
    }

});
