# Generated by Django 2.2.2 on 2020-10-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo', '0008_kontaktperson_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesign',
            name='year',
            field=models.PositiveIntegerField(choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020),
        ),
    ]
