<template>
	<div id="map">
		<div id="allmap" ref="allmap"></div>
	</div>
</template>
<script>
	export default {
		name: "BaiduMap",
		methods: {
			map() {
				let map = new window.BMap.Map(this.$refs.allmap); // 创建Map实例
				map.centerAndZoom(new window.BMap.Point(116.404, 39.915), 11); // 初始化地图,设置中心点坐标和地图级别
				map.addControl(new BMap.NavigationControl());    
				map.addControl(new BMap.ScaleControl());    
				map.addControl(new BMap.OverviewMapControl());    
				map.addControl(new BMap.MapTypeControl());   
				map.setCurrentCity("北京"); // 设置地图显示的城市 此项是必须设置的
				map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放
			},
		},
		data() {
            return{
                
            }
		},
		mounted() {
			this.map();
		},
	};
</script>
<style>
#map{
    width: 100%;
    height: 100%;
}
	#allmap {
		width: 100%;
        height: 100%;
		overflow: hidden;
	}
</style>

