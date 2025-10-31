"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. "
            "Убедитесь, что Django установлена и "
            "активировано виртуальное окружение."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
