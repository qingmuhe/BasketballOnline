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
class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_psd = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_info = models.CharField(max_length=255)
    user_like = models.IntegerField()
    user_fans = models.IntegerField()
    user_follow = models.IntegerField()
    user_img = models.CharField(max_length=255)
    user_ip = models.CharField(max_length=255)
    user_blog_num = models.IntegerField()
    user_emial = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'user'



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


