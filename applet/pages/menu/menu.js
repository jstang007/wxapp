const app = getApp()
Page({
  //页面初始数据
  data: {
    grids: [{name:'应用1'},{name:'应用2'}]
  },//九宫格内容
  //生命周期函数--监听页面加载
  onLoad: function(options){
    this.updateMenuData()
  },
  //请求后台，更新demogrid数据
  updateMenuData: function(){
    var that = this
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion+'/service/menu',
      success: function(res){
        var menuData = res.data.data
        that.setData({
          grids: menuData
        })
      }
    }) 
  },
  onNavigatorTap: function(e){
    var index = e.currentTarget.dataset.index
    var appItem = this.data.grids[index]
    if (appItem.app.application == 'weather'){
      wx.navigateTo({
        url: '../weather/weather',
      })
    }
  }
});