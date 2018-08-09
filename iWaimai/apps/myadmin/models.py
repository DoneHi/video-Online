# from django.db import models
# from datetime import  datetime
# # Create your models here.
# class Video(models.Model):
#     title=models.CharField(max_length=255,verbose_name='主题')
#     description=models.CharField(max_length=1000,verbose_name='描述')
#     author=models.CharField(max_length=50,verbose_name='作者')
#     create_time=models.DateTimeField(verbose_name='创建时间')
#     times=models.IntegerField(max_length=5000,verbose_name='次数')
#     status=models.IntegerField(max_length=1,verbose_name='状态')
#     class Meta:
#         verbose_name='视频归属'
#         verbose_name_plural=verbose_name
#
# class VideoComments(models.Model):
#     user = models.ForeignKey(UserP, verbose_name='用户')
#     video = models.ForeignKey(Video, verbose_name='课程')
#     fav_id = models.IntegerField(default=0, verbose_name='数据id')
#     fav_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '讲师')), default=0, verbose_name='收藏类型')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')
#     class Meta:
#         verbose_name = '视频'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name