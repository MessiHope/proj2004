# Generated by Django 2.0.1 on 2018-01-14 15:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180114_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, help_text='请填写完整、规范的通讯地址。如在国外，可使用外文地址。', max_length=100, verbose_name='通讯地址'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='industry',
            field=models.CharField(blank=True, choices=[('农、林、牧、渔业', '农、林、牧、渔业'), ('采矿业', '采矿业'), ('制造业', '制造业'), ('电力、热力、燃气及水生产和供应业', '电力、热力、燃气及水生产和供应业'), ('建筑业', '建筑业'), ('批发和零售业', '批发和零售业'), ('交通运输、仓储和邮政业', '交通运输、仓储和邮政业'), ('住宿和餐饮业', '住宿和餐饮业'), ('信息传输、软件和信息技术服务业', '信息传输、软件和信息技术服务业'), ('金融业', '金融业'), ('房地产业', '房地产业'), ('租赁和商务服务业', '租赁和商务服务业'), ('科学研究和技术服务业', '科学研究和技术服务业'), ('水利、环境和公共设施管理业', '水利、环境和公共设施管理业'), ('居民服务、修理和其他服务业', '居民服务、修理和其他服务业'), ('教育', '教育'), ('卫生和社会工作', '卫生和社会工作'), ('文化、体育和娱乐业', '文化、体育和娱乐业'), ('公共管理、社会保障和社会组织', '公共管理、社会保障和社会组织'), ('国际组织', '国际组织'), ('其他', '其他')], max_length=100, verbose_name='所在行业'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='请填写中国大陆格式（固话须带区号）或国际格式（以加号开头）的电话号码，结果将统一为国际格式。', max_length=128, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organization',
            field=models.CharField(blank=True, help_text='请填写工作单位的官方全称。', max_length=100, verbose_name='工作单位'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='请填写中国大陆格式（固话须带区号）或国际格式（以加号开头）的电话号码，结果将统一为国际格式。', max_length=128, verbose_name='固定电话'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wechat',
            field=models.CharField(blank=True, help_text='查看微信号的方法：打开微信→我→微信号。', max_length=100, verbose_name='微信号'),
        ),
    ]
