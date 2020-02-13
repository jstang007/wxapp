const app = getApp()
const imageUrl = app.globalData.serverUrl + app.globalData.apiVersion+ '/service/image'
Page({
  data:{
    needUploadFiles: [], //需要上传的图片
    downloadedBackupedFiles: [],//已下载的备份图片
  },
  //选择图片上传
  chooseImage: function(e){
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'],//可指定原图/压缩图，默认均有
      sourceType: ['album', 'camera'],//可指定来源是相册/相机，默认均有
      success: function(res) {
        //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({needUploadFiles: that.data.needUploadFiles.concat(res.tempFilePaths)});
      },
    })
  },
  //上传图片
  uploadFiles: function(){
    var that = this
    for (var i = 0;i<this.data.needUploadFiles.length;i++){
      var filePath = this.data.needUploadFiles[i]
      wx.uploadFile({
        url: imageUrl,
        filePath: filePath,
        name: 'test',
        success: function(res){
          // that.setData({ downloadedBackupedFiles: []})  //从新加载
          // that.onLoad()
          var res = JSON.parse(res.data)
          var md5 = res.data[0].md5
          var name = res.data[0].name
          var newImageItem = {"md5":md5,"name":name}
          that.downloadFile(newImageItem)
        }
      })
    }
    wx.showToast({
      title: '上传成功',
    })
    this.setData({ needUploadFiles: [] })
  },
  //下载图片
  downloadFile: function (imgItem) {
    var that = this
    var downloadUrl = imageUrl + '?md5=' + imgItem.md5
    wx.downloadFile({
      url: downloadUrl,
      success: function (res) {
        var filepath = res.tempFilePath //获取到的图片存入临时本地路径
        console.log(filepath)
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        imgItem.path = filepath   //增加path字段
        newDownloadedBackupedFiles.push(imgItem) //操作数组，相当于append
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles //存入全局变量数组中
        })
        console.log(newDownloadedBackupedFiles)
      }
    })
  },
  //删除图片
  deleteBackup: function(imgItem){
    wx.request({
      url: imageUrl+'?md5=' + imgItem.md5,
      method: 'DELETE',
      success: function(res){
        console.log(res.log)
        wx.showToast({
          title: '删除成功！',
        })
      }
    })
  },
  onLoad: function(){
    this.downloadAllFromRemote()
    console.log('已进入onload')
  },
  //下载所有已备份的图片，后台文件夹存在的图片
  downloadAllFromRemote: function(){
    var that =this
    wx.request({
      url: imageUrl+'/list',
      success: function(res){
        var imageList = res.data.data
        for (var i=0;i<imageList.length;i++){
          var imgItem = imageList[i]
          that.downloadFile(imgItem)
          console.log('转交给downloadFile')
        }
      }
    })
  },
  //长按确认函数
  longTapConfirm: function(e){
    var that =this
    var confirmList = ["删除备份"]
    wx.showActionSheet({  //弹出框框
      itemList: confirmList,
      success: function(res){
        if(res.cancel){return}
        var imageIndex = e.currentTarget.dataset.index
        var imageItem = that.data.downloadedBackupedFiles[imageIndex]
        var newList = that.data.downloadedBackupedFiles //从全局数组中移除
        newList.splice(imageIndex, 1)
        that.setData({downloadedBackupedFiles: newList})
        that.deleteBackup(imageItem)
      }
    })
  }
  //上传图片文件
});