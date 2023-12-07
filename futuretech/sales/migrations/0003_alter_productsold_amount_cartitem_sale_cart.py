# Generated by Django 4.2.7 on 2023-12-05 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_discountpercentage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0002_remove_productsold_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsold',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.cartitem'),
        ),
    ]
