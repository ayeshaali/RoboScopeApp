(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{33:function(e,t,n){e.exports=n(77)},35:function(e,t,n){var o=n(1),r=(n(6),n(38));n(7);e.exports=function(e){var t=e.data.split(")(").map((function(e){var t=e.split(",");return o.createElement(r,{properties:t})}));return o.createElement("div",{className:"grid-container"},t)}},38:function(e,t,n){var o=n(1);n(6),n(7);e.exports=function(e){return o.createElement("div",{className:"grid-item "+(1==parseInt(e.properties[1])?"active":"inactive")},o.createElement("form",{action:"/activetoggle?id="+e.properties[0],method:"post"},o.createElement("button",{type:"submit",name:"submitButton"},e.properties[0])))}},69:function(e,t){},7:function(e,t,n){},76:function(e,t,n){},77:function(e,t,n){"use strict";n.r(t);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var o=n(32),r=n(1),a=n(35),c=r.useEffect,i=r.useState,s=(n(7),n(39)("http://127.0.0.1:5000")),l=function(e){var t=i(window.token),n=Object(o.a)(t,2),l=n[0],u=n[1];return s.on("connect",(function(){console.log("Websocket connected!")})),c((function(){s.on("message",(function(e){console.log("arduino"),u(e.data)}))}),[l]),r.createElement("div",{className:"App"},r.createElement("header",{className:"App-header"},r.createElement("p",null,"Welcome")),r.createElement(a,{data:l}))},u=n(1),m=n(72);n(6),n(76);m.render(u.createElement(l,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[33,1,2]]]);
//# sourceMappingURL=main.e803beeb.chunk.js.map