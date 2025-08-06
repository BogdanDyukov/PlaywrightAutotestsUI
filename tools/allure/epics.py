from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS system"  # Автотесты написаны только для этой части системы
    STUDENT = "Student system"  # Лишь предполагаем, что эта часть существует
    ADMINISTRATION = "Administration system"  # Лишь предполагаем, что эта часть существует
