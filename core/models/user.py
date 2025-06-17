"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

OBJETIVO_CHOICES = [
    ('hipertrofia', 'Hipertrofia'),
    ('emagrecimento', 'Emagrecimento'),
    ('definicao', 'Definição'),
]

NIVEL_CHOICES = [
    ('sedentário','Sedentário'),
    ('leve', 'Leve'),
    ('moderado', 'Moderado'),
    ('intenso', 'Intenso'),
    ('atleta', 'Atleta')
]

ALIMENTACAO_CHOICES = [
    ('vegano','Vegano'),
    ('vegetariano', 'Vegetariano'),
    ('sem gluten', 'Sem Gluten'),
    ('sem lactose', 'Sem Lactose'),
    ('sem restrições', 'Sem Restrições')
]


class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""
    
    nome = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email'), help_text=_('Email'))
    senha = models.CharField(max_length=128, blank=True)
    idade = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(120)], default=0)
    peso = models.FloatField(validators=[MinValueValidator(10), MaxValueValidator(500)], default=0)
    altura = models.FloatField(validators=[MinValueValidator(10), MaxValueValidator(120)], default=0)
    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES, default='definição')
    nivelatv = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='leve')
    alimentacao = models.CharField(max_length=20,choices=ALIMENTACAO_CHOICES, default='sem restrições')
    passage_id = models.CharField(max_length=255, unique=True,      verbose_name=_('passage_id'), help_text=_('Passage ID'))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('name'), help_text=_('Username'))
    is_active = models.BooleanField(
        default=True, verbose_name=_('Usuário está ativo'), help_text=_('Indica que este usuário está ativo.')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Usuário é da equipe'),
        help_text=_('Indica que este usuário pode acessar o Admin.'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
