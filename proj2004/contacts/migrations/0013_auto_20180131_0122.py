# Generated by Django 2.0.1 on 2018-01-30 17:22

import contacts.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_profile_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='attend',
            field=models.NullBooleanField(help_text='全校秩年校庆活动安排在2018年4月29日，欢迎各位返校参与。', verbose_name='是否参加秩年校庆活动'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, help_text='如要要办理校友卡，请上传证件照。要求为近期免冠彩色照，白底，竖版。上传后系统将自动把照片调整为400×500的尺寸。', upload_to=contacts.models.get_photo_upload_path, verbose_name='校友卡证件照'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='remark',
            field=models.CharField(blank=True, help_text='如果以上内容有特殊情况的，可在备注栏中说明。例如：学籍信息有误；有转系情况；有多个手机号、邮箱；有多个常住地等。', max_length=250, verbose_name='备注'),
        ),
    ]