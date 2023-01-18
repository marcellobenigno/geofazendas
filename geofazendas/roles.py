from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    pass


class Gestor(AbstractUserRole):
    pass


class Sindicato(AbstractUserRole):
    pass


class Anunciante(AbstractUserRole):
    pass
