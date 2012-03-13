
var debugInitialValue = seajs.debug;


seajs.config({
  debug: 2
});


define(function(require) {

  var test = require('../../test');

  var a = require('./a');
  var b = require('./b');
  var c = require('./c');
  var d = require('./d');

  var timestamp = (new Date().getTime() + '').substring(0, 8);

  test.assert(debugInitialValue === undefined, 'initial debug value is undefined');
  test.assert(seajs.debug === 1, 'seajs.debug should be 1');
  test.assert(a.id.indexOf(timestamp) === -1, a.id);
  test.assert(b.id.indexOf(timestamp) === -1, b.id);
  test.assert(c.id.indexOf(timestamp) === -1, c.id);
  test.assert(d.id.indexOf(timestamp) === -1, d.id);


  var scripts = document.getElementsByTagName('script');
  for (var i = 0; i < scripts.length; i++) {
    var src = scripts[i].src;
    if (src && /\/debug\/\w\.js/.test(src)) {
      test.assert(src.indexOf(timestamp) > 0, src);
    }
  }

  test.done();
});
