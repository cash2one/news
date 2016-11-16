// 路径配置
require.config({
    paths: {
        echarts: 'http://echarts.baidu.com/build/dist'
    }
});
launchExample();

var line_chart;
function launchExample() {
	// 使用
	require(
	    [
	        'echarts',
	        'echarts/chart/line',
            'echarts/chart/bar',
            'echarts/chart/scatter',
            'echarts/chart/radar',
            'echarts/chart/map'
	    ],
	    function (ec) {
	    	// 新增设备时间分布相关变量
	        line_chart = ec.init(document.getElementById('tab_body'), 'macarons'); 
    
		    // 为echarts对象加载数据 
		    line_chart.setOption(optionnewdev()); 
	    }
	);
}

var oCurTabIdx = '';
var rCurTabIdx = '';
$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    // e.target // activated tab
    // e.relatedTarget // previous tab
    // if (!EC_READY || !DATA_READY) {
    //     return;
    // }
    if (e.target.id.match('o-')) {
        // overview
        oCurTabIdx = e.target.id.replace('o-','');
        showTabContent(oCurTabIdx);
    }
    // else {
    //     // ranking
    //     rCurTabIdx = e.target.id.replace('r-','');
    //     showTabContent(3, rCurTabIdx);
    // }
    // window.alert("cur:" + $(e.target).text() + ";/r/nprev:" + $(e.relatedTarget).text())
    // window.alert("cur:" + e.target.id);
});

var functionMap = {};

functionMap.chartnewdev = function(){
    line_chart.hideLoading();
    line_chart.setOption(optionnewdev());
};
functionMap.chartnewuser = function(){
    line_chart.hideLoading();
    line_chart.setOption(optionnewuser());
};

function showTabContent(type){
	if (functionMap['chart' + type])
	{
		functionMap['chart' + type]();
	}
	else
	{
		window.alert('该菜单尚未开放...');
	}
};