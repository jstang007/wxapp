//index.js
//获取应用实例
const app = getApp()
const cookieUtils = require('../../utils/cookie.js')

Page({
  data: {
    isAuthorized: false,
    constellationData: null,
    stockData: null,
    weatherData: null,
    userInfo: null,
    hasUserInfo: null
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  updateData: function(){
    wx.showLoading({title: '加载中',})
    var that = this
    var cookie = cookieUtils.getCookieFromStorage()
    var header = {}
    header.Cookie = cookie
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/weather',
      method: 'GET',
      header: header,
      success: function(res){
        that.setData({weatherData: res.data.data})
        wx.hideLoading()
      }
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/stock',
      method: 'GET',
      header: header,
      success: function(res){  
        that.setData({stockData: res.data.data})
        wx.hideLoading()
      }
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/constellation',
      method: 'GET',
      header: header,
      success: function (res) {
        console.log(res)
        that.setData({constellationData: res.data.data})
        wx.hideLoading()
      }
    })
  },
  //下拉刷新,先检查session是否过期，再更新页面数据
  onPullDownRefresh: function(){
    var that = this
    var cookie = cookieUtils.getCookieFromStorage()
    var header = {}
    header.Cookie = cookie
    wx.request({
      url: app.globalData.serverUrl+app.globalData.apiVersion+'/auth/status',
      header: header,
      success: function(res){
        var data = res.data.data
        if (data.is_authorized ==1){
          that.setData({isAuthorized: true})
          that.updateData()
        }else{
          that.setData({isAuthorized: false})
          wx.showToast({
            title: '请先登陆',
            icon: 'none'
          })
        }
      }
    })
  },
  onLoad: function () {
    this.onPullDownRefresh()
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },  
  teststorage: function(event){
    wx.setStorage({
      key: 'mykey',
      data: 'mydata',
    })
    wx.getStorage({
      key: 'mykey',
      success: function(res) {
        console.log(res.data)
      },
    })
  }
})
