from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.core.validators import MaxLengthValidator, MinLengthValidator

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None, **kwargs):
        """Create and return a `User` with an email, username and password."""
        if not username:
            raise TypeError("Users must have a username.")

        if not password:
            raise TypeError("User must have a  papssword.")

        user = self.model(
            username=username, password=password, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, email=None, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise TypeError("Superusers must have a password.")

        if not username:
            raise TypeError("Superusers must have a unique username.")

        user = self.create_user(
            username=username, password=password, email=email, **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    first_name = models.CharField(
        _("First name"),
        max_length=200,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        _("Last name"),
        max_length=200,
        null=False,
        blank=False,
    )
    username = models.CharField(
        _("Username"),
        max_length=200,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        _("Email"),
        max_length=200,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        _("date created"),
        editable=False,
        auto_now_add=True,
    )
    objects = UserManager()
    
    def __str__(self):
        if self.first_name & self.last_name:
            return f"{self.first_name} {self.last_name}-G{self.grade}"
        else:
            return f"{self.username}-G{self.grade}"

    class Meta:
        ordering = ["-created"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserProfile(models.Model):
    SEX_CHOICES = (
        ("Male", ("Male")),
        ("Female", ("Female")),
    )
    """
    A model for storing addtional imformation about User.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = ProcessedImageField(
        upload_to="profile_photo",
        processors=[ResizeToFill(512, 512)],
        format="JPEG",
        options={"quality": 100},
        null=True,
        blank=True,
    )
    sex = models.CharField(
        _("Sex"),
        max_length=100,
        choices=SEX_CHOICES,
        null=True,
        blank=True
    )
    
    grade = models.SmallIntegerField(
        verbose_name=_("Grade"),
        null=True,
        blank=False,
    )
    class_label = models.PositiveSmallIntegerField(
        verbose_name=_("Class label"),
        null=True,
        blank=False,
    )
    about_me = models.CharField(
        _("About Me"),
        max_length=400,
        null=True,
        blank=True
    )
    cell = models.CharField(
        _("Phone Number"),
        max_length=50, 
        null=True, 
        blank=True,
    )
    cell = models.CharField(
        _("Other Phone Number (optional)"),
        max_length=50, 
        null=True, 
        blank=True,
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}'s Profile"
        else:
            return f"{self.user.username}'s Profile"

    @property
    def profile_photo_url(self):
        if self.profile_photo:
            return self.profile_photo.url
        return os.path.join(
            settings.STATIC_URL,
            "assets/logos/invalid-profile-photo.jpg"
        )
