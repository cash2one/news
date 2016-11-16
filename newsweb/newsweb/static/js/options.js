function optionnewdev() {
	var result = {}
	result = {
	    title: {
	        text: '新增设备时间分布',
	        x: 'center',
	        y: 'top'
	    },
	    tooltip : {
	        trigger: 'axis'
	    },
	    legend: {
	        data:['今天','昨天'],
	        x: 'center',
	        y: 'bottom'
	    },
	    toolbox: {
	        show : true,
	        feature : {
	            saveAsImage : {show: true}
	        }
	    },
	    calculable : true,
	    xAxis : [
	        {
	            type : 'category',
	            boundaryGap : false,
	            data : ['周一','周二','周三','周四','周五','周六','周日']
	        }
	    ],
	    yAxis : [
	        {
	            type : 'value'
	        }
	    ],
	    series : [
	        {
	            name:'今天',
	            type:'line',
	            stack: '总量',
	            data:[120, 132, 101, 134, 90, 230, 210]
	        },
	        {
	            name:'昨天',
	            type:'line',
	            stack: '总量',
	            data:[220, 182, 191, 234, 290, 330, 310]
	        }
	    ]
	};
	return result;
}

function optionnewuser() {
	var result = {}
	result = {
	    title: {
	        text: '新增用户时间分布',
	        x: 'center',
	        y: 'top'
	    },
	    tooltip : {
	        trigger: 'axis'
	    },
	    legend: {
	        data:['今天','昨天'],
	        x: 'center',
	        y: 'bottom'
	    },
	    toolbox: {
	        show : true,
	        feature : {
	            saveAsImage : {show: true}
	        }
	    },
	    calculable : true,
	    xAxis : [
	        {
	            type : 'category',
	            boundaryGap : false,
	            data : ['周一','周二','周三','周四','周五','周六','周日']
	        }
	    ],
	    yAxis : [
	        {
	            type : 'value'
	        }
	    ],
	    series : [
	        {
	            name:'今天',
	            type:'line',
	            stack: '总量',
	            data:[120, 132, 181, 134, 90, 230, 210]
	        },
	        {
	            name:'昨天',
	            type:'line',
	            stack: '总量',
	            data:[220, 182, 191, 234, 290, 330, 310]
	        }
	    ]
	};
	return result;
}