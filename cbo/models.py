import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `user_id` VARCHAR(255) NOT NULL COMMENT '主键，U开头',
#  `user_psd` VARCHAR(255) NOT NULL COMMENT '非空',
#  `user_name` VARCHAR(255) NOT NULL COMMENT '非空',
#  `user_info` VARCHAR(255),
#  `user_like` INTEGER NOT NULL COMMENT '最小值0',
#  `user_fans` INTEGER NOT NULL COMMENT '最小值0',
#  `user_follow` INTEGER NOT NULL COMMENT '最小值0',
#  `user_img` VARCHAR(255) NOT NULL,
#  `user_ip` VARCHAR(255) NOT NULL COMMENT '非空',
#  `user_blog_num` INTEGER NOT NULL COMMENT '最小值0',
#  `user_emial` VARCHAR(255) NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('姓名', max_length=50, default='匿名用户')
    introduce = models.TextField('简介', default='暂无介绍')
    company = models.CharField('公司', max_length=100, default='暂无信息')
    profession = models.CharField('职业', max_length=100, default='暂无信息')
    address = models.CharField('住址', max_length=100, default='暂无信息')
    telephone = models.CharField('电话', max_length=11, default='暂无信息')
    wx = models.CharField('微信', max_length=50, default='暂无信息')
    qq = models.CharField('QQ', max_length=50, default='暂无信息')
    wb = models.CharField('微博', max_length=100, default='暂无信息')
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name='邮箱')
    photo = models.ImageField('头像', blank=True, upload_to='images/user/')
    like = models.IntegerField('点赞数', default=0)
    fans = models.IntegerField('粉丝数', default=0)
    follow = models.IntegerField('关注数', default=0)
    blog_num = models.IntegerField('博客数', default=0)

    class Meta:
        db_table = 'user'

        # 设置返回值

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        使用给定的用户名、电子邮件和密码创建并保存用户。
        """
        # 如果没有username则抛出异常
        if not username:
            raise ValueError('The given username must be set')
        # 标准化电子邮件，查看源码会发现是用@进行分割
        email = self.normalize_email(email)
        # 标准化用户名
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        # 为用户设置密码，将纯文本密码转换为用于数据库存储的哈希值
        user.set_password(password)
        # 保存用户
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        # 设置is_staff默认值为False，is_superuser默认值为False
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        # 设置is_staff默认值为True，is_superuser默认值为True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # 如果调用此方法，is_staff必须为True，否则会抛出异常
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        # 如果调用此方法，is_superuser必须为True，否则会抛出异常
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `bolg_id` VARCHAR(255) NOT NULL COMMENT '主键，自增，B开头',
#  `user_id` VARCHAR(255) NOT NULL COMMENT '外键',
#  `blog_title` VARCHAR(255) NOT NULL COMMENT '最小1，最大30',
#  `blog_content` VARCHAR(255) NOT NULL COMMENT '最10，最大40000',
#  `blog_img` VARCHAR(255),
#  `blog_time` DATETIME NOT NULL,
#  `blog_liked` INTEGER NOT NULL COMMENT '最小0',
#  `blog_comment_num` INTEGER NOT NULL COMMENT '最小0',
#  `blog_visited` INTEGER NOT NULL COMMENT '最小0',
#  `blog_label` VARCHAR(255) NOT NULL COMMENT '非空',
#  `blog_categroy` VARCHAR(255) NOT NULL COMMENT '非空',
#  `blog_recommand` INTEGER NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Blog(models.Model):
    bolg_id = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255)
    blog_title = models.CharField(max_length=255)
    blog_content = models.CharField(max_length=255)
    blog_img = models.CharField(max_length=255)
    blog_time = models.DateTimeField()
    blog_liked = models.IntegerField()
    blog_comment_num = models.IntegerField()
    blog_visited = models.IntegerField()
    blog_label = models.CharField(max_length=255)
    blog_categroy = models.CharField(max_length=255)
    blog_recommand = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'blog'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `sneaker_id` VARCHAR(255) NOT NULL COMMENT '主键，自增，S开头',
#  `sneaker_brand` VARCHAR(255) NOT NULL,
#  `sneaker_model` VARCHAR(255) NOT NULL COMMENT '如闪现3',
#  `sneaker_rating` DOUBLE PRECISION NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Sneaker(models.Model):
    sneaker_id = models.CharField(max_length=255, primary_key=True)
    sneaker_brand = models.CharField(max_length=255)
    sneaker_model = models.CharField(max_length=255)
    sneaker_rating = models.FloatField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'sneaker'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `brand_id` VARCHAR(255) NOT NULL COMMENT '非空，自增，b开头',
#  `brand_img` VARCHAR(255) NOT NULL COMMENT '非空',
#  `brand_name` VARCHAR(255) NOT NULL COMMENT '非空',
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Brand(models.Model):
    brand_id = models.CharField(max_length=255, primary_key=True)
    brand_img = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'brand'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `blog_id` VARCHAR(255) COMMENT '外键',
#  `sneaker_id` VARCHAR(255) COMMENT '外键',
#  `comment_id` VARCHAR(255) NOT NULL COMMENT '主键，C开头',
#  `user_id` VARCHAR(255) NOT NULL COMMENT '非空',
#  `comment_time` VARCHAR(255) NOT NULL,
#  `comment_content` VARCHAR(255) NOT NULL COMMENT '非空',
#  `father_id` VARCHAR(255) COMMENT '为空表示是评论，否则为评论回复',
#  `user_rating` DOUBLE PRECISION,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Comment(models.Model):
    blog_id = models.CharField(max_length=255)
    sneaker_id = models.CharField(max_length=255)
    comment_id = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255)
    comment_time = models.CharField(max_length=255)
    comment_content = models.CharField(max_length=255)
    father_id = models.CharField(max_length=255)
    user_rating = models.FloatField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'comment'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `user_id` VARCHAR(255) NOT NULL COMMENT '主键，外键',
#  `follower` VARCHAR(255) NOT NULL,
#  `followed` VARCHAR(255) NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Follow(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    follower = models.CharField(max_length=255)
    followed = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'follow'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `like_id` VARCHAR(255) NOT NULL COMMENT '主键，自增',
#  `user_id` VARCHAR(255) NOT NULL,
#  `blog_id` VARCHAR(255) NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Like(models.Model):
    like_id = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255)
    blog_id = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'like'

# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `sneaker_id` VARCHAR(255) NOT NULL COMMENT '外键',
#  `adv_id` VARCHAR(255) NOT NULL COMMENT '主键',
#  `adv_name` VARCHAR(255) NOT NULL,
#  `adv_num` INTEGER NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Adv(models.Model):
    sneaker_id = models.CharField(max_length=255)
    adv_id = models.CharField(max_length=255, primary_key=True)
    adv_name = models.CharField(max_length=255)
    adv_num = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'advantage'


# CREATE TABLE IF NOT EXISTS `tableName` (
#  `id` INTEGER NOT NULL auto_increment,
#  `sneaker_id` VARCHAR(255) NOT NULL COMMENT '外键',
#  `disadv_id` JSON NOT NULL COMMENT '主键',
#  `disadv_name` VARCHAR(255) NOT NULL,
#  `disadv_num` INTEGER NOT NULL,
#  `createdAt` DATETIME NOT NULL,
#  `updatedAt` DATETIME NOT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB;
class Disadv(models.Model):
    sneaker_id = models.CharField(max_length=255)
    disadv_id = models.CharField(max_length=255, primary_key=True)
    disadv_name = models.CharField(max_length=255)
    disadv_num = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'disadvantage'


