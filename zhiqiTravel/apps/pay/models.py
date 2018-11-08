from django.db import models
from datetime import datetime

from users.models import MyUser, TheContact
from operation.models import ShoppingCart


class OrderItems(models.Model):
    user = models.ForeignKey(MyUser, verbose_name='下单用户', on_delete=models.CASCADE)
    good = models.ForeignKey(ShoppingCart, verbose_name='购买的商品信息', on_delete=models.CASCADE)
    order_num = models.CharField(max_length=25, verbose_name='订单号')

    class Meta:
        verbose_name = '用户购买商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.good.product.name


# Create your models here.
class GoodsOrdersMainTable(models.Model):
    order_num = models.CharField(max_length=25, verbose_name='订单号')
    order_describe = models.CharField(max_length=30, verbose_name='订单描述')
    total_amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="订单的资金总额")
    consignee = models.CharField(max_length=30, verbose_name='收货人')
    address = models.CharField(max_length=100, verbose_name='详细地址')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    zip_code = models.CharField(max_length=6, verbose_name='邮政编码')
    order_state = models.CharField(max_length=3, choices=(('wzf', '未支付'),
                                                          ('yzf', '已支付'),
                                                          ('ywc', '已完成'),
                                                          ), default='wzf', verbose_name='订单状态')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='订单提交时间')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='订单支付时间')
    finish_time = models.DateTimeField(null=True, blank=True, verbose_name='订单完成时间')

    class Meta:
        verbose_name = '商品订单主表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_describe