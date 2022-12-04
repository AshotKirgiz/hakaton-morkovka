# hakaton-morkovka

Стак технологий:
  
  Бэк: django 3.2.16, Pillow 9.3.0, sqlite 3, javascript;
  Фронт: html 5, css 4;
  Дизайн: illustrator 23, figma;

Запуск проекта:

Для запуска проекта требуется клонировать репозиторий с гит хаба (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). После клонирования требуется установить python последней версии. Папку проекта надо открыть через cmd и установить django и pillow, используя команду pip install <name>==<version>. Перед запуском сервера нужно прописать две команды: python manage.py makemigrations  и  python manage.py migrate 
Развертывание сервера происходит за счет команды python manage.py runserver. Файл manage.py находится в основной папке репозитория. Сервер работает по адресу http://127.0.0.1:8000 или проще говоря localhost:8000. С этого момента по вышесказанному адресу у вас будет работать сайт. Подробнее с документацией можно ознакомиться здесь - https://docs.djangoproject.com/en/4.1/#index-first-steps

Подробное описание файла и их предназначения можно найти в коде и здесь - https://docs.djangoproject.com/en/4.1/

Ветки url адресов:
1. admin/ используется для администрации сайта, просмотру базы данных и всех действий, связанных с информацией пользователя.
2. home/ используется для главной страницы, котораяперенаправляет нас на остальные.
3. accounts/ основная ветка url адресов.

    account/user - личный кабинет пользователя, который подал заявку
    
    account/admin - личный кабинет эксперта
    
    login/ - страница входа
    
    logout/ - функция выхода из аккаунта
    
    register/ - страница регистрации
    
    bids/ - страница просмотора всех заявок
    
    bids/bids-detail - страница детальной информации о заявке
    
    bids/bids-mark - оценка заявки
    
    bids/bids-mark/printed-editions - страница оценки по критериям печатных изданий
    
    bids/bids-mark/lower-criteria - страница занижающих критериев
    
    bids/bids-mark/information_publications - страница оценки по критериям телевизионных материалов
    
    end/ - страница с итоговыми результатами по завершению конкурса
    
