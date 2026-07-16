# Project Architecture

```
app.py
│
├── src/
│   ├── config.py
│   ├── utils.py
│   └── ai/
│       ├── client.py
│       └── prompts.py
│
├── examples/
│
└── docs/
```

## Purpose

The project is organised into small, reusable modules to keep the code clean, maintainable and easy to expand.

Future AI services will be added inside the `src/ai` package.
