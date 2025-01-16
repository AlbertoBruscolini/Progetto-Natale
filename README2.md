# Progetto NATALEEEE - main.py

Questo progetto è un'applicazione web di quiz sviluppata con Flask. Il file `main.py` contiene il codice principale dell'applicazione, inclusa la configurazione di Flask, la definizione delle route e la logica del quiz.

## Struttura del Codice

### Importazioni

```python
from flask import Flask, render_template, request, redirect, url_for, session
import random
