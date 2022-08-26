CREATE USER IF NOT EXISTS 'debug' IDENTIFIED BY 'debug';
CREATE DATABASE IF NOT EXISTS `{{ cookiecutter.module_name }}_db`;
GRANT ALL ON `{{ cookiecutter.module_name }}_db`.* TO 'debug'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS `test_{{ cookiecutter.module_name }}_db`;
GRANT ALL ON `test_{{ cookiecutter.module_name }}_db`.* TO 'debug'@'%';
FLUSH PRIVILEGES;
