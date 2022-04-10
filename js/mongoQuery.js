msg.collection = msg.payload;
var aux = new Date();
var hj = aux.getTime() - (aux.getTimezoneOffset() * 60000)

var dataHj = new Date(hj - (3600000*3));

var aux2 = aux.setDate(aux.getDate()-1);
aux2 = aux.getTime() - (aux.getTimezoneOffset() * 60000)
var dataOntem = new Date(aux2 - (3600000*3));

msg.data = [dataOntem, dataHj];
msg.payload = {"recvTime": {"$gte": new Date(dataOntem),"$lte": new Date(dataHj)}, "attrName": "v_l1n"};
msg.limit = 150000;
return msg;
