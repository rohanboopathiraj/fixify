from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class FixifyUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email: str, password: str | None = None, **other_fields) -> 'FixifyUser':
        """
        Create and return a regular USER with an email and password.
        """

        if not password:
            raise ValueError("Password must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str | None = None, **other_fields) -> 'FixifyUser':
        """
        Create and return a SUPER USER with an email and password.
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)


class FixifyUser(AbstractUser):
    email = models.EmailField(unique=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = FixifyUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='fixifyuser_groups',  # Custom related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='fixifyuser_permissions',  # Custom related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



