// pages/weather/weather.js

const app = getApp()
const popularCities = '{"cities": ["深圳", "广州", "北京", "上海"]}'
Page({
  /**
   * 页面初始数据
   */
  data: {
    isAuhtorized: false,
    weatherData: null
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options){
    this.updateWeatherData()
  },
  updateWeatherData: function(){
    var that = this
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion+'/service/weather',
      method: 'POST',
      data: {
        cities: popularCities
      },  
      success: function(res){
        var tmpData = res.data.data
        that.setData({weatherData: tmpData})
        wx.hideLoading()
      }
    })
  },
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function(){
    this.updateWeatherData()
  }
})