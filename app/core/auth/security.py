"""
Archivo que contiene la clase Hasher, la cual proporciona métodos para trabajar con contraseñas y hashes.
"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    """
    Esta clase proporciona métodos para trabajar con contraseñas y hashes.
    """

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        Verifica si una contraseña en texto plano coincide con su versión hasheada.

        :param plain_password: La contraseña en texto plano que se va a verificar.
        :type plain_password: str
        :param hashed_password: La versión hasheada de la contraseña almacenada.
        :type hashed_password: str
        :return: True si la contraseña coincide, False si no coincide.
        :rtype: bool
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str):
        """
        Genera un hash a partir de una contraseña en texto plano.

        :param password: La contraseña en texto plano que se va a hashear.
        :type password: str
        :return: El hash resultante de la contraseña.
        :rtype: str
        """
        return pwd_context.hash(password)
