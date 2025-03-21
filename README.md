# CI/CD, Github Actions, ArgoCD
CI/CD, Github Actions, ArgoCD : непрерывная интеграция,
 развертывание и доставка

Итоговый результат:
1. CI-пайплайн:
    - Успешно проходит линтинг, юнит-тесты и сборку Docker-образа.
    - Запускается при пуше в ветку dev.
2. CD-пайплайн:
    - Публикует образ в Docker Hub.
    - Обновляет манифесты в репозитории.
3. ArgoCD:
    - Автоматически разворачивает приложение в Kubernetes.
    - Статус приложения: Healthy и Synced.

Подробное описание и скриншоты с выполнением лабораторной работы в файле "Отчет 12"

![image](https://github.com/user-attachments/assets/dddcf3ba-3e67-4a61-9160-01e9b0454c85)

![image](https://github.com/user-attachments/assets/d41b6688-c232-48cb-aabc-2b34893a436c)

![image](https://github.com/user-attachments/assets/30ede4e6-0557-4827-b13e-34a2b953d4bd)



