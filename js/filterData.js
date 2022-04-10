var m = {};
m.labels = [];
m.labelsCount = [];
m.labelsSum = [];
for(var i=0; i < 24; ++i) {
    m.labels.push(i.toString());
    m.labelsCount.push(0);
    m.labelsSum.push(0);
}

m.data = [[]];
m.series = [];

var ontem = new Date("2020-12-16T03:00:00.000Z");
//m.series.push(hj.toString());
var ano = ontem.getFullYear(), mes = ontem.getMonth()+1, dia = ontem.getDate()+1;
var hour = '';

var msg = {};
let data;

msg.payload.forEach((elem, idx) => {
    //m.series.push(elem.recvTime.toString());
    data = new Date(elem.recvTime);
    
    if(ano == data.getFullYear() && mes == data.getMonth()+1 && dia == data.getDate()) {
        
        var hour = data.getHours();
        //m.series.push(hour);
        if(hour === 0) {
            m.labelsCount[0] += 1;
            m.labelsSum[0] += parseFloat(elem.attrValue);
        }else if(hour === 1) {
            m.labelsCount[1] += 1;
            m.labelsSum[1] += parseFloat(elem.attrValue);
        }else if(hour === 2) {
            m.labelsCount[2] += 1;
            m.labelsSum[2] += parseFloat(elem.attrValue);
        }else if(hour === 3) {
            m.labelsCount[3] += 1;
            m.labelsSum[3] += parseFloat(elem.attrValue);
        }else if(hour === 4) {
            m.labelsCount[4] += 1;
            m.labelsSum[4] += parseFloat(elem.attrValue);
        }else if(hour === 5) {
            m.labelsCount[5] += 1;
            m.labelsSum[5] += parseFloat(elem.attrValue);
        }else if(hour === 6) {
            m.labelsCount[6] += 1;
            m.labelsSum[6] += parseFloat(elem.attrValue);
        }else if(hour === 7) {
            m.labelsCount[7] += 1;
            m.labelsSum[7] += parseFloat(elem.attrValue);
        }else if(hour === 8) {
            m.labelsCount[8] += 1;
            m.labelsSum[8] += parseFloat(elem.attrValue);
        }else if(hour === 9) {
            m.labelsCount[9] += 1;
            m.labelsSum[9] += parseFloat(elem.attrValue);
        }else if(hour === 10) {
            m.labelsCount[10] += 1;
            m.labelsSum[10] += parseFloat(elem.attrValue);
        }else if(hour === 11) {
            m.labelsCount[11] += 1;
            m.labelsSum[11] += parseFloat(elem.attrValue);
        }else if(hour === 12) {
            m.labelsCount[12] += 1;
            m.labelsSum[12] += parseFloat(elem.attrValue);
        }else if(hour === 13) {
            m.labelsCount[13] += 1;
            m.labelsSum[13] += parseFloat(elem.attrValue);
        }else if(hour === 14) {
            m.labelsCount[14] += 1;
            m.labelsSum[14] += parseFloat(elem.attrValue);
        }else if(hour === 15) {
            m.labelsCount[15] += 1;
            m.labelsSum[15] += parseFloat(elem.attrValue);
        }else if(hour === 16) {
            m.labelsCount[16] += 1;
            m.labelsSum[16] += parseFloat(elem.attrValue);
        }else if(hour === 17) {
            m.labelsCount[17] += 1;
            m.labelsSum[17] += parseFloat(elem.attrValue);
        }else if(hour === 18) {
            m.labelsCount[18] += 1;
            m.labelsSum[18] += parseFloat(elem.attrValue);
        }else if(hour === 19) {
            m.labelsCount[19] += 1;
            m.labelsSum[19] += parseFloat(elem.attrValue);
        }else if(hour === 20) {
            m.labelsCount[20] += 1;
            m.labelsSum[20] += parseFloat(elem.attrValue);
        }else if(hour === 21) {
            m.labelsCount[21] += 1;
            m.labelsSum[21] += parseFloat(elem.attrValue);
        }else if(hour === 22) {
            m.labelsCount[22] += 1;
            m.labelsSum[22] += parseFloat(elem.attrValue);
        }else if(hour === 23) {
            m.labelsCount[23] += 1;
            m.labelsSum[23] += parseFloat(elem.attrValue);
        }
    }
    else {
        //m.series.push(ano+'-'+mes+'-'+dia);
    }
    //m.data[0].push(parseFloat(elem.attrValue));
})

for(i=0; i<24;++i) {
    if(m.labelsCount[i] === 0)
        m.data[0].push(0);
    else
        m.data[0].push(parseFloat(m.labelsSum[i])/parseFloat(m.labelsCount[i]));
}

return {payload:[m],topic:msg.topic};
