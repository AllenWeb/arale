define("#widget/0.9.10/widget",["base","$","./daparser"],function(a,b,c){function l(){return"widget-"+k++}function m(a){return j.call(a)==="[object String]"}function n(a){return j.call(a)==="[object Function]"}function o(a){for(var b in a)if(a.hasOwnProperty(b))return!1;return!0}function p(a){return a.replace(/^\s*/,"").replace(/\s*$/,"")}function q(a){return e.contains(document.documentElement,a)}function r(a){return a.charAt(0).toUpperCase()+a.substring(1)}function s(a){return a==null||(m(a)||e.isArray(a))&&a.length===0||e.isPlainObject(a)&&o(a)}function t(a,b){for(var c in a){if(!a.hasOwnProperty(c))continue;var d=p(c).split(/\s*,\s*/),e=a[c];while(c=d.shift()){var f=c.split(/\s+/),g=f[0],h=f[1];h||(h=g,g="click"),b[g+" "+e]=h}}}function x(a){return n(a.events)&&(a.events=a.events()),a.events}function y(a,b){var c=a.match(u),d=c[1]+g+b.cid,e=c[2]||"";return e.indexOf("{{")>-1&&(e=z(e,b)),{type:d,selector:e}}function z(a,b){return a.replace(v,function(a,c){var d=c.split("."),g=b,h;while(h=d.shift())g===b.attrs?g=b.get(h):g=g[h];if(m(g))return g;var i=e(g)[0];return i&&i.nodeType===1?"."+f.stamp(i):w})}var d=a("base"),e=a("$"),f=a("./daparser"),g=".delegate-events-",h="_onRender",i=d.extend({propsInAttrs:["element","template","model","events"],element:null,template:"<div></div>",model:null,events:null,attrs:{parentNode:document.body,"data-api":!0},initialize:function(a){this.cid=l(),this.initAttrs(a),this._bindOnRender2OnChange(),this.parseElement(),this._parseDataAttrs(),this.initProps(),this.delegateEvents(),this.setup()},_bindOnRender2OnChange:function(){var a=this,b=a.attrs;for(var c in b){if(!b.hasOwnProperty(c))continue;var d=h+r(c);a[d]&&function(b){a.on("change:"+c,function(c,d,e){a[b](c,d,e)})}(d)}},parseElement:function(){var a=this.element;a?this.element=e(a):this.get("template")&&this.parseElementFromTemplate();if(!this.element||!this.element[0])throw"element is invalid"},parseElementFromTemplate:function(){this.element=e(this.get("template"))},_parseDataAttrs:function(){if(!this.get("data-api"))return;this.dataset||(this.dataset=f.parse(this.element[0]));var a=this.dataset.action;if(a){var b=x(this)||(this.events={});t(a,b)}},initProps:function(){},delegateEvents:function(a,b){a||(a=x(this));if(!a)return;if(m(a)&&n(b)){var c={};c[a]=b,a=c}for(var d in a){if(!a.hasOwnProperty(d))continue;var e=y(d,this);(function(a,b){b.element.on(e.type,e.selector,function(c){n(a)?a.call(b,c):b[a](c)})})(a[d],this)}return this},undelegateEvents:function(a){var b={};return arguments.length===0?b.type=g+this.cid:b=y(a,this),this.element.off(b.type,b.selector),this},setup:function(){},render:function(){this._renderInitialAttrs();var a=this.get("parentNode");return a&&!q(this.element[0])&&this.element.appendTo(a),this},_renderInitialAttrs:function(){var a=this.attrs;for(var b in a)if(a.hasOwnProperty(b)){var c=h+r(b);if(this[c]){var d=this.get(b);s(d)||this[c](this.get(b),undefined,b)}}},$:function(a){return this.element.find(a)},destroy:function(){this.undelegateEvents(),i.superclass.destroy.call(this)}});c.exports=i;var j=Object.prototype.toString,k=0,u=/^(\S+)\s*(.*)$/,v=/{{([^}]+)}}/g,w="INVALID_SELECTOR"});