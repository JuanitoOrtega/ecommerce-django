from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
  def create_user(self, username, first_name, last_name, email, password=None):
    if not email:
      raise ValueError('El usuario debe ser un correo electrónico')

    if not username:
      raise ValueError('El nombre de usuario debe ser un seudónimo')

    user = self.model(
      email = self.normalize_email(email),
      username = username,
      first_name = first_name,
      last_name = last_name,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, first_name, last_name, email, password):
    user = self.create_user(
      email = self.normalize_email(email),
      username = username,
      first_name = first_name,
      last_name = last_name,
      password = password,
    )

    user.is_admin = True
    user.is_active = True
    user.is_staff = True
    user.is_superadmin = True
    user.save(using=self._db)
    return user


class Account(AbstractBaseUser):
  first_name = models.CharField('Nombres', max_length=50)
  last_name = models.CharField('Apellidos', max_length=50)
  username = models.CharField('Nombre de usuario', max_length=50, unique=True)
  email = models.EmailField('Correo electrónico', max_length=100, unique=True)
  phone_number = models.CharField('Teléfono', max_length=50)

  class Meta:
    verbose_name = 'cuenta'
    verbose_name_plural = 'cuentas'

  # Campos atributos de django
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now_add=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  is_superadmin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  objects = MyAccountManager()

  # Para mostrar nombre completo
  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, add_label):
    return True


class UserProfile(models.Model):
  user = models.OneToOneField(Account, on_delete=models.CASCADE)
  address_line_1 = models.CharField('Dirección principal', max_length=100, blank=True)
  address_line_2 = models.CharField('Dirección secundaria', max_length=100, blank=True)
  profile_picture = models.ImageField('Ávatar', blank=True, upload_to='userprofile')
  city = models.CharField('Ciudad', max_length=20, blank=True)
  state = models.CharField('Estado', max_length=20, blank=True)
  country = models.CharField('País', max_length=20, blank=True)

  class Meta:
    verbose_name = 'perfil de usuario'
    verbose_name_plural = 'perfil de usuarios'

  def __str__(self):
    return self.user.first_name

  def full_address(self):
    return f'{self.address_line_1} {self.address_line_2}'