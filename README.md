**LaetusBB**

Features:
* Purely SSR
* BBCode support

Limitations:
* Only basic/old-school session auth for now

# How to Run
1. Generate a .env and siteconf.ini of your own from the examples provided
2. `python manage.py runserver` (Debug Server)

# Project Structure

```
laetusbb
│
└── laetusbb/
└── core/
└── apps/
│   └── thread/
│   └── user/
```


* core:
    * Forum models
    * entry point

* apps/thread:
    * Handle threads, posts, attachments, etc.

* apps/user:
    * [User profiles](https://docs.conan.io/en/latest/howtos/manage_gcc_abi.html)
