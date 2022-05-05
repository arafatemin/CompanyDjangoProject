from django.db import models
# python manage.py makemigrations
# python manage.py migrate



class Category(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    slug = models.SlugField(allow_unicode=True)
    def __str__(self):
        return self.title

class Urunler(models.Model):
    sz                      = (
                                ("S", "S"),
                                ("XS", "XS"),
                                ("M", "M"),
                                ("L", "L"),
                                ("XL", "XL"),
                                ("XXL", "XXL")
                                )

    cr                       = (
                                ("Black", "Black"),
                                ("White", "White"),
                                ("Yellow", "Yellow"),
                                ("Red", "Red"),
                                ("Blue", "Blue"),
                                ("Green", "Green")
                            )

    bm                       = (
                                ("TL", "TL"),
                                ("$", "$"),
                                ("Euro", "Euro"),
                                )
    name                    = models.CharField(max_length=64, blank=True, null=True)
    slug                    = models.SlugField(allow_unicode=True)
    price                   = models.FloatField(max_length=7, blank=True, null=True)
    birim                   = models.CharField(blank=True, null=True, max_length=64, choices=bm)
    img                     = models.ImageField(upload_to='urunler', blank=True, null=True)
    date                    = models.DateTimeField(auto_now_add=True)
    count                   = models.IntegerField()
    size                    = models.CharField(blank=True, null=True, max_length=64, choices=sz)
    color                   = models.CharField(blank=True, null=True, max_length=64, choices=cr)
    description             = models.TextField()
    category                = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]




    # @property
    # def imageURL(self):
    #     try:
    #         url = self.img.url
    #     except:
    #         url = ''
    #     return url
    


    def __str__(self):
        return self.name + ' ' + str(self.count)


class Employee(models.Model):
    name                    = models.CharField(max_length=64, blank=True, null=True)
    slug                    = models.SlugField(allow_unicode=True)
    phone                   = models.CharField(max_length=15, null=True, blank=True)
    email                   = models.EmailField(blank=True, null=True)
    img                     = models.ImageField(upload_to='employee', blank=True, null=True)
    profession              = models.CharField(max_length=64, blank=True, null=True)
    experience1             = models.TextField()
    experience2             = models.TextField()
    experience3             = models.TextField()
    description             = models.TextField()


    # @property
    # def imageURL(self):
    #     try:
    #         url = self.img.url
    #     except:
    #         url = ''
    #     return url

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class AboutUs(models.Model):
    visyon                  = models.TextField()
    misyon                  = models.TextField()
    img                     = models.ImageField(upload_to='aboutus', blank=True, null=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=64, blank=True, null=False)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    tel = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name















